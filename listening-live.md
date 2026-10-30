# Listening Live

**Outcome: you know what a live
setup needs — an adapter that can
listen properly, a data source that
names it, and a first session on
your own network — and you know this
chapter's honesty status: the lab
had no adapter, so live capture is
taught here from the documentation,
not from transcripts.** Everything
before and after this chapter was
run; this one is labelled, per the
rules in `criteria.md`.

## The one hardware requirement that matters

Ordinary Wi-Fi adapters, doing their
ordinary job, show the system only
frames addressed to that machine.
Kismet needs the opposite: **monitor
mode**, a state in which the adapter
hands over *everything it hears* on
a channel and never transmits. Not
every adapter — and not every driver
— can do it. The Linux Wi-Fi stack
(mac80211) supports it for many
chipsets; the Kismet documentation
keeps the current word on which
chipsets behave, and "behaves under
Kismet" is the question to ask of
any adapter you are considering,
ahead of speed or price. USB
adapters with a long history in this
work are the usual choice, precisely
because their monitor mode is a
known quantity.

A second adapter is the comfortable
setup: leave your machine's built-in
Wi-Fi connected to your network for
ordinary use, and dedicate the USB
adapter to listening. The listener
is not *on* any network — that is
rather the point.

## Naming the source

A live source names the interface:

```bash
sudo kismet -c wlan1:name=usb-listener
```

Kismet starts `kismet_cap_linux_wifi`,
asks the system to put the interface
into monitor mode (creating a
monitor companion interface where
the driver wants one), and begins.
Two behaviours to expect, both from
the documentation:

- **Channel hopping.** One radio
  hears one channel at a time, so by
  default Kismet hops through the
  channel list, dwelling briefly on
  each — the census builds at the
  speed of the hop cycle. A source
  can instead be locked to a channel
  (`channel=` in the source options)
  when you are studying one network
  and want nothing missed.
- **Warnings about your network
  manager.** Desktop network managers
  and monitor mode disagree about
  who owns an adapter. Kismet's
  console names the conflict when it
  sees one; dedicating an adapter
  nobody else manages is the usual
  peace treaty.

## Your first live session, sized sanely

Per chapter 2, the subject is your
own network. A good first hour:

1. Start Kismet with the live source
   and open the web interface.
2. Watch your own access point
   appear, with the SSID and channel
   you set — compare with your
   router's settings page (that
   comparison is the live version of
   chapter 6's arithmetic).
3. Bring a phone near and watch a
   client appear, then walk it out
   of the room and watch `last_time`
   stop advancing. Presence, learned
   on yourself.
4. Stop the server (Ctrl-C in its
   console) and note the `.kismet`
   log the run left behind — chapter
   10 reads it.

Range is radio range: the same walls
that eat your Wi-Fi eat the census,
and a device heard at the edge is a
device half-heard. Kismet reports
signal strength live precisely so
you can learn your room's acoustics.

## The check (when you have the hardware)

Re-run chapter 6's audit against
reality: for your own access point,
name, channel, and type as shown by
Kismet should match your router's
own claims, and your phone's
comings and goings should match
your memory of your own movements.
When the census and the truth agree
on the networks you can check, you
may trust it — carefully, and per
chapter 2 — about the ones you
cannot.
