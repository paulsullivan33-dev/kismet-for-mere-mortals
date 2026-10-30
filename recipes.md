# Recipes

**Outcome: four jobs you can do
with Kismet, sized for your own
networks, using only the skills the
earlier chapters built.** Every
recipe ends with the check that
says it worked.

## 1. Audit your own access points

The question: does your Wi-Fi
announce what you think it does?

- Start a replay or live session
  (chapters 6 and 9).
- List the devices of type Wi-Fi AP
  whose SSID you recognise.
- For each: channel against your
  router's setting, and the maker
  name against the box on your
  shelf. A mismatch is a changed
  setting, a misremembered box, or a
  stranger — in that order, until
  the evidence says otherwise.

*Check:* the AP record's channel and
SSID equal the router's own settings
page. They did for the lab's
CafeWiFi (channel 6) and LibraryNet
(channel 1), because those were the
frames written.

## 2. See what your phone announces

The question: what does your own
device volunteer?

- On a test capture or a live
  session with your own phone,
  find its client record and read
  its probed SSIDs.
- Expect some, or none: modern
  phones randomise their address
  and often probe only when they
  must, which is privacy working.

*Check:* the list contains only
networks you recognise, and every
entry is a name you once joined.
That is both the answer and the
lesson of chapter 2.

## 3. Spot a stranger wearing your network's name

The question: is anything pretending
to be your access point?

- Watch your SSID's AP records.
  A legitimate home has one (or a
  small known number, if you run
  several radios on one name).
- A second record with your SSID
  but a different hardware address
  and a strange channel is the
  beginning of a question, not the
  end of one: check your own
  equipment first (a repeater, a
  neighbour's borrowed name, a
  gadget's default). If none explains
  it, the next step is the router
  owner — you — and then, if you
  have reason to believe someone is
  deliberately impersonating, the
  usual reporting channels for your
  area. Kismet's job here is
  noticing; judging belongs to
  people.

*Check:* every AP record claiming
your SSID traces to a box you own.

## 4. Rehearse a survey on a file before doing one live

The question: how do I practice
without stakes?

- Take a capture — from Kismet's
  own log conversion (chapter 10),
  from a previous session, or from
  `kismet-lab/make_pcap.py` — and
  answer a question with the API
  before the web UI: count devices,
  list access points, name the
  loudest source.
- Automate the answer in a small
  script, and check it against the
  file's own story (chapter 6's
  arithmetic is the template).
- Only then run the same script
  against a live session of your
  own network.

*Check:* the script's answers match
the file's known contents exactly.
A tool trusted on a file earns its
place on the air.
