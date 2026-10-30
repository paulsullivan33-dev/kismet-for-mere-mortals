#!/usr/bin/env python3
"""Hand-build a small 802.11 capture (radiotap + raw frames) for the lab.

Invented devices only: two access points and one client, on paper
channels 6 and 1. Writes lab-capture.pcap next to this script.
"""
import struct
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "lab-capture.pcap")

RADIOTAP = bytes([0, 0, 8, 0, 0, 0, 0, 0])  # version, pad, len=8, no fields


def tag(tid, body):
    return bytes([tid, len(body)]) + body


def beacon(bssid, src, ssid, channel, seq):
    fc = struct.pack("<H", 0x0080)          # type 0, subtype 8 (beacon)
    dur = b"\x00\x00"
    dst = b"\xff\xff\xff\xff\xff\xff"       # broadcast
    hdr = fc + dur + dst + src + bssid + struct.pack("<H", seq << 4)
    fixed = struct.pack("<QHH", 0, 100, 0x0431)  # ts, interval, caps ESS+priv off
    tags = (tag(0, ssid.encode())
            + tag(1, bytes([0x82, 0x84, 0x8b, 0x96]))          # rates
            + tag(3, bytes([channel]))                        # DS params
            + tag(5, bytes([0, 1, 0, 0, 0, 0, 0, 0])))        # TIM
    return hdr + fixed + tags


def probe_req(client, ssid, seq):
    fc = struct.pack("<H", 0x0040)          # type 0, subtype 4 (probe req)
    dur = b"\x00\x00"
    dst = b"\xff\xff\xff\xff\xff\xff"
    bssid = b"\xff\xff\xff\xff\xff\xff"
    hdr = fc + dur + dst + client + bssid + struct.pack("<H", seq << 4)
    tags = (tag(0, ssid.encode())
            + tag(1, bytes([0x02, 0x04, 0x0b, 0x16])))
    return hdr + tags


def probe_resp(bssid, client, ssid, channel, seq):
    fc = struct.pack("<H", 0x0050)          # type 0, subtype 5 (probe resp)
    dur = b"\x00\x00"
    hdr = fc + dur + client + bssid + bssid + struct.pack("<H", seq << 4)
    fixed = struct.pack("<QHH", 0, 100, 0x0431)
    tags = (tag(0, ssid.encode())
            + tag(1, bytes([0x82, 0x84, 0x8b, 0x96]))
            + tag(3, bytes([channel])))
    return hdr + fixed + tags


AP1 = bytes.fromhex("021122334401")   # CafeWiFi, channel 6
AP2 = bytes.fromhex("021122334402")   # LibraryNet, channel 1
CLIENT = bytes.fromhex("02aabbccdd01")

frames = []
for i in range(6):
    frames.append(beacon(AP1, AP1, "CafeWiFi", 6, i))
for i in range(6):
    frames.append(beacon(AP2, AP2, "LibraryNet", 1, i))
frames.append(probe_req(CLIENT, "CafeWiFi", 1))
frames.append(probe_resp(AP1, CLIENT, "CafeWiFi", 6, 20))
frames.append(probe_req(CLIENT, "", 2))  # broadcast probe

with open(OUT, "wb") as f:
    # pcap global header, DLT_IEEE802_11_RADIO (127)
    f.write(struct.pack("<IHHiIII", 0xA1B2C3D4, 2, 4, 0, 0, 65535, 127))
    ts = 1767225600  # 2026-01-01 00:00:00 UTC, arbitrary lab time
    for i, fr in enumerate(frames):
        pkt = RADIOTAP + fr
        f.write(struct.pack("<IIII", ts, i * 1000, len(pkt), len(pkt)))
        f.write(pkt)

print(f"wrote {OUT}: {len(frames)} frames, "
      f"{os.path.getsize(OUT)} bytes")
