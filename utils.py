def read_input():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    lines = [line.rstrip() for line in lines]
    return lines


def chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
