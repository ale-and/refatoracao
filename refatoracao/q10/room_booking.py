from dataclasses import dataclass


@dataclass(frozen=True)
class Room:
    building: str
    floor: int
    name: str

    def surcharge(self) -> float:
        extra = 0.0
        if self.building == "A" and self.floor >= 3:
            extra += 10.0
        if self.name == "LAB":
            extra += 40.0
        return extra


@dataclass(frozen=True)
class Schedule:
    start_hour: int
    end_hour: int

    def hours(self) -> int:
        return self.end_hour - self.start_hour


@dataclass(frozen=True)
class BookingRequest:
    room: Room
    schedule: Schedule
    projector: bool
    sound: bool
    attendees: int


class RoomBooking:

    def quote(self, request: BookingRequest) -> float:
        base = request.schedule.hours() * 50.0
        if request.projector:
            base += 30.0
        if request.sound:
            base += 20.0
        if request.attendees > 40:
            base *= 1.15

        base += request.room.surcharge()

        return round(base, 2)
