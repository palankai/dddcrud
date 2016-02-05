class Contact:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __eq__(self, other):
        return(
            isinstance(other, self.__class__) and
            self.name == other.name
        )

    def __str__(self):
        return '<Contact(%s, %s)>' % (self.name, self.phone)

