# Glossary

The terms, collected in one place.

**Access point (AP)** — the radio
that offers a network: a router's
Wi-Fi, a café hotspot. In Kismet's
list, a device of type *Wi-Fi AP*.

**Beacon** — the announcement frame
an access point sends about ten
times a second, carrying its name,
address, channel and abilities. The
census is built mostly of beacons.

**BSSID** — an access point's own
MAC address; the network's
identifier at radio level, as
opposed to the name humans read.

**Capture tool** — one of the small
helper programs (`kismet_cap_*`)
that does the actual hearing for a
kind of source and hands frames to
the server.

**Channel** — one slice of the
Wi-Fi band. A radio listens on one
channel at a time; access points
live on one (or a bonded few).

**Channel hopping** — cycling a
listening radio through the channel
list, dwelling briefly on each, so
one radio can census the whole band
— at sampling speed, not completely.

**Client** — a device that uses
networks rather than offering them:
phones, laptops, gadgets. In the
list, *Wi-Fi Client*.

**Data source** — a configured ear:
a string naming a thing to listen
to and the capture tool that
understands it, as in
`file.pcap:type=pcapfile`.

**Device** — Kismet's unit of
knowledge: one record per radio
identity heard, grown frame by
frame into a dossier.

**Helper binary path** —
(`helper_binary_path`) the config
list of directories Kismet will run
capture tools from; the fence of
chapter 11.

**IEEE 802.11** — the standard
family that defines Wi-Fi; Kismet's
name for its Wi-Fi handling is
*PHY80211*.

**KismetDB** — the log format: the
SQLite database each run writes,
read by the `kismetdb_` tools.

**MAC address** — a device's
hardware address on the network:
maker's prefix plus a unique rest.
Modern devices often broadcast
randomised ones instead.

**Monitor mode** — an adapter state
that delivers every frame heard on
a channel to the computer, and
transmits nothing. The live
listener's posture.

**OUI / manufacturer database** —
the lookup that turns a MAC
address's first bytes into the
maker's name.

**Pcap file** — the standard
recording format for network
frames; Kismet can replay one as a
data source and write one from a
log.

**PHY** — Kismet's word for a radio
family handler (802.11, Bluetooth,
and so on). Each has its own view
of the device list.

**Probe request / probe response** —
a client's call of *"is <network>
there?"* and an access point's
answer. The probe list is how a
client betrays the networks it
remembers.

**Radiotap** — a small header placed
in front of captured frames carrying
radio facts (channel, signal) about
how the frame was heard.

**REST API** — the server's
addressable facts: the same
knowledge as the web interface,
returned as JSON to programs.

**SSID** — a network's human name:
*CafeWiFi*, *LibraryNet*. Offered
by access points, called for by
clients.

**Wardriving** — moving through an
area logging the networks heard,
from the era of doing it by car.
Chapter 2 covers its standing.
