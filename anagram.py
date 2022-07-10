def is_anagram(str1, str2) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    # pass  # remove pass statement and implement me
    if(sorted(str1) == sorted(str2)):
        return True
    else:
        return False

