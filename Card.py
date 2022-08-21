class Card:
    def __init__(self, value):
        if 0 <= value <= 14:
            self.value = value
        else:
            raise ValueError("invalid card")

    def get_value(self):
        return self.value
