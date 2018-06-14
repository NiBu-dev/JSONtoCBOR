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

    def test_text_str_tp_cbor(self):
        input_value = "somedata"
        expected_output = "1101000 1110011 1101111 1101101 1100101 1100100 1100001 1110100 1100001"
        actual_output = self.conv_inst.text_string_to_cbor(input_value)
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()