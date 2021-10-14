from models.contact import Contact


class ContactSerializer:

    @staticmethod
    def serialize(contact):
        return contact.name + ";" + contact.number + ";"

    @staticmethod
    def deserialize(raw_contact) -> Contact:
        split_contact = raw_contact.split(";")

        # check raw is valid
        if len(split_contact) < 3:
            return None

        name = split_contact[0]
        number = split_contact[1]

        # instance contact
        contact = Contact(name, number)
        return contact
