import random
import hashlib

def sha256_2_string(string_to_hash):
    """ Returns the SHA256^2 hash of a given string input
    in hexadecimal format.

    Args:
        string_to_hash (str): Input string to hash twice

    Returns:
        str: Output of double-SHA256 encoded as hexadecimal string.
    """

    # (hint): feed binary data directly between the two SHA256 rounds

    # Placeholder for (1a)

    # Reference: 
    # https://docs.python.org/3/library/hashlib.html
    # https://www.programiz.com/python-programming/methods/string/encode

    m = hashlib.sha256()                # Create a SHA-256 hash object
    m.update(string_to_hash.encode())   # Feed the byte object using update()
    temp_m = m.digest()                 # Return the digest of the strings passed to the update()
    m = hashlib.sha256()
    m.update(temp_m)
    return m.hexdigest()

def encode_as_str(list_to_encode, sep = "|"):
    """ Encodes a list as a string with given separator.

    Args:
        list_to_encode (:obj:`list` of :obj:`Object`): List of objects to convert to strings.
        sep (str, optional): Separator to join objects with.
    """
    return sep.join([str(x) for x in list_to_encode])

def nonempty_intersection(list1, list2):
    """ Returns true iff two lists have a nonempty intersection. """
    return len(list(set(list1) & set(list2))) > 0
