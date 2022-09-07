import string

data = """
aaa1, aa1, aaaa1
a2, aaa2, aaa2"""


def strip_all_number(data):
    return data.strip(string.digits)


new_data = strip_all_number(data)
print(new_data)
