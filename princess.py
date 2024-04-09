class PrincessQuiz:
    def __init__(self, Ariel=0, Belle=0, Cinderella=0, Mulan=0):
        self.personalities = {
            'Belle': 0,
            'Cinderella': 0,
            'Mulan': 0,
            'Ariel': 0
        }

    def add(self, personality):
        self.personalities[personality] += 1

    def get_personality(self):
        return max(self.personalities, key=self.personalities.get)

    def clear(self):
        self.personalities = {
            'Belle': 0,
            'Cinderella': 0,
            'Mulan': 0,
            'Ariel': 0,
        }
