# The Log and Its Tools

**Outcome: a finished run is not
gone — you can reopen its log and
make it answer questions, produce
receipts, and turn into other
formats.**

## The log is a database

Each run leaves a file like
`Kismet-20261030-04-17-17-1.kismet`
in the directory Kismet was started
from. It is a SQLite database
(KismetDB version 11 in the lab's
run), written as the run happens:
devices, packets, data sources,
alerts. Stop the server mid-thought
and the log still holds everything
up to the interruption — one reason
surveys survive laptop lids.

## Statistics first

The fastest way back into a run is
its summary. This is the lab's real
output for the replayed capture
(transcript t04):

```bash
kismetdb_statistics --in Kismet-20261030-04-17-17-1.kismet
```

```text
Packets: 15
Devices: 3
1 datasources
  .../lab-capture.pcap  ... pcapfile
    Packets: 15

Packet tags found in log:
  DOT11_BEACON_SSID DOT11_PROBE_REQ DOT11_RESPONSE_SSID
```

Notice the tags: the log records not
just counts but *kinds* — beacons
seen, probes seen, responses seen.
A statistics page for a live run
tells the shape of an afternoon at a
glance: how many devices, from how
many sources, over what span,
whether location data rode along
(none here, honestly reported).

## The devices, back out

```bash
kismetdb_dump_devices --in <run>.kismet --out devices.json
```

writes the census as JSON — the same
three devices, the same names, from
the log alone (t04). This is the
bridge from listening to everything
else you might do with data: diff
two evenings, feed a spreadsheet,
check a suspicion. What you *should*
do with a device list that includes
other people's radios is chapter 2's
subject, and it applies to files
exactly as it applies to screens.

## The converter family

The install ships a shelf of
`kismetdb_` tools (the lab's
directory listing is in t04). The
ones a first year meets:

- **`kismetdb_to_pcap`** — write the
  run's packets back out as a pcap.
  Feed that pcap to chapter 6's
  replay, or to Wireshark, and the
  circle closes: logs become
  captures become logs.
- **`kismetdb_to_wiglecsv`** — export
  access points in the format the
  WiGLE wireless-mapping project
  uses, for those who contribute
  beacon-level sightings there.
- **`kismetdb_to_kml` /
  `kismetdb_to_gpx`** — map formats,
  for runs that carried GPS.
- **`kismetdb_clean` and
  `kismetdb_strip_packets`** — tend
  and slim a log: strip the packet
  payloads and keep the census, the
  polite form for a log you keep.

(The lab ran statistics and the
device dump for real; the converters
are named from the shipped package
and their one-line purposes, per
`criteria.md`.)

## The check

Close the loop on the lab's numbers
one final way: statistics say 15
packets and 3 devices; the dump
names the same three; the API said
the same while the run was live.
Three doors into one room. A run
whose log disagrees with its live
face is a run whose story is not
finished — and now you own three
ways to notice.
