class SpringdroidProgrammer:

    def __init__(self, program):
        self.program = program

    def get_line(self):
        s = ""
        while True:
            output = self.program.run()
            if (output == "need_input") or (output == "halt"):
                break
            if output[0] == "output":
                if output[1] > 255:
                    return output[1]
                s += chr(output[1])
        s = s.strip()
        return s

    def send_line(self, param):
        chars = [ord(c) for c in param] + [10]
        self.program.run(chars)
