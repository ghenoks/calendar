class Event:
    def __init__(
        self,
        title,
        start,
        end,
        location=None,
        description=None,
        uid=None,
        status=None,
        created=None,
        last_modified=None,
        is_all_day=False
    ):
        self.title = title
        self.start = start
        self.end = end
        self.location = location
        self.description = description
        self.uid = uid
        self.status = status
        self.created = created
        self.last_modified = last_modified
        self.is_all_day = is_all_day
        self.emoji = None