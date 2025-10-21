class Calendar:
    def __init__(self):
        self.events = []

    def load_from_file(self, filepath: str, importer):
        self.events = importer.load(filepath)

    def apply_transformer(self, transformer):
        for event in self.events:
            event.emoji = transformer.transform(event.title)

    def export_to_file(self, filepath: str, exporter):
        exporter.save(filepath, self.events)