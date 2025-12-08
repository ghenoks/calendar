import re
from transformers_class.emoji_transformer import EmojiTransformer


class PriorityTransformer(EmojiTransformer):
    def __init__(self, base_transformer: EmojiTransformer, user_mapping: dict):
        self.base = base_transformer
        self.user_mapping = {k.lower(): v for k, v in user_mapping.items()}

        escaped_words = [re.escape(word) for word in self.user_mapping.keys()]
        pattern = r"\b(" + "|".join(escaped_words) + r")\b"
        self.regex = re.compile(pattern, re.IGNORECASE)

    def transform(self, text: str) -> str:
        match = self.regex.search(text)
        if match:
            word = match.group(1).lower()
            return self.user_mapping[word]

        # Fallback to base transformer
        return self.base.transform(text)