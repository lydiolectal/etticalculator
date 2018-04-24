import unittest
import re
import functools
# Classes
class Operation:
    def __init__(self, line_number, op, e1, e2, is_profane):
        self.line_number = line_number
        self.op = op
        self.e1 = e1
        self.e2 = e2
        self.is_profane = is_profane


# Functions

def parse(text):
    pass

def parse_line(text, line_number):
    operations = [{"re": "Please\sadd\s(\d+)\sto\s(\d+)", "op": "+"}]
    operation = functools.reduce((lambda acc, f_info: reducer(acc, f_info, text)), operations, None)
    if operation is None:
        return None
    else:
        return Operation(line_number, operation["op"], operation["e1"], operation["e2"], False)

def reducer(acc, f_info, text):
    print(f_info["re"])
    matches = matches_regex(text, f_info["re"])
    if matches:
        return {"e1": matches[0], "e2": matches[1], "op": f_info["op"]}
    return acc

def matches_regex(text, regex):
    add_re = re.compile(regex)
    m = add_re.match(text)
    print(m)
    if m is None:
        return False
    else:
        return m.groups()

class TestTokenizer(unittest.TestCase):

    def test_addition(self):
        input1 = "Please add 1 to 2."
        command = parse_line(input1, 1)
        expected = Operation(1, "+", "1", "2", False)
        self.assertEqual(command.line_number, expected.line_number)
        self.assertEqual(command.op, expected.op)
        self.assertEqual(command.e1, expected.e1)
        self.assertEqual(command.e2, expected.e2)
        self.assertEqual(command.is_profane, expected.is_profane)

    # def test_profane_addition(self):
    #     input1 = "Please fucking add 1 to 2."
    #     command = parse_line(input1, 1)
    #     expected = Operation(1, "+", 1, 2, True)
    #     self.assertEqual(command.line_number, expected.line_number)
    #     self.assertEqual(command.op, expected.op)
    #     self.assertEqual(command.e1, expected.e1)
    #     self.assertEqual(command.e2, expected.e2)
    #     self.assertEqual(command.is_profane, expected.is_profane)
    #
    # def test_profane_prefix_addition(self):
    #     input1 = "Fucking please add 1 to 2."
    #     command = parse_line(input1, 1)
    #     expected = Operation(1, "+", 1, 2, True)
    #     self.assertEqual(command.line_number, expected.line_number)
    #     self.assertEqual(command.op, expected.op)
    #     self.assertEqual(command.e1, expected.e1)
    #     self.assertEqual(command.e2, expected.e2)
    #     self.assertEqual(command.is_profane, expected.is_profane)
    #
    # def test_comment(self):
    #     input1 = "Hello please add 1 to 2."
    #     actual = parse_line(input1, 1)
    #     expected = None
    #     self.assertEqual(actual, expected)
    #
    # def test_addition_weird_punctuation(self):
    #     input1 = "PleAse!!?!?!?    add 1 to?????~~ 2.~~~        "
    #     command = parse_line(input1, 1)
    #     expected = Operation(1, "+", 1, 2, False)
    #     self.assertEqual(command.line_number, expected.line_number)
    #     self.assertEqual(command.op, expected.op)
    #     self.assertEqual(command.e1, expected.e1)
    #     self.assertEqual(command.e2, expected.e2)
    #     self.assertEqual(command.is_profane, expected.is_profane)
