from ics import Calendar as ICSCalendar
from models.event import Event

class CalendarImporter:
    "Class for loading .ics data"
    def load(self, filepath: str):
        with open(filepath, 'r') as f:
            ics_cal = ICSCalendar(f.read())
        events = []
        for e in ics_cal.events:
            events.append(Event(
                title=e.name or "Untitled",
                start=e.begin,
                end=e.end,
                location=e.location,
                description=getattr(e, "description", None),
                uid=getattr(e, "uid", None),
                status=getattr(e, "status", None),
                is_all_day=e.all_day
            ))

        return events