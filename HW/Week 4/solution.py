import os.path
from tempfile import gettempdir


class File:
    def __init__(self, file_name):
        f = open(file_name, "a").close()
        self.file_name = file_name

    def __str__(self):
        return os.path.abspath(self.file_name)

    def read(self):
        with open(self.file_name, "r") as f:
            return f.read()

    def write(self, line):
        with open(self.file_name, "w") as f:
            return f.write(line)

    def __add__(self, other):
        with open(self.file_name, "r") as f1:
            content_1 = f1.read()
        with open(other.file_name, "r") as f2:
            content_2 = f2.read()

        new_file_dir = gettempdir()
        new_file = File(os.path.join(new_file_dir, "new_file_name"))
        new_file.write(content_1 + content_2)
        return new_file

    def __iter__(self):
        with open(self.file_name, "r") as f:
            self.lines = f.readlines()

        self.current = 0
        self.lines_num = len(self.lines)
        return iter(self.lines)

    def __next__(self):
        if self.current > self.lines_num:
            raise StopIteration

        result = self.lines[self.current]
        self.current += 1
        return result


"""
path_to_file = 'some_filename'
print(os.path.exists(path_to_file))
file_obj = File(path_to_file)
print(os.path.exists(path_to_file))
print(file_obj.read())
file_obj.write('some text')
print(file_obj.read())
file_obj.write('other text')
print(file_obj.read())
file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
file_obj_1.write('line 1\n')
file_obj_2.write('line 2\n')
new_file_obj = file_obj_1 + file_obj_2
for line in new_file_obj:
    print(ascii(line))
"""

# print(isinstance(new_file_obj, File))
