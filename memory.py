class Memory:
    def __init__(self):
        self.preferences = {
            "brand": "Sony",
            "max_price": 100,
            "shipping": "Prime"
        }

    def update(self, key, value):
        self.preferences[key] = value

    def get(self, key):
        return self.preferences.get(key)
