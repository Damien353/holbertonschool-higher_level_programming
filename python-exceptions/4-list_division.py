#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError

            if (not isinstance(my_list_1[i], (int, float)) or 
                not isinstance(my_list_2[i], (int, float))):
                raise TypeError
            division_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            division_result = 0
            print("division by 0")
        except TypeError:
            division_result = 0
            print("wrong type")
        except IndexError:
            division_result = 0
            print("out of range")
        finally:
            result.append(division_result)
    return result
