class FileManager:
    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print('file does not exist')
        except Exception as e:
            print(f'error occured: {e}')

    def write_file(self, filename, content):
        try:
            with open(filename, 'w') as file:
                file.write(content)
        except Exception as e:
            print(f'error occured: {e}')
