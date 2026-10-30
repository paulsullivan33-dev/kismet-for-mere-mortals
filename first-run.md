# First Run — the Server and the Login

**Outcome: Kismet running, a login
that works, and a status answer that
proves the server is alive — all
before any listening happens.**

## Start it with nothing to hear

Kismet does not need a data source to
be worth starting. Run it plainly:

```bash
sudo kismet
```

(Real capture work needs the
privileges; the server will say so
if they are missing.) The console
tells the start-up story — config
files included one by one, a server
identity generated and stored in
`~/.kismet/`, the manufacturer
database loaded (40,657 records in
the lab's run — that is the list
that turns a maker's address prefix
into a maker's name), and:

```text
INFO: Starting Beast webserver on 0.0.0.0:2501
```

From here the server is a web site
that happens to be a wireless
monitor. Leave it running; the rest
of this chapter talks to it.

## The first-run password

Point a browser at
`http://localhost:2501` on the same
machine. The first visit asks you to
create the login — a username and
password of your choosing, stored
hashed in `~/.kismet/kismet_httpd.conf`.
This is not decoration. The API can
reconfigure sources and read
everything the server knows, so
Kismet refuses to serve any of it
until someone owns it. The lab's
first API call, made before its
login existed and repeated after
without one, got the refusal in
full:

```text
401 Permission denied
This resource requires a login or session token.
```

Treat a 401 like a locked door that
proves the locks work. (The lab
itself set its throwaway login in
the site config file, a documented
alternative chapter 11 mentions;
the browser setup is the route to
learn, because it is the one you
will meet on a fresh machine.)

## The check: ask the server about itself

With the login, the status endpoint
gives the server's own account of
itself — and this exact exchange,
with the lab's login, is transcript
t03:

```bash
curl -u yourname:yourpassword http://127.0.0.1:2501/system/status.json
```

```json
{"kismet.system.version": "2026.10.R1-9ea2ca0e9",
 "kismet.system.devices.count": 0,
 "kismet.system.memory.rss": 29224, ...}
```

Version, memory, and a device count
of zero — zero because nothing has
been heard yet, and a beautifully
checkable fact: any number other
than zero at this point means a
source is already feeding it. The
web interface at the same address
shows the same emptiness as a page
of quiet graphs and an empty device
list. That emptiness is the correct
starting picture. Chapter 6 fills it
without touching a radio; chapter 9
fills it with the real air.
