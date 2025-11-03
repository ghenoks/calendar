class Event:
    def __init__(
            self,
            title,
            start,
            end,
            location=None,
            description = None,
            uid = None,
            status = None,
            is_all_day = False
    ):
        self.title = title
        self.start = start
        self.end = end
        self.location = location
        self.description = description
        self.uid = uid
        self.status = status
        self.is_all_day = is_all_day
        self.emoji = None