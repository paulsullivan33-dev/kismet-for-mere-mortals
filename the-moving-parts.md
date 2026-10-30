# The Moving Parts

**Outcome: when something surprises
you later, you can name the part
responsible — server, data source,
interface, or log — instead of
blaming "Kismet" as a whole.**

Five parts do the work. Keep them
separate in your head and every
error message in this guide becomes
an address, not a fog.

## The server: `kismet`

One program is the brain. It takes
frames in, builds the device list,
answers questions, and writes the
log. When people say "run Kismet"
they mean this. It is a long-lived
server, not a command that finishes:
you start it, it listens until you
stop it, and everything else is a
way of talking to it.

## The ears: data sources

The server has no radio of its own.
Hearing is done by small separate
programs called **capture tools**,
one per kind of source, which the
server starts and supervises:

- `kismet_cap_linux_wifi` — real Wi-Fi
  adapters on Linux, the live ear of
  chapter 9.
- `kismet_cap_pcapfile` — a capture
  file played back as if it were an
  antenna. This is the ear the lab
  used, and the one chapter 6 teaches.
- Others for other radios — Bluetooth,
  Zigbee, RTL-SDR services, aircraft —
  each its own tool, all feeding the
  same server.

A configured ear is a **data source**,
named by a string like:

```text
-c /path/to/lab-capture.pcap:type=pcapfile
```

The part before the colon says
*what* to listen to; the `type=` says
*which tool* understands it. When a
source fails, it is almost always
this seam — the wrong tool, a tool
the server is not allowed to run
(chapter 11's helper path), or a
thing that is not there.

## The face and the API

The server offers the same knowledge
two ways. The **web interface** on
port 2501 is the face: pages of
devices, maps, graphs, settings. The
**REST API** underneath it is the
same facts as data — chapter 8 pulls
the device list with `curl` and gets
exactly what the web page shows,
because the web page got it there
too. Anything you can see, a script
can ask for; that is a design
decision, and chapter 8 leans on it.

Both sit behind a login. The server
keeps its credentials in your own
config directory (`~/.kismet/`), and
an unauthenticated request gets a
firm `401 Permission denied` — the
lab verified that refusal before it
verified anything else.

## The memory: the `.kismet` log

Every run writes a log file named
for its start, like
`Kismet-20261030-04-17-17-1.kismet`.
It is a SQLite database holding the
devices, the packets, the sources
and the alerts of the run. The
server writes it as it goes, and a
family of **`kismetdb_` tools** reads
it afterwards — statistics, device
dumps, conversions to other formats
(chapter 10). The log is the run's
record: delete the server, the log
still testifies.

## The configuration

Behaviour lives in a family of files
in `/etc/kismet/`: the master
`kismet.conf`, which includes
companions for the web server
(`kismet_httpd.conf`), for 802.11
(`kismet_80211.conf`), for logging,
alerts, and more. Your own changes
belong in the override file
`kismet_site.conf`, which is loaded
last and wins — chapter 11 explains
why that one habit keeps upgrades
painless. One setting from that
family runs the whole show more than
any other: `helper_binary_path`, the
list of directories the server will
run capture tools from. It is a
security fence, and the lab hit it
head-on (transcripts t00, chapter
13).

## The check

Watch a start-up once with these
five names in mind. The console
shows them in order: config files
included, web server started,
manufacturer database loaded, data
source launched. The lab's start
(transcript t02) reads like a roll
call of the parts above — if one is
missing from yours, you have found
your problem's address.
