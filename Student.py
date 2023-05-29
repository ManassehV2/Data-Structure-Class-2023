class Student:
    def __init__(self, name, score, rank):
        self.name = name
        self.score = score
        self.rank = rank

    def __str__(self):
        return f"Name: {self.name} Score: {self.score} Rank: {self.rank}"

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.rank < other.rank
        return False
