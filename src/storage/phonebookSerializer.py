from contactSerializer import ContactSerializer


class PhonebookSerializer:

    @staticmethod
    def serialize(phonebook):
        product = ""
        for contact in phonebook:
            # interpolate the serialized contact + newline
            product = product + f"{ContactSerializer.serialize(contact)}\n"

        return product

    @staticmethod
    def deserialize(raw_phonebook):
        product = []

        # split by newline
        split = raw_phonebook.split("\n")

        # append deserialized row to product var
        for contact in split:
            product.append(ContactSerializer.deserialize(contact))

        return product
