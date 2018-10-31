NOTES
=====

Background:

- Domain Driven Design
- Hexagonal Design

Events can help here to communicate changes within the domain model.

"Event Driven" can be one of:

- event notification
- event carried state transfer
- event sourcing
- CQRS

=> See Martin Fowler's "event driven" blog post

General Programming Model: Method vs Event

Method calls ~ sending a message from the caller to the callee (sender -> receiver).
Events ~ receiver listens to the sender (`a.on('someEvent', b.someMethod)`).

Events are the same thing as Messages, only with the direction inverted. This
removes the direct coupling and allows multiple listeners vs a single callee.

This is obviously the Observer Pattern, other pattern is the Pub/Sub with an
Event BUS. Receivers listen to the Event BUS, senders send to the Event BUS.
This removes coupling for both the sender & the receiver.

Summary of Method:

- sender tells receiver
- usually sync
- fixed coupling
- new receiver: change to sender

Summary of Event:

- receiver listens to sender
- usually async
- loose coupling
- new receiver: no change to sender
- sometimes: hard to debug

Testing? Methods are tested with mocks, whereas Events are just send/received in tests.

Example: call center

Pair programming: funny Atlassian video
