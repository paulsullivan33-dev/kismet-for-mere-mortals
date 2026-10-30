# Reading the Results

**Outcome: you can read a device
record the way Kismet built it —
field by field back to the frames
that earned each one.**

## A device is a dossier, not a row

Every device in Kismet's list is a
record that grows as frames arrive.
The web interface shows the friendly
surface; the record underneath is
what the API returns (chapter 8),
and its fields follow one naming
idea: `kismet.device.base.*` for what
is true of everything, and a block
per radio family — `dot11.device.*`
for Wi-Fi — for the particulars.

## The base fields

- **`kismet.device.base.macaddr`** —
  the device's hardware address, its
  identity in the census. The first
  bytes are the maker's prefix, which
  is how Kismet names manufacturers;
  the lab's `02:` addresses are
  locally administered, so no maker
  claims them — exactly what you want
  from invented devices.
- **`kismet.device.base.type`** —
  Kismet's verdict on the role:
  *Wi-Fi AP*, *Wi-Fi Client*, and
  others as evidence accumulates. The
  types are earned, not declared —
  an access point is one because it
  beacons like one.
- **`kismet.device.base.name`** — for
  an access point, the network name
  it advertises (its **SSID**). For a
  client, usually blank until some
  frame gives it something to be
  called.
- **`kismet.device.base.packets.total`** —
  every frame Kismet has credited to
  this device, as sender or as a
  party. Chapter 6's arithmetic —
  6, 7, 3 — lives here.
- **`first_time` / `last_time`** —
  when the device entered the census
  and when it was last heard.
  Together they are a presence log:
  *this phone was in range between
  these hours* is a first-time /
  last-time sentence, and chapter 2's
  rules are about exactly sentences
  like that.
- **`kismet.device.base.channel`** —
  the channel the device was heard
  on.

## The Wi-Fi particulars

Inside `dot11.device`, the details
that make wireless sense:

- **`dot11.device.advertised_ssid_map`** —
  the names an access point has
  announced, with the fine print of
  each announcement. The lab's record
  for LibraryNet holds exactly one
  entry: its own name.
  An access point advertising *many*
  names is usually several virtual
  networks on one radio.
- **`dot11.device.num_probed_ssids`** —
  for a client, how many distinct
  networks it has called out for.
  The probe list is the most
  personal data in the census: it is
  the device's memory of where it
  has been. Kismet shows it because
  it is diagnostic gold on your own
  devices — and chapter 2 explains
  why it deserves care on anyone
  else's.
- **`num_associated_clients`,
  `num_client_aps`** — the
  relationship counts: how many
  clients an access point serves,
  how many access points a client
  has been seen with. The map of who
  talks to whom is drawn from these.
- **Signal fields** — how loud each
  device was heard, strongest and
  most recent. In the lab's file
  there are none (a hand-built frame
  carries no honest signal reading,
  and the generator did not fake
  one); live captures are rich with
  them, and they are how *near* and
  *far* enter the story.

## The check

Take one device and tell its story
without the screen. For the lab's
client: *a device with a made-up
address appeared, asked twice for
networks by name — once for CafeWiFi
by name, once for anyone at all —
and got an answer from CafeWiFi.*
Three packets, one small biography,
every clause traceable to a frame.
When you can narrate a record that
way, you are no longer reading
Kismet's output — you are reading
the air, with Kismet as the
translator. That is the skill the
rest of the guide spends.
