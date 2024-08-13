class Report:
    def __init__(self, filename):
        self.filename = filename

    def generate_report(self):
        try: 
            with open(self.filename, 'r') as data_file:
                data = data_file.read()
                report = f'report based on {data}'
                return report
        except FileNotFoundError:
            print('file does not exist')
        except Exception as e:
            print('error occured: {e}')
