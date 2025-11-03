from datetime import timedelta
from ics import Calendar as ICSCalendar, Event as ICSEvent

class CalendarExporter:
    """Class for exporting data into an .ics file."""
    def export(self, filepath: str, events):
        ics_cal = ICSCalendar()

        for e in events:
            event_name = f"{e.emoji} {e.title}" if e.emoji else e.title

            new_event = ICSEvent(
                name=event_name,
                location=e.location,
                description=e.description,
                uid=e.uid,
                status=e.status
            )

            if getattr(e, "is_all_day", False):
                start_date = e.start.date()
                end_date = e.end.date()

                # Adjust to avoid the extra +1 day
                if (end_date - start_date).days > 1:
                    end_date -= timedelta(days=1)

                new_event.begin = start_date
                new_event.end = end_date
                new_event.make_all_day()
            else:
                new_event.begin = e.start
                new_event.end = e.end
            ics_cal.events.add(new_event)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(ics_cal.serialize_iter())