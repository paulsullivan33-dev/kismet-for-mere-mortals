# Kismet for Mere Mortals

Wi-Fi talks whether you listen or not.
Every access point announces its name
ten times a second. Every phone calls
out for the networks it remembers. All
of it travels in the open, as radio,
through the room you are sitting in.
**Kismet** is the program that listens
to that conversation and writes it
down: which networks exist, which
devices are near them, what they are
called, how strong they are, and when
they came and went. It only receives.
It never joins a network, never sends
a packet, and never asks permission —
because radio reception does not work
that way. That one fact shapes
everything in this guide, including
its rules.

This guide explains what Kismet sees
and how it is built, how to install
it, and how to read what it finds.
Then it does something most wireless
guides cannot do in a sandbox: it
proves the listening works. The lab
that wrote this guide had **no Wi-Fi
hardware at all** — no adapter, no
monitor mode, no airwaves. So it built
a tiny stretch of airwaves by hand:
fifteen 802.11 frames written byte by
byte in Python, carrying two invented
access points and one invented client.
Replaying that file through Kismet's
pcap-file data source produced exactly
those three devices in Kismet's list —
names, types and packet counts all
accounted for. The server, the web
interface, the API, the config system
and the log tools all ran for real,
and the transcripts are kept in the
repo. What the lab could not run —
choosing an adapter, monitor mode,
live capture — is taught from the
documentation and labelled as such
wherever it appears. `criteria.md`
keeps the full ledger.

One thing comes before all of that,
and it is not technical. A tool that
hears other people's devices carries
responsibilities, and the law on
listening changes from place to place.
Chapter 2 is short, and it is not
optional reading.

## What this guide covers

- [**What Kismet is**](what-kismet-is.md) —
  the listening model: radios in
  monitor mode, frames in the open, a
  server that turns them into a list
  of devices
- [**The rules of the air**](the-rules-of-the-air.md) —
  the lawful-use chapter: your own
  networks, other people's beacons,
  and where the line runs in plain
  terms
- [**The moving parts**](the-moving-parts.md) —
  the server, the capture tools called
  data sources, the web interface, the
  API, and the log file that remembers
  everything
- [**Installing Kismet**](installing-kismet.md) —
  the project's own packages, and the
  version check that proves it runs
- [**First run — the server and the
  login**](first-run.md) — starting
  Kismet, the first-run password, and
  the status check that proves the
  server is alive before any radio is
  attached
- [**Replaying a capture**](replaying-a-capture.md) —
  the pcap-file data source: feed
  Kismet a capture file and watch it
  find the devices inside — the lab's
  core proof, and a safe way to learn
- [**Reading the results**](reading-the-results.md) —
  what a device record holds: types,
  names, channels, packet counts,
  first and last seen, and the SSIDs a
  client goes looking for
- [**Asking the API**](asking-the-api.md) —
  the REST API with curl: status,
  devices, data sources, and how
  scripts should log in
- [**Listening live**](listening-live.md) —
  real adapters, monitor mode, channel
  hopping, and your first live capture
  — documented-only in this guide, and
  labelled so
- [**The log and its tools**](the-log-and-its-tools.md) —
  the `.kismet` log: statistics, device
  dumps, and converting a run into
  other formats
- [**Configuration**](configuration.md) —
  the config file family, the site
  override that keeps your changes
  upgrade-proof, and the helper path
  that decides which tools Kismet may
  run
- [**Recipes**](recipes.md) — audit your
  own access points, see what your
  phone announces, spot a stranger
  using your network's name, and
  rehearse a survey on replayed files
  before doing one live
- [**Limits**](limits.md) — metadata,
  not contents: what passive listening
  cannot show you, and where this
  guide's own verification stops
- [**Troubleshooting**](troubleshooting.md) —
  the capture tool that is "not
  installed", the 401 that is correct,
  the empty device list, and the traps
  this guide's lab fell into
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Attacking networks. Kismet observes;
the tools that inject packets, break
handshakes or force devices off a
network are a different family, and
chapter 2 explains why they are out
of bounds here. Decrypting other
people's traffic is likewise out —
Kismet's view is the management
conversation around the data, not the
data. Bluetooth, Zigbee and the other
radios Kismet can hear with the right
capture hardware are pointed at, not
taught; this guide is about Wi-Fi.
Site surveys for hire, and anything
involving networks you do not own or
have permission to study, are not
recipes — they are the subject of
chapter 2.

## How to use this guide

Read chapter 1 for the model and
chapter 2 before powering anything
up. Chapter 3 names the parts, so
later surprises have names. Chapters
4 and 5 get you an installed server
with a login. Chapter 6 is the heart
of it: with nothing but a capture
file you can do everything the rest
of the guide teaches, in complete
safety, before any radio is involved.
Chapter 9 then moves the same skills
to live airwaves. The lab's
transcripts live in
`kismet-lab/transcripts/`; the script
that built the lab's capture file is
`kismet-lab/make_pcap.py`, and you can
feed its output to your own Kismet
exactly as the lab did.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Wireshark for Mere Mortals](https://paulsullivan33-dev.github.io/wireshark-for-mere-mortals/)
- [tcpdump for Mere Mortals](https://paulsullivan33-dev.github.io/tcpdump-for-mere-mortals/)
- [Nmap for Mere Mortals](https://paulsullivan33-dev.github.io/nmap-for-mere-mortals/)
- [Networking for Mere Mortals](https://paulsullivan33-dev.github.io/networking-for-mere-mortals/)
- [RTL-SDR for Mere Mortals](https://paulsullivan33-dev.github.io/rtl-sdr-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/kismet-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/kismet-for-mere-mortals/blob/main/LICENSE-CODE).
