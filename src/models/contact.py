class Contact:
    name = ""
    number = ""

    def __init__(self, name, num):
        self.name = name
        self.number = num

    def format_output(self):
        return self.number
