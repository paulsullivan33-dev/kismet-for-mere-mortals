# Replaying a Capture

**Outcome: Kismet finds real devices
inside a capture file you feed it —
every later skill in this guide,
practised on a file that cannot
embarrass anyone.** This is the
chapter the whole lab stands on.

## The file is an antenna

A **pcap file** is a recording of
network frames — the standard
container Wireshark and tcpdump also
use. Kismet's `kismet_cap_pcapfile`
tool plays one back as a data
source, handing the server each
frame as if a radio had just
received it. The server cannot tell
the difference, and does not need
to: the code that turns frames into
devices is the same either way.

That makes a capture file the safest
classroom in wireless work. No
transmitting (there never is), no
neighbours in the data unless the
file brought them, no adapter to
buy, and the experiment replays
identically forever. Professionals
use the same trick to test; you are
about to use it to learn.

## The lab's capture

The repo carries the generator:
`kismet-lab/make_pcap.py` writes
fifteen frames by hand — beacons
from two invented access points,
`CafeWiFi` on channel 6 and
`LibraryNet` on channel 1, probe
requests from one invented client,
and one probe response. Invented
names, locally-administered
addresses (the `02:` first byte is
the giveaway — real manufacturers'
addresses do not start that way),
an arbitrary timestamp. Run it:

```bash
python3 kismet-lab/make_pcap.py
```

```text
wrote lab-capture.pcap: 15 frames, 1303 bytes
```

A capture of your own, from any
source you have the right to use,
works in its place — a file from a
previous Kismet run's conversion
(chapter 10), or one tcpdump made on
your own network.

## Feed it to Kismet

```bash
kismet -c /path/to/lab-capture.pcap:type=pcapfile
```

Two console lines are the whole
ceremony (transcript t02):

```text
INFO: Data source '.../lab-capture.pcap:type=pcapfile' launched successfully
INFO: Pcapfile '.../lab-capture.pcap' closed: end of pcapfile reached
```

The second line deserves a pause,
because everyone misreads it once:
*closed* here is **success**. The
file has fifteen frames; Kismet read
fifteen frames; the source's work is
done. The server keeps running, and
— this is the part that matters —
**the devices stay**. A replayed
network does not vanish when its
recording ends, any more than a live
one vanishes when an access point is
unplugged. It ages, quietly, in the
list.

## The check

Ask for the devices, in the web
interface or with curl (chapter 8
does this properly; here is the
short form):

```bash
curl -u yourname:yourpassword http://127.0.0.1:2501/system/status.json
```

`kismet.system.devices.count`
should say **3**. Then the device
list names them — the lab's actual
answer, packet for packet:

```text
02:AA:BB:CC:DD:01 | Wi-Fi Client |            | packets: 3
02:11:22:33:44:02 | Wi-Fi AP     | LibraryNet | packets: 6
02:11:22:33:44:01 | Wi-Fi AP     | CafeWiFi   | packets: 7
```

Check the arithmetic, because it is
the frame story told back to you:
six beacons from each access point;
the probe response makes seven for
CafeWiFi; the client sent two
probes and is a party to that same
response — three. Fifteen frames
went in, three devices came out,
nothing invented, nothing lost. If
your counts differ from a file you
built, the frames differ — the
census never lies about its input.
That is exactly the trust you will
need when the input is the sky.
