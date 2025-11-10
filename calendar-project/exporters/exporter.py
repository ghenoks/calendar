from datetime import timedelta
from ics import Calendar as ICSCalendar, Event as ICSEvent

class CalendarExporter:
    """Class for exporting events into an .ics file."""
    def export(self, filepath: str, events):
        ics_cal = ICSCalendar()

        for e in events:
            # Název — anonymizovaný (emoji) nebo původní
            event_name = f"{e.emoji or ''} {e.title}".strip()

            new_event = ICSEvent(
                name=event_name,
                location=e.location,
                description=e.description,
                uid=e.uid,
                status=e.status
            )

            if e.created:
                new_event.created = e.created
            if e.last_modified:
                new_event.last_modified = e.last_modified

            if e.is_all_day:
                start_date = e.start.date()
                end_date = e.end.date()

                # if same day -> add +1 to make DTEND valid
                if end_date <= start_date:
                    end_date = start_date + timedelta(days=1)
                else:
                    end_date -= timedelta(days=1)

                new_event.begin = start_date
                new_event.end = end_date
                new_event.make_all_day()
            else:
                new_event.begin = e.start
                new_event.end = e.end

            ics_cal.events.add(new_event)

        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(ics_cal.serialize_iter())