# Configuration

**Outcome: your changes survive
upgrades, your server is yours, and
the one setting that guards the
capture tools is a name you know.**

## The family of files

Kismet's behaviour lives in
`/etc/kismet/`. The master file,
`kismet.conf`, does little itself
except include the others — the
lab's start-up log shows the parade
(transcript t02):

```text
INFO: Including sub-config file: /etc/kismet/kismet_httpd.conf
INFO: Including sub-config file: /etc/kismet/kismet_memory.conf
INFO: Including sub-config file: /etc/kismet/kismet_alerts.conf
INFO: Including sub-config file: /etc/kismet/kismet_80211.conf
INFO: Including sub-config file: /etc/kismet/kismet_logging.conf
INFO: Including sub-config file: /etc/kismet/kismet_filter.conf
```

Each companion owns a subject: the
web server, memory limits, alerts,
the 802.11 decoder, logging,
filtering — plus per-radio files for
the other capture families. Inside,
values are `name=value` lines, and
the files are heavily commented;
they are meant to be read. Paths in
them use expansions you will meet in
the wild: `%h` is your home
directory (your personal config and
log identity live in `%h/.kismet/`),
`%E` the config directory itself.

## The override habit

Do not edit the shipped files. The
last word in every start-up belongs
to **`kismet_site.conf`** in the
same directory (and any files in
`kismet_site.d/`): loaded after
everything, its values win. Put
every change you make there, one
setting per line, and a package
upgrade can replace the whole family
without touching a single decision
of yours. The lab's own site file,
by the end of its work, held three
lines and each earned its place —
your real one will grow the same
way, a line per lesson.

## The guard: `helper_binary_path`

```text
helper_binary_path=/usr/bin
```

(the default is written `%B`, the
install's bin directory). This is
the list of directories from which
Kismet will run helper and capture
tools — a deliberate fence, so that
a data source string can never talk
the server into executing some stray
program that happens to share a
name. It is also the setting behind
the lab's loudest failure: with its
unpacked-by-hand install, every
source died with `Capture tool not
installed` until the site file added
the lab's bin directory (t00). On a
package install the default is
already right, and you should leave
it so — knowing the fence exists is
the lesson, not moving it.

## The login, as configuration

Chapter 5's browser setup stores
your login in `~/.kismet/`. The
config-file alternative, which the
lab used because a sandbox has no
comfortable browser: `httpd_username`
and `httpd_password` set in
`kismet_site.conf` define the login
in the clear, and the server treats
a login defined in the global config
as the owner — any login in the
user file is then ignored. That is
documented behaviour and genuinely
useful for a headless box you manage
by files. It also means the site
file becomes a secret: permissions
tight, and a throwaway password in
any example — including every
example in this guide.

While in `kismet_httpd.conf`
territory: the web server listens
on port **2501** by default and on
all interfaces. On a machine that
faces other people, binding it to
localhost (`httpd_bind_address`) or
putting it behind your own
arrangements is the difference
between a tool and an invitation.

## Defining sources ahead of time

Command-line `-c` strings are for
the session in front of you.
Sources you always want — a
dedicated adapter, a standing file
replay, a remote sensor — can be
written as `source=` lines in the
site file and they will be opened
at every start; the server says so
on the console (and notes when
command-line sources override the
file's for a run). Name each one
(`name=`) the way you will want to
see it in the source list.

## The check

Restart Kismet and read the roll
call with new eyes: overrides
counted, sub-configs included, your
site file honoured last. Then change
one harmless thing in
`kismet_site.conf` — the server name
in the status response, say — and
watch it take effect while the
shipped files stay untouched. That
small loop is the whole chapter.
