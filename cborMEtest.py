# Test the file output against cbor.me website results

from in_out import InOut
from converter import JsonToCbor
import re


class CBORtoHex:

    def __init__(self) -> None:
        self.cbor_read_f = None
        cbor_data = None
        self.io_inst = InOut()
        conv_inst = JsonToCbor({})
        json_data = self.io_inst.read_json(self.io_inst.input)
        if type(json_data) is str:
            cbor_data = conv_inst.text_string_to_cbor(json_data)
        if type(json_data) is int:
            cbor_data = conv_inst.integer_to_cbor(json_data)
        if type(json_data) is list:
            cbor_data = conv_inst.integer_to_cbor(json_data)
        self.io_inst.write_cbor(self.io_inst.output, cbor_data)
        self.convert_to_hex(self.parse_cbor())

    def parse_cbor(self) -> str:
        self.cbor_read_f = open(self.io_inst.output, "r").read()
        return self.cbor_read_f

    def convert_to_hex(self, value):
        words = re.findall(r"[01]+", value)
        print(words)
        wd = ''
        for word in words:
            if "0000" in word or (words.index(word) < len(words) and words.index(word) != 0):
                wd += "0"
            i = (hex(int(word, 2))[2:])
            wd += i
        print(wd)


if __name__ == '__main__':
    CBORtoHex()
