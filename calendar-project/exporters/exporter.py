from ics import Calendar as ICSCalendar, Event as ICSEvent

class CalendarExporter:
    def save(self, filepath: str, events):
        ics_cal = ICSCalendar()
        for e in events:
            new_event = ICSEvent(
                name=f"{e.emoji} {e.title}",
                begin=e.start,
                end=e.end,
                location=e.location
            )
            ics_cal.events.add(new_event)

        with open(filepath, 'w') as f:
            f.writelines(ics_cal)