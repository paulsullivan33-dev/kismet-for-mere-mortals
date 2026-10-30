# Limits

**Outcome: you can state what
Kismet cannot show you — and what
this guide itself could not
prove — before either costs you.**

## Metadata, not contents

Kismet's world is the management
conversation: names, addresses,
channels, counts, times. It is not
the *contents* of anyone's traffic.
Modern Wi-Fi encrypts the data
payloads of joined networks, and
even on an open network this
guide's path — census first, packets
only as your own files — stops at
the introductions. If what you need
is the data, you need a different
situation (and, for anyone else's
data, a different chapter 2
answer). Expect to know that a
device exists and how it behaves,
not what it says.

## Only what is broadcast

Nobody is obliged to talk. A client
that never probes, on a network
nobody is using, in range only
briefly, may leave almost no trace;
a quiet network heard from behind
two walls is a rumour with a MAC
address. The census is a sample of
what the air volunteered, not an
inventory of everything switched
on — and a device can be absent
from the list for no deeper reason
than that it had nothing to say
while you were hopping channels.

## One channel at a time

A single radio samples the band in
turns (chapter 9's hopping). Brief
events fall between dwells. Locked
on one channel, you see that
channel completely and the rest not
at all. More adapters widen the
net; nothing widens it to
everything.

## Identity is softer than it looks

A MAC address looks like a serial
number and behaves like a nickname.
Phones rotate randomised addresses
by design; access points can run
several names on one radio, or be
several radios under one name.
Kismet reports addresses and names
faithfully — what *thing* they add
up to is your inference, and it
should stay humble, especially
about other people's devices
(chapter 2).

## Range is the room you are in

Walls, distance, and a noisy band
all edit the census before Kismet
sees it. Two listeners in two rooms
produce two different truths, both
honest. Signal strength is a clue
about nearness, not a measurement
of it.

## This guide's own limit

Stated once, plainly: the lab
verified the server, the web
interface, the API, the config
system, and the log tools against a
replayed capture file, on a machine
with no wireless hardware. Live
capture — adapter choice, monitor
mode, the hopping reality — is
taught from the documentation, and
the lab never heard a real frame.
The frame-processing heart those
live skills depend on is the same
heart the replay exercised; the
radio edge of it is yours to verify
with chapter 9's check, on your own
network, the day an adapter is in
your hand.
