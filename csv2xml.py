
def open(str):
    return "<"+str+">"

def close(str):
    return "</"+str+">"

def openFile(str):
    file = open(str, "r")
    print(file.readlines())

def main():
    filename = 'C:\\Users\student\Documents\CS Homeworks\main.txt'
    openFile(filename)


main()
