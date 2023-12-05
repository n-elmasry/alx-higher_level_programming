#!/usr/bin/python3
"""   returns the dictionary description  """


def class_to_json(obj):
    """  returns the dictionary description  """
    newdict = {}

    for attr in obj.__dict__:
        attrvalue = getattr(obj, attr)
        if isinstance(attrvalue, (list, dict, str, int, bool)):
            newdict[attr] = attrvalue
    return newdict
