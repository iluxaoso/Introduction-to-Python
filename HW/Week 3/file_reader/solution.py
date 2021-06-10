class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return ""
