#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result

    except Exception as e:
        rt = "None"
        if b == 0:
            return rt

    finally:
        if 'result' not in locals():
            result = None
        print("Inside result: {}".format(result))
