class SomeClass:

    @classmethod
    def print_sth(cls):
        with open('./kacper_test/txt_files/input.txt', 'r') as input_stream:
            print('inside the function')
            content = input_stream.read()
            with open('./kacper_test/txt_files/output.txt') as output_stream:
                output_stream.write(content)