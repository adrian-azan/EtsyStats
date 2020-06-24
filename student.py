class student:

    def __init__(self, name,subject):
        self.name = name     #string
        self.subject = subject


    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __hash__(self):
        return hash(self.name)
            