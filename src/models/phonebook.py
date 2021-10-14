class Phonebook:

    def __init__(self):
        self.contacts = []

    def name_or_number_exists(self, name, number):
        # iterates through contacts to see if the name or number exists
        for contact in self.contacts:
            if contact.name == name or contact.number == number:
                return True

        return False

    def search_with_name(self, name):
        # iterates through contacts to return the first instance with a matching name
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def name_exists(self, name):
        contact = self.search_with_name(name)
        return contact is not None

    # fetches a collection of alias contacts
    def get_aliases(self, number):
        # sorts out the origin of a certain number
        return self.get_by_number(number)[1:]

    def get_by_number(self, number):
        contacts = []
        # iterates and returns all contacts with a specific number
        for contact in self.contacts:
            if contact.number == number:
                contacts.append(contact)
        return contacts

    # indicates weather one or more contacts uses a number
    def number_exists(self, number):
        for contact in self.contacts:
            if contact.number == number:
                return True
        return False
