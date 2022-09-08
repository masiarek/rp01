VALID_CHARS = "0123456789 ,."


def list_numbers(string, remove_chars):
    if remove_chars:
        string = "".join(char for char in string if char in VALID_CHARS)

    numbers = []
    for number in string.replace(",", " ").split():
        try:
            numbers.append(float(number))
        except ValueError:
            pass

    return numbers


def reverse_integer(number):
    as_str = str(number)
    return int(as_str[::-1])
