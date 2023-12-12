from contextlib import contextmanager


# using class
class ManageFile:
    def __init__(self, filename, mode):
        print("init")
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_traceback):
        self.file.close()
        if exc_type:
            print(exc_type, exc_val)
        print("exit")
        return True


with ManageFile("demo2.txt", "r") as file:
    print(file.read())
    file.dfgdgs
print(file.closed)


# using decorator and generator
@contextmanager
def manage_file(file_path, mode):
    file = None
    try:
        file = open(file_path, mode)
        yield file
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if file is not None:
            file.close()


with manage_file("example.txt", "w") as file:
    file.write("Hello, this is an example.")
    file.hdhd

print(file.closed)
