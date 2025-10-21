from ics import Calendar
import re

from ics import Calendar

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)

# dictionary
# read ics file
# regex find words
# replace them with dictionary
# export it into ics file

"""
emoji_dict = {
    "meeting": "💼",
    "lunch": "🍽️",
    "coffee": "☕",
    "project": "📁",
    "deadline": "⏰",
    "call": "📞",
    "birthday": "🎂",
    "gym": "🏋️",
    "vacation": "🏖️",
    "doctor": "🩺",
}


def replace_with_emoji(event_name, emoji_dict):
    name_lower = event_name.lower()
    for keyword, emoji in emoji_dict.items():
        # Simple keyword check (regex word boundaries for better match)
        if re.search(rf"\b{re.escape(keyword)}\b", name_lower):
            return emoji
    # Default fallback emoji if nothing matches
    return "📅"

# Read the file
with open("basic.ics", "r", encoding="utf-8") as f:
    calendar = Calendar(f.read())

# Loop through events
for event in calendar.events:
    print("Title:", event.name)
    print("Start:", event.begin)
    print("End:", event.end)
    print("Description:", event.description)
    print("Location:", event.location)
    print("-" * 40)

for event in calendar.events:
    original_name = event.name or ""
    emoji_name = replace_with_emoji(original_name, emoji_dict)
    print(f"Original: {original_name} → {emoji_name}")

"""