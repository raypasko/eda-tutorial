from bus import Bus
from call_center import CallAgency, LocalCallCenter

t = 0
def get_time():
    global t
    t += 1
    return t - 1

def test_basic_usage():
    global t; t = 0

    bus = Bus()
    agency = CallAgency(time_adaptor=get_time)

    bus.add_listener("call", agency.call)
    bus.emit(("call", "020/123456"))
    bus.emit(("call", "020/134256"))
    bus.emit(("call", "000/123456"))
 
    assert agency.number_of_calls == 3
    assert agency.call_logs == [
        (0, "020/123456"),
        (1, "020/134256"),
        (2, "200/123456"),
        ]

#def test_basic_usage():
#    global t; t = 0
#
#    agency = CallAgency([
#        LocalCallCenter("020"),
#        LocalCallCenter("200"),
#    ], time_adaptor=get_time)
#
#    agency.call("020/123456")
#    agency.call("020/134256")
#    agency.call("200/123456")
#
#    assert agency.number_of_calls == 3
#    assert agency.call_logs == [
#        (0, "020/123456"),
#        (1, "020/134256"),
#        (2, "200/123456"),
#        ]
#
#def test_area_code_redirection():
#    global t; t = 0
#
#    center1 = LocalCallCenter("1", time_adaptor=get_time)
#    center2 = LocalCallCenter("2", time_adaptor=get_time)
#
#    agency = CallAgency([center1, center2,], time_adaptor=get_time)
#
#    agency.call("1/123456")
#    agency.call("2/123456")
#
#    assert agency.call_logs == [
#            (0, "1/123456"),
#            (2, "2/123456"),
#            ]
#    assert agency.number_of_calls == 2
#
#    assert center1.call_logs == [(1, "1/123456")]
#    assert center1.number_of_calls == 1
#
#    assert center2.call_logs == [(3, "2/123456")]
#    assert center2.number_of_calls == 1
#
#def test_blacklist_logging():
#    global t; t = 0
#    return # TODO
#
#    center = CallCenter(["1/12345"], time_adaptor=get_time)
#    center.call("1/12345")
#    center.call("2/12345")
#
#    assert center.call_logs == []
