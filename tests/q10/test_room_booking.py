import pytest

from refatoracao.q10.room_booking import BookingRequest, Room, RoomBooking, Schedule


def request(building, floor, room, start, end, projector, sound, attendees):
    return BookingRequest(
        Room(building, floor, room), Schedule(start, end), projector, sound, attendees
    )


def test_quote_examples():
    rb = RoomBooking()

    assert rb.quote(request("B", 1, "101", 8, 10, False, False, 10)) == pytest.approx(
        100.0, abs=0.001
    )
    assert rb.quote(request("A", 3, "101", 8, 10, True, True, 50)) == pytest.approx(
        (2 * 50.0 + 30 + 20) * 1.15 + 10, abs=0.01
    )
    assert rb.quote(request("B", 1, "LAB", 8, 10, False, False, 10)) == pytest.approx(
        (2 * 50.0) + 40, abs=0.01
    )


def test_refactor_goal_introduce_parameter_object():
    assert Schedule(8, 12).hours() == 4
    assert Room("A", 2, "101").surcharge() == 0.0
    assert Room("A", 3, "LAB").surcharge() == 50.0
    assert RoomBooking().quote(request("A", 1, "101", 8, 9, True, False, 41)) == pytest.approx(
        (50.0 + 30) * 1.15, abs=0.01
    )
