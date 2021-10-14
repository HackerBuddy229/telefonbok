from contact import Contact
from phonebook import Phonebook


class Telefonbok:
    _phonebook = None

    def __init__(self):
        _phonebook = Phonebook()

    # Adds a name with corresponding number to the phonebook
    # Name != other_names
    # number != other_numbers
    def add(self, name, number):
       # check if name OR number exists
        exists = self._phonebook.name_or_number_exists(name, number) 

       # create contact
        new_contact = Contact(name, number)

       # append contact
        self._phonebook.contacts.append(new_contact)

    # prints a contact to screen based on the name (also alias with the same number)
    def lookup(self, name):
        contacts = []

        # check for names
        primary_contact = self._phonebook.search_with_name(name)

        if primary_contact is None:
            print("This name does not exist")
            return

        contacts.append(primary_contact)

        # check for contacts with the number
        aliases = self._phonebook.get_aliases(primary_contact.number)

        if len(aliases) > 0:
            contacts += aliases

        # present list 
        for contact in contacts:
            print(contact.format_output())

    # create a new contact with the same number as another contact but a different name
    def alias(self):
        pass

    # change the number for a name [including aliases]
    def change(self):
        pass

    # Saves the current instanceeof the phonebook to a filename
    def save(self):
        pass

    # fetches a phonebook instance from a file
    def load(self):
        pass
