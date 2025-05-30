import json
import os

class UserPreferences:
    def __init__(self, filename="preferences.json"):
        self.filename = filename
        self.preferences = self.load_preferences()

    def load_preferences(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        else:
            # Default preferences
            return {
                "preferred_brands": ["Apple"],
                "max_budget": 200,
                "shipping_speed": "Prime"
            }

    def update_preference(self, key, value):
        self.preferences[key] = value
        self.save_preferences()

    def save_preferences(self):
        with open(self.filename, "w") as f:
            json.dump(self.preferences, f, indent=4)
