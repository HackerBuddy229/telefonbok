from models.contact import Contact
from models.phonebook import Phonebook
from storage.fileStorageService import FileStorageService
from storage.phonebookSerializer import PhonebookSerializer


class Telefonbok:

    def __init__(self):
        self._phonebook = Phonebook()

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
        # check for names
        primary_contact = self._phonebook.search_with_name(name)

        if primary_contact is None:
            print("This name does not exist")
            return

        # check for contacts with the number
        contacts = self._phonebook.get_by_number(primary_contact.number)

        # present list 
        for contact in contacts:
            print(contact.format_output())

    # create a new contact with the same number as another contact but a different name
    def alias(self, origin, alias):
        # Check if name exists
        alias_exists = self._phonebook.name_exists(alias)
        if alias_exists:
            print("your alias exists as a contact")
            return

        # Fetch origin contact
        origin_contact = self._phonebook.search_with_name(origin)
        if origin_contact is None:
            print("no such contact")
            return

        # create new contact
        contact_new = Contact(alias, origin_contact.number)

        # append the contact
        self._phonebook.contacts.append(contact_new)

    # change the number for a name [including aliases]
    def change(self, name, number):
        # find number by name
        origin = self._phonebook.search_with_name(name)
        if origin is None:
            print("user does not exist")

        # get all contacts
        contacts = self._phonebook.get_by_number(origin.number)

        # for to change
        for contact in contacts:
            contact.number = number

    # Saves the current instance of the phonebook to a filename
    def save(self, filename):
        # serialize
        raw = PhonebookSerializer.serialize(self._phonebook.contacts)

        # write raw
        FileStorageService.save_raw(filename, raw)

    # fetches a phonebook instance from a file
    def load(self, filename):
        # fetch raw
        raw = FileStorageService.fetch_raw(filename)

        # TODO: Add error handeling

        # deserialize
        contacts = PhonebookSerializer.deserialize(raw)

        # replace contacts
        self._phonebook.contacts = contacts
