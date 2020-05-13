
def phone_format(format, number):
    """
    phone_format('xxx-xxx-xxxx', 1234567890)
    """
    try:
        if isinstance(number, int):
            number = str(number)
        number_format = format.replace('x', '%s')

        length_of_format = format.count('x')
        length_of_number = len(number)
        
        if length_of_number == length_of_format:
            return number_format % tuple(str(number))

        # length of number > length of format
        elif length_of_number > length_of_format:
            return number_format % tuple(number[:length_of_format])            

        # length of number < length of format
        else:
            return (number_format % tuple(number.ljust(length_of_format))).strip()

    except TypeError:
        pass
    return ''