class Event:
    def __init__(self, title, start, end, location=None):
        self.title = title
        self.start = start
        self.end = end
        self.location = location
        self.emoji = None