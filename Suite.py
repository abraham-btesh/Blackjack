import Card


class Suite(Card.Card):
    def __init__(self, value, suite):
        self.suite = suite
        self.available = True
        super().__init__(value)

    def is_available(self):
        return self.available

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True
