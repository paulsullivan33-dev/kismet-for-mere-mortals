# Asking the API

**Outcome: your scripts can pull the
same facts the web page shows —
status, devices, data sources — and
log in the way Kismet expects.**

## Everything is an endpoint

The web interface is a client of the
API, not a separate brain. Each fact
has an address, and adding `.json`
to it asks for data instead of a
page. The three endpoints this guide
uses were all run live in the lab
(transcript t03):

```text
/system/status.json            the server's account of itself
/devices/last-time/1/devices.json   every device heard since a time
/datasource/all_sources.json   the data sources and their health
```

The lab's answers: status reported
version `2026.10.R1-9ea2ca0e9` and
`devices.count: 3`; the device list
named CafeWiFi, LibraryNet and the
client with their packet counts; the
source list reported the pcapfile
source, `packets: 15`, still marked
running. `/devices/views/all/devices.json`
returns the same census through the
view system the web UI uses.

## Logging in, two ways

**Basic auth for scripts.** The
simplest honest route: send the
login you created in chapter 5 with
each request.

```bash
curl -u yourname:yourpassword \
  http://127.0.0.1:2501/devices/last-time/1/devices.json
```

Keep the password out of your
scripts and shell history the way
you would any secret — read it from
a file or the environment, and
remember the connection is plain
HTTP on your own machine unless you
configure more (chapter 11). Without
any login, the answer is the `401`
of chapter 5, and that refusal is
part of the design, not a fault to
work around.

**Sessions for browsers.** The web
interface logs in through
`/session/login` and carries a
session cookie; scripts do not need
this unless they are impersonating a
browser, which they should not.

There is also an API-key mechanism
(`/auth/apikey/...`) for giving a
program its own revocable credential
instead of your password — the
grown-up choice for anything you
leave running. The lab noted the
endpoints; it did not need them, and
neither will a first script.

## Asking narrower questions

The full device list is the fire
hose; the API has taps:

- **Time windows.** `last-time/<ts>`
  asks for devices heard after a
  Unix timestamp — poll it with your
  last poll's time and you have a
  change feed.
- **By address.** `/devices/by-mac/<mac>/devices.json`
  follows one device; the lab's
  client is `02:AA:BB:CC:DD:01` in
  its story and will be some phone of
  yours in yours.
- **Fields.** Requests can carry a
  field selection (a JSON body
  naming the dotted fields you want),
  so a script that only needs names
  and counts need not haul the whole
  dossier. The dotted names of
  chapter 7 are the vocabulary.

## The check

Reproduce chapter 6's proof from
the command line alone: status
count 3, three devices with the
right names, source at 15 packets.
If a script of yours prints those
three facts and compares them to
what the file contained, it is doing
real verification — the same habit
this guide's lab used to trust its
own results. From here, automation
is ordinary programming, and the
air is just another input.
