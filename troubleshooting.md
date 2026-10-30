# Troubleshooting

**Outcome: the failures this guide
met — and the ones waiting for you —
each with its cause and its
tell-tale.**

## "Capture tool not installed"

```text
ERROR: Data source '...:type=pcapfile' failed to launch:
Capture tool not installed
```

The capture program exists but the
server will not run it — or Kismet
cannot find it where it is allowed
to look. Recall chapter 11's guard:
Kismet runs helpers only from
`helper_binary_path`. Causes, in the
order the lab met them: the tool's
package is not installed at all
(`kismet-capture-linux-wifi` carries
the Wi-Fi tools), or — the strange
installs — the tools live somewhere
the fence does not cover. Fix the
package first; touch the fence only
if you can say why.

## The 401 that will not let you in

You are being refused because there
is genuinely no login the server
recognises yet. On a first run, do
the chapter 5 browser setup before
testing the API — the API has no
guest door by design. If a login
existed and stopped working, ask
whether a `kismet_site.conf`
`httpd_username` / `httpd_password`
pair has taken over: a login defined
in the global config replaces the
user-file login entirely, by design
(chapter 11). And if curl works in
your browser's shadow but not in a
script, check the obvious: the API
answers on the same port 2501 the
UI uses.

## "End of pcapfile reached" — and then nothing happens

Nothing *should* happen; the file
is finished and the devices remain
in the list (chapter 6). If the
device list is genuinely empty, the
file had nothing the decoder wanted:
check it outside Kismet first —
`tcpdump -r file.pcap` should show
802.11 frames with a radiotap (or
compatible) header. A pcap of wired
Ethernet traffic is a fine capture
of the wrong medium, and Kismet
will faithfully find no wireless
devices in it.

## An error about a database you never asked for

```text
ERROR: Could not open ICAO database .../kismet_adsb_icao.txt.gz,
ADSB ICAO lookup will not be available.
```

Not every ERROR is yours. Kismet
starts handlers for every radio
family and complains, accurately,
about each missing optional piece.
This one wants the
`kismet-adsb-icao-data` package —
aircraft lookups, irrelevant unless
you are chasing planes. Read errors
for whose world they belong to
before fixing them.

## The server starts, the source starts, and no devices appear

Work the seam (chapter 3) in order:
the source's own line in the console
(it will say when it is re-opening
after an error, and why); the source
list in the API (a source at zero
packets is an ear hearing silence —
wrong channel, dead adapter, or a
file that ended); then the input
itself. For live work on Linux,
 permissions are the usual culprit —
capture needs privileges, which is
why this guide starts Kismet with
`sudo`.

## The old name answers instead of the program

`kismet_server` on a modern system
is a notice, not a binary: it tells
you the program is called `kismet`
now and exits. Anything in your
notes or scripts from before that
change will point at it — update
the name and move on (chapter 4).

## The lab's own confession

The lab's strangest failure was
none of Kismet's: an extracted, run
-from-a-folder install whose server
died with a missing shared library
when launched one way and ran
happily when launched another —
an environment variable that did
not survive the journey through a
wrapper. The lesson survives the
details: when a program claims a
file is missing, ask *missing from
whose view* before concluding it is
missing at all.
