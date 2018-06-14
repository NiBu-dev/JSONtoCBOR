import json


class InOut:

    def __init__(self) -> None:
        # self.input = input("Enter the name of the input json file: ")
        # self.output = input("Enter the name of the output CBOR file: ")
        self.input = "myJson.json"
        self.output = "out.cbor"
        self.bin_data = None

    def read_json(self, file_name: str) -> dict:
        read_data = open(file_name).read()
        return json.loads(read_data)

    def write_cbor(self, file_name: str) -> object:
        self.bin_data = open(file_name, "w")
        return self.bin_data


if __name__ == '__main__':
    io_inst = InOut()