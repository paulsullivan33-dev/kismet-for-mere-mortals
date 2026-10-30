# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's networks and devices are invented, and use
   locally-administered addresses no real maker owns.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 13 names what the tool
   cannot do: a census of what was broadcast, not the contents
   of traffic; devices that stay silent stay invisible; one
   channel at a time; identity softer than addresses suggest.
8. **The ethics rule is in the text, early.** A listening tool
   hears other people's devices, so chapter 2 — before any
   procedure — draws the line in plain terms: your own networks
   are the classroom, beacons are public speech, other people's
   traffic and networks are off limits, interfering is worst of
   all. The recipes are all built on the reader's own airwaves.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is an Ubuntu 24.04 sandbox with **no wireless
hardware**: no adapter, no `/sys/class/net/*/wireless`, no
monitor mode (transcript t05 keeps the evidence). Everything
verifiable without a radio was verified; the radio edge is
documented-only and labelled.

Kismet **2026.10.R1** (server version string
`2026.10.R1-9ea2ca0e9`) was obtained from the project's official
apt repository for Ubuntu noble — the packages `kismet-core`,
`kismet-capture-linux-wifi` and `kismet-logtools`, plus the two
system libraries they needed. The sandbox's package manager was
locked by other work, so the `.deb` files were extracted and run
from a folder with `LD_LIBRARY_PATH` (transcript t00); the
programs, versions and behaviour are the packaged ones, only
the plumbing differed. Two extraction consequences were needed
and are disclosed in t00: the extracted config tree was linked
at `/etc/kismet` because Kismet expands `%E` to its compiled
config path, and the lab's bin directory was added to
`helper_binary_path` through the standard override file
`kismet_site.conf`. The lab's web login was also set through
that site file (a documented route) because the sandbox has no
comfortable browser; the password used was a throwaway and is
not a credential for anything.

The lab's airwaves were synthetic and are labelled as such
everywhere: `kismet-lab/make_pcap.py` writes 15 hand-built
802.11 frames (radiotap headers; beacons from two invented
access points, CafeWiFi and LibraryNet; probe requests from one
invented client; one probe response; arbitrary 2026-01-01
timestamps). tcpdump decoded the file as valid 802.11 before
Kismet ever saw it (t01).

Run for real, with transcripts as evidence:

- Installation facts: the project's noble repository contents
  (Kismet is absent from Ubuntu 24.04's own repos), the package
  split, the two missing libraries, the dpkg lock refusal, the
  extraction, and `kismet --version` (t00). The old
  `kismet_server` name's signpost behaviour was also observed.
- The hand-built capture and its independent decode by
  tcpdump, frame types and channel included (t01).
- Server start from the extracted tree: the full sub-config
  parade, the web server on port 2501, the 40,657-record
  manufacturer database, the server UUID file under the user's
  `~/.kismet`, PHY handler registration (t02).
- The pcapfile data source replaying the file: launch success,
  all 15 frames processed, the "end of pcapfile reached"
  completion line (t02). Without the helper-path override, the
  same start failed with "Capture tool not installed" — kept
  as chapter 14's main exhibit.
- The REST API on loopback: a 401 refusal without a login, then
  with the lab login — `/system/status.json` reporting exactly
  3 devices, `/devices/last-time/1/devices.json` naming the two
  access points and the client with packet counts 7 / 6 / 3
  that reconcile frame-by-frame with the generated file,
  `/devices/views/all/devices.json`, `/datasource/all_sources.json`
  reporting the pcapfile source at 15 packets, and the web UI
  root page answering with `<title>Kismet</title>` (t03).
- The log tools against the run's own `.kismet` log:
  `kismetdb_statistics` (15 packets, 3 devices, the packet
  tags) and `kismetdb_dump_devices` reproducing the same census
  from the log alone (t04).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- The normal `apt install` route end to end (the files were the
  repository's own; only the installer's run is untested), and
  the browser first-run password wizard of chapter 5 (the lab
  set its login in the site config instead).
- **All live capture** (chapter 9 entire): adapter and chipset
  choice, monitor mode, `kismet_cap_linux_wifi` against real
  hardware, channel hopping behaviour, signal values in device
  records, network-manager conflicts, and the capture
  permission behaviour on a stock install.
- Web interface interaction beyond the root page answering:
  clicking through device details, graphs and settings.
- The API-key endpoints (`/auth/apikey/...`) — noted from the
  server, not exercised.
- The `kismetdb_` converters other than statistics and the
  device dump — named from the shipped package's contents.
- Capture families beyond Wi-Fi (Bluetooth, Zigbee, ADS-B and
  the rest), GPS-fed runs, and remote capture sources.

Fixtures are this guide's own and deliberately generic: two
stock SSIDs (CafeWiFi, LibraryNet), locally-administered
`02:` addresses, and an arbitrary date. No real network, person
or place appears anywhere in the lab.
