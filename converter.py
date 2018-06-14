from in_out import InOut



class JsonToCbor:

    def __init__(self, data: dict) -> None:
        self.data = data

    def text_string_to_cbor(self, value: str) -> str:
        header = None
        major_type = 3 << 5
        if len(value) <= 23:
            header = major_type | len(value)
        if 24 <= len(value) <= 255:
            header = major_type | 24
        if 256 <= len(value) <= 65535:
            header = major_type | 25
        if len(value) > 655635:
            raise OverflowError("The text is too long!")
        header = bin(header)[2:].zfill(7)
        value = ' '.join(format(ord(x), 'b') for x in value)
        return "{0} {1}".format(header, value)


# insta = JsonToCbor({})
# print (insta.text_string_to_cbor("somedata"))