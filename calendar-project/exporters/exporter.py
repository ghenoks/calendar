from ics import Calendar as ICSCalendar, Event as ICSEvent

class CalendarExporter:
    "Class for exporting data into an .ics file"
    def export(self, filepath: str, events):
        ics_cal = ICSCalendar()
        for e in events:
            new_event = ICSEvent(
                name=f"{e.emoji}",
                begin=e.start,
                end=e.end,
                location=e.location
            )
            ics_cal.events.add(new_event)

        with open(filepath, 'w') as f:
            f.writelines(ics_cal)