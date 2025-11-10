from ics import Calendar as ICSCalendar
from models.event import Event

class CalendarImporter:
    """Class for loading .ics data into internal Event objects."""
    def load(self, filepath: str):
        with open(filepath, "r", encoding="utf-8") as f:
            ics_cal = ICSCalendar(f.read())

        events = []
        for e in ics_cal.events:
            events.append(Event(
                title=e.name or "Untitled",
                start=e.begin,
                end=e.end,
                location=getattr(e, "location", None),
                description=getattr(e, "description", None),
                uid=getattr(e, "uid", None),
                status=getattr(e, "status", None),
                created=getattr(e, "created", None),
                last_modified=getattr(e, "last_modified", None),
                is_all_day=e.all_day
            ))
        return events