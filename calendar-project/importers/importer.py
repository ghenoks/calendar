from ics import Calendar as ICSCalendar
from models.event import Event

class CalendarImporter:
    def load(self, filepath: str):
        with open(filepath, 'r') as f:
            ics_cal = ICSCalendar(f.read())
        events = []
        for e in ics_cal.events:
            events.append(Event(
                title=e.name or "Untitled",
                start=e.begin,
                end=e.end,
                location=e.location
            ))
        return events