
class JsonToCbor:

    def __init__(self, data: dict) -> None:
        self.data = data
        self.majorTypes = {"u_int": 0 << 5, "s_int": 1 << 5, "string": 3 << 5, "array": 4 << 5,
                      "map": 5 << 5}
        self.intTypes = {"uint_8": 24, "uint_16": 25, "uint_32": 26, "uint_64": 27}

    def text_string_to_cbor(self, value: str) -> str:
        length = None
        header = None

        if len(value) <= 23:
            header = self.majorTypes["string"] | len(value)
        if 24 <= len(value) <= 255:
            header = self.majorTypes["string"] | self.intTypes["uint_8"]
            length = len(value)
        if 256 <= len(value) <= 65535:
            header = self.majorTypes["string"] | self.intTypes["uint_16"]
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

    def integer_to_cbor(self, value: int) -> str or None:
        header = None
        major_type = None
        if value >= 0:
            major_type = self.majorTypes["u_int"]
        if not value >= 0:
            major_type = self.majorTypes["s_int"]
            value = abs(value) - 1
        if value <= 23:
            header = major_type | value
            header = "{0:08b}".format(header)
            return header
        if value > 23:
            if 0 <= value.bit_length() <= 8:
                header = major_type | self.intTypes["uint_8"]
            if 8 < value.bit_length() <= 16:
                header = major_type | self.intTypes["uint_16"]
            if 16 < value.bit_length() <= 32:
                header = major_type | self.intTypes["uint_32"]
            if 32 < value.bit_length() <= 64:
                header = major_type | self.intTypes["uint_64"]
            header = "{0:08b}".format(header)

            return "{0} {1}".format(header, "{0:08b}".format(value))