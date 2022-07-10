def is_palindrome(self) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    # pass  # remove pass statement and implement me

    if self[::1] == self[::-1]:
        return True
    else:
        return False