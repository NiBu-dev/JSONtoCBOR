import unittest
from in_out import InOut
from converter import JsonToCbor
import re


class InputTesCase(unittest.TestCase):

    io_inst = InOut()
    conv_inst = JsonToCbor({})

    def test_input_file_extension(self):
        expected_extension = "json"
        user_input_extension = re.findall(r"\w+.(\w+)", self.io_inst.input)
        self.assertEqual(expected_extension, user_input_extension[0])

    def test_output_file_extension(self):
        expected_extension = "cbor"
        user_input_extension = re.findall(r"\w+.(\w+)", self.io_inst.output)
        self.assertEqual(expected_extension, user_input_extension[0])

    def test_short_text_str_to_cbor(self):
        input_value = "somedata"
        expected_output = "01101000 01110011 01101111 01101101 01100101 01100100 01100001 01110100 01100001"
        actual_output = self.conv_inst.text_string_to_cbor(input_value)
        self.assertEqual(actual_output, expected_output)

    def test_medium_text_str_to_cbor(self):
        input_value = "Once upon a time there was a medium data"
        expected_output = "01111000 00101000 01001111 01101110 01100011 01100101 00100000 01110101 01110000 01101111 " \
                          "01101110 00100000 " \
                          "01100001 00100000 01110100 01101001 01101101 01100101 00100000 01110100 01101000 01100101 " \
                          "01110010 01100101 00100000 01110111 01100001 01110011 00100000 01100001 00100000 01101101 " \
                          "01100101 01100100 01101001 01110101 01101101 00100000 01100100 01100001 01110100 01100001"
        actual_output = self.conv_inst.text_string_to_cbor(input_value)
        self.assertEqual(expected_output, actual_output)

    # def test_int_to_cbor(self):
    #     input_value = 10

if __name__ == '__main__':
    unittest.main()