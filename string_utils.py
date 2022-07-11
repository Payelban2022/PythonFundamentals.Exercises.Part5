
def str_len(word) -> int:

    """
    Given a string parameter, this function should return the length of the parameter.
    """
    # pass  # remove pass statement and implement me
#     a = input("Please input the word")
#     return a
# def word(name_word):
#     print(len(word), ",", word)
    length = (len(word))
    return length

print(str_len("word"))


def first_char(word) -> str:
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """
    # pass  # remove pass statement and implement me
#     print("The first character is:", str1[:1])
# str1 = ("Welcome to String length.")
# first_char(str1)
    firstchar = word[0]
    return firstchar
print (first_char("good"))






def last_char(word) -> str:
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """
    # pass  # remove pass statement and implement me
    lastchar = word[-1]
    return lastchar
print(last_char("good"))


def input_has_substring(fullstring,substring) -> bool:
    """
    This function determines if the substring exists within the string. Returns True or False.
    """
    pass  # remove pass statement and implement me
    if substring in fullstring:
        return True
    else:
        return False



def substring(s, start, stop) -> str:
    """
    Returns the substring of a string.

    Keyword arguments:
    str_in -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    """
    # pass  # remove pass statement and implement me
    return s[start:stop]
print(substring("beautiful",2,5))

def opposite_case(word) -> str:
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    """
    # pass  # remove pass statement and implement me
    opposite = word.swapcase()
    return opposite
print(opposite_case("Python"))
