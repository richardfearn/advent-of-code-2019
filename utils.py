def read_input():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    lines = [line.rstrip() for line in lines]
    return lines
