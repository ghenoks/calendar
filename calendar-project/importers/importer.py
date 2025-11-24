from ics import Calendar as ICSCalendar
from models.event import Event
from io import BytesIO, StringIO

class CalendarImporter:
    """Class for loading .ics data into internal Event objects."""

    def load_file(self, filepath: str):
        # Filepath loader
        with open(filepath, "r", encoding="utf-8") as f:
            return self._load_from_string(f.read())

    def load_stream(self, input_stream: BytesIO):
        # Convert bytes to string

        ics_str = input_stream.read().decode("utf-8")
        return self._load_from_string(ics_str)

    def _load_from_string(self, ics_str: str):
        ics_cal = ICSCalendar(ics_str)
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