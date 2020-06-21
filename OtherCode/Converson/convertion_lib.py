def string_list(var1):
    TYPE = type(var1)
    if TYPE == str:
        list1 = []
        list1.append(var1)
        return list1
    else:
        return "Input is not a string"

def list_string(list1):
    TYPE = type(list1)
    if TYPE == list:
        str1 = "".join(list1)
        return str1
    else:
        return "Input is not a list"


def string_list_byChar(str1):
    TYPE = type(str1)
    if TYPE == str:
        return list(str1)
    else:
        return "Input is not a string"

def charList_string(list1):
    TYPE = type(list1)
    if TYPE == list:
        list1 = "".join(list1)
        return list1
    else:
        return "Input is not a list"

def int_string(num):
    TYPE = type(num)
    if TYPE == int:
        return str(num)
    else:
        return "Input is not a integer"

def string_int(str1):
    TYPE = type(str1)
    if TYPE == str:
        return int(str1)
    else:
        return "Input is not a string with an integer"
#####################################################################
def float_string(num):
    TYPE = type(num)
    if TYPE == float:
        return str(num)
    else:
        return "Input is not a float"

def string_float(str1):
    TYPE = type(str1)
    if TYPE == str:
        return  float(str1)
    else:
        return "Input is not a string with a float"

def int_bool(num):
    TYPE = type(num)
    if TYPE == int:
        return bool(num)
    else:
        return "Input is not a vaild number"
    
def bool_int(bool1):
    TYPE = type(bool1)
    if TYPE == bool:
        return int(bool1)
    else:
        return "Input is not a boolin"

def char_ASCII(str1):
    TYPE = type(str1)
    if TYPE == str:
        return  ord(str1)
    else:
        return "Input is not a vaild ASCII"

def ASCII_char(num):
    TYPE = type(num)
    if TYPE == int:
        return  chr(num)
    else:
        return "Input is not a vaild ASCII"

def float_list(num):
    TYPE = type(num)
    if TYPE == float:
        list1 = []
        list1.append(num)
        return list1
    else:
        return "Input is not a float"

def list_float(list1):
    TYPE = type(list1)
    if TYPE == list:
        print(len(list1))
        for i in range(0, len(list1), 1):
            if type(list1[i]) == int:
                list1[i] = float(list1[i])
        return list1

list1 = [2,3,5,6,3,6,9]
result = list_float(list1)
print(result)

