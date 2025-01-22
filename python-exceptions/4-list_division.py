#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError
            if not isinstance(my_list_1[i], (int, float)):
                raise TypeError
            if not isinstance(my_list_2[i], (int, float)):
                raise TypeError

            result.append(my_list_1[i] / my_list_2[i])
            division_result = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            if 'division_result' not in locals():
                division_result = 0
            result.append(division_result)
    return result
