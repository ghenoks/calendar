from transformers.emoji_transformer import EmojiTransformer


class DictionaryTransformer(EmojiTransformer):
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary

    def transform(self, text: str) -> str:
        text_lower = text.lower()
        for word, emoji in self.dictionary.items():
            if word in text_lower:
                return emoji
        return "❓"