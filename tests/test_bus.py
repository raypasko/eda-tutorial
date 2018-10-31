from bus import Bus

def test_a_bus_can_emit_events():
    event = ("Something", {"some": "thing"})
    bus = Bus()
    bus.emit(event)

def test_a_receiver_gets_notified():
    events_received = []
    r1 = lambda event: events_received.append(event)
    bus = Bus()
    bus.add_listener("Something", r1)
    event = ("Something", {"some": "thing"})
    bus.emit(event)
    assert events_received == [event]


def test_multiple_receivers_get_notified():
    events_received = []
    r1 = lambda event: events_received.append(("r1", event))
    r2 = lambda event: events_received.append(("r2", event))
    bus = Bus()
    bus.add_listener("Something", r1)
    bus.add_listener("Something", r2)
    event = ("Something", {"some": "thing"})
    bus.emit(event)
    assert events_received == [("r1", event), ("r2", event)]


def test_events_accept_a_payload():
    pass


	

