# What Kismet Is

**Outcome: you can say what Kismet
collects, where it gets it, and the
one thing it never does — transmit.**
Everything else in this guide is
detail hung on that frame.

## The conversation you cannot hear

A Wi-Fi access point — the box your
router gives you, or the one in a
café — spends its life announcing
itself. About ten times a second it
sends a short radio frame called a
**beacon**, saying in effect: *my name
is CafeWiFi, my address is this, I am
on channel 6, I can talk at these
speeds.* Anyone in range can hear
that. It is meant to be heard; that is
how your laptop finds the network
before you ever type a password.

Your phone plays the other half. When
it is looking for a network, it calls
out with **probe requests**: *is
HomeNet-Example there? is
Airport-Lounge there?* — naming
networks it has joined before, so a
friendly access point can answer. An
access point that hears its name
answers with a **probe response**.

None of this is encrypted. Passwords
protect the *data* a network carries
after you join; the introductions
happen in the clear, because they
have to. Kismet exists to collect the
introductions.

## What Kismet does with them

Kismet is a **passive wireless
monitor**. A Wi-Fi adapter in a
special state called **monitor mode**
hands Kismet every frame it hears,
not just the ones addressed to it.
Kismet's server takes those frames
apart and builds a living list of
**devices**: access points, clients
(phones, laptops, gadgets), and the
relationships between them — which
client is talking to which access
point, which names each client goes
looking for, how strong the signal
is, and when each device was first
and last heard.

The result is a map of the wireless
neighbourhood, drawn from what the
neighbourhood itself broadcasts. In
this guide's lab, Kismet was fed a
capture file containing two invented
access points and one invented
client, and its list said exactly
that:

```text
02:AA:BB:CC:DD:01 | Wi-Fi Client |            | packets: 3
02:11:22:33:44:02 | Wi-Fi AP     | LibraryNet | packets: 6
02:11:22:33:44:01 | Wi-Fi AP     | CafeWiFi   | packets: 7
```

That is the whole product in three
lines: who is out there, what kind of
thing they are, what they call
themselves, and how much they have
said.

## The one thing it never does

Kismet does not transmit. It does not
join networks, does not send probes
of its own, does not knock devices
off the air. Listening is all it
does, and that passivity is both its
safety and its limit: it can only
report what others chose to say out
loud, and it cannot ask questions.
Chapter 13 lists what that leaves out
of reach.

## The check

Pick any answer Kismet gives and ask
*which broadcast said that?* A
network's name and channel came from
its beacons. A client's shopping list
of remembered networks came from its
probe requests. If you can trace a
fact on the screen back to a frame
someone else sent, you understand the
tool. If a screen ever seems to know
something nobody broadcast, you have
found either an inference Kismet is
making from several frames (it does
some, and says so) or a
misunderstanding worth chasing.

## Where Kismet sits

Kismet has been listening since 2001,
which makes it an elder of wireless
security. It runs on Linux (and other
systems), drives a long list of
capture hardware beyond Wi-Fi —
Bluetooth, Zigbee, aircraft
transponders, weather sensors — and
is driven in return through a web
interface and a full programming
interface, both covered later. It is
written by the Kismet Wireless
project and installed from the
project's own packages (chapter 4).

Its neighbours are close but
different. A packet capture tool like
Wireshark shows you frames; Kismet
turns frames into a census. A network
scanner like Nmap knocks on doors
over a wire; Kismet never knocks at
all. The next chapter is the one the
law cares about: what you may do
with a census of other people's
radios.
