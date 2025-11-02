import json
from models.calendar import Calendar
from transformers.dictionary_transformer import DictionaryTransformer
from exporters.exporter import CalendarExporter
from importers.importer import CalendarImporter

class CalendarService:
    def __init__(self, importer=None, exporter=None):
        self.importer = importer or CalendarImporter()
        self.exporter = exporter or CalendarExporter()

    def transform_calendar(self, filepath: str, method: str = "dictionary") -> str:
        # Import .ics file into calendar object
        calendar = Calendar()
        for event in self.importer.load(filepath):
            calendar.add_event(event)

        # Select transformation strategy
        transformer = self._get_transformer(method)

        # Apply transformations
        for event in calendar.get_events():
            event.emoji = transformer.transform(event.title)

        # Export updated calendar
        output_path = "output.ics"
        self.exporter.export(output_path, calendar.get_events())

        return output_path

    def _get_transformer(self, method: str):
        if method == "dictionary":
            with open("utils/emoji_dict.json") as f:
                emoji_dict = json.load(f)
            return DictionaryTransformer(emoji_dict)
        # future: add regex/embedding transformers
        raise ValueError(f"Unknown transformation method: {method}")