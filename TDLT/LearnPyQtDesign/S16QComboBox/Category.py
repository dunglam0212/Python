class Category:
    def __init__(self, id = None, name = None):
        self.id = id
        self.name = name

    def __str__(self):
        return str(self.id) + '-' + self.name
