# Installing Kismet

**Outcome: a `kismet` program that
runs on your machine and can state
its version — before any radio,
login, or capture enters the
picture.**

## Where Kismet comes from

Kismet is not in Ubuntu 24.04's own
repositories — the lab checked, and
`apt-cache policy kismet` comes back
empty. The project publishes its own
packages, kept current, from its own
repository at `kismetwireless.net`,
with a set of packages per
distribution. That split is the
first thing to understand about the
install: **`kismet` is a family.**

- `kismet-core` — the server itself,
  the web interface, the config
  files, the manufacturer database.
- `kismet-capture-linux-wifi` — the
  capture tools for Wi-Fi, including
  the live adapter tool and the
  capture-file tool this guide leans
  on.
- `kismet-logtools` — the `kismetdb_`
  family of chapter 10.
- More capture packages for other
  radios, and data packages (the lab
  skipped `kismet-adsb-icao-data`,
  the aircraft lookup table, and its
  absence showed up later as one
  honest, harmless error line —
  chapter 14 tells the story).

Installing the top-level `kismet`
package from the project's
repository pulls in the whole
family; installing the pieces above
by name gets you everything this
guide uses. The project's site
carries the current instructions for
adding its repository to your
distribution — follow those, since
signing keys and release names are
theirs to change.

## What the lab did, exactly

This guide's lab machine had its
package manager locked by other
work, so the lab did the same
install by hand, and says so
(transcript t00 keeps the receipts):
it downloaded the `.deb` files for
release **2026.10.R1** — the same
files an `apt install` would have
fetched from the project's noble
repository — plus the two system
libraries the machine lacked, and
unpacked them into a folder. Same
bytes, same versions, same programs;
only the plumbing differed. On an
ordinary machine you will use the
package manager and never think
about any of this. The lab's two
extraction quirks — a config path
that expected `/etc/kismet`, and the
capture tools' helper path — are
artefacts of unpacking by hand, and
they make a guest appearance in
chapter 14 because the underlying
rules protect real installs too.

## The check

However it arrived, the acceptance
test is one line:

```bash
kismet --version
```

```text
Kismet 2026.10.R1-9ea2ca0e9
```

That is the version this guide's lab
ran throughout. Kismet releases are
named for year and month; yours may
be newer, which is fine — everything
here is behaviour, not trivia, and
behaviour changes slowly. If the
command is not found, the install
did not finish; if it prints a
version, chapter 5 can start the
server. Note that `kismet_server`
still exists as a name on the
system, but it is a signpost, not a
program — modern Kismet is started
with `kismet` alone, and the old
name will tell you so if you call
it.
