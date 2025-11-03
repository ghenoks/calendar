import json
from models.calendar import Calendar
from transformers.dictionary_transformer import DictionaryTransformer
from exporters.exporter import CalendarExporter
from importers.importer import CalendarImporter
from transformers.priority_transformer import PriorityTransformer


class CalendarService:
    def __init__(self, importer=None, exporter=None):
        self.importer = importer or CalendarImporter()
        self.exporter = exporter or CalendarExporter()

    def transform_calendar(self, filepath: str, method: str, user_mapping: dict | None = None) -> str:
        # Import .ics file into calendar object
        calendar = Calendar()
        for event in self.importer.load(filepath):
            calendar.add_event(event)

        # Select transformation strategy
        transformer = self._get_transformer(method, user_mapping)

        # Apply transformations
        for event in calendar.get_events():
            event.emoji = transformer.transform(event.title)

        # Export updated calendar
        output_path = "output.ics"
        self.exporter.export(output_path, calendar.get_events())

        return output_path

    def _get_transformer(self, method: str, user_mapping: dict | None = None):
        # Returns the correct transformer
        if method == "dictionary":
            with open("utils/emoji_dict.json") as f:
                emoji_dict = {k.lower(): v for k, v in json.load(f).items()}

            base_transformer = DictionaryTransformer(emoji_dict)

        # TODO: add other transformers

        # Error handling
        else:
            raise ValueError(f"Unknown transformation method: {method}")

        # If user mapping added
        if user_mapping:
            return PriorityTransformer(base_transformer, user_mapping)

        return base_transformer