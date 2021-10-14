class Phonebook:


    def __init__(self):
        contacts = []

    def name_or_number_exists(self, name, number):
        for contact in self.contacts:
            if contact.name == name or contact.number == number:
                return True

        return False
    
    def search_with_name(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact

        return None

    def name_exists(self, name):
       contact = self.search_with_name(name)
       return contact is not None

    def get_aliases(self, number):
        contacts = []
        for contact in contacts:
            if contact.number == number:
                contacts.append(contact)

        return contacts[1:]
