#! /usr/bin/python3

from day25.tests import read_input
from intcode import Program

program = Program(read_input())

text = program.get_ascii()
while True:
    print(text)
    line = input(">")
    text = program.send_ascii_and_get_reply(line)
    print()
