def append_to_txt(filename, string_text):
    with open(filename, "a") as myfile:
        myfile.write(string_text+"\n")

def read_bottom_line_txt(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        # print(last_line)
        return last_line

def read_txt(fileloc):
    try:
        with open(fileloc, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File does not exist")
