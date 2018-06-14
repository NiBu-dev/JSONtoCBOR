from in_out import InOut



class JsonToCbor:

    def __init__(self, data: dict) -> None:
        self.data = data

    def text_string_to_cbor(self, value: str) -> str:
        length = None
        header = None
        major_type = 3 << 5
        if len(value) <= 23:
            header = major_type | len(value)
        if 24 <= len(value) <= 255:
            header = major_type | 24
            length = len(value)
        if 256 <= len(value) <= 65535:
            header = major_type | 25
            length = len(value)
        if len(value) > 655635:
            raise OverflowError("The text is too long!")
        header = bin(header)[2:].zfill(8)
        value = ' '.join(format(ord(x), '08b') for x in value)
        if length is None:
            return "{0} {1}".format(header, value)
        else:
            length = bin(length)[2:].zfill(8)
            return "{0} {1} {2}".format(header, length, value)


