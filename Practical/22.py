class Log:
    def __init__(self, long_filename):
        self.long_filename = long_filename

    def write_err(self, massage):
        try:
            with open(self.long_filename, 'a') as log_file:
                log_file.write(f'err: {massage}')

        except Exception as e:
            print(f'err : {e}')
            