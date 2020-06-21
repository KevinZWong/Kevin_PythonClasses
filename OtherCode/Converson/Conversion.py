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



##############  boolin ## int #################
num = 1
result = int_bool(num)
print("int_bool:",result)

str1 = True
result = bool_int(str1)
print("bool_int:", result)
###########  float ## string  ###############

result = float_string(123.0)
print("float_string:", result)

result = string_float("456")
print("string_float:", result)
##############  ASCII ## char  ##################
result = char_ASCII("a")
print("char_ASCII:", result)

result = ASCII_char(65)
print("ASCII_char:", result)












###################################################################
'''
list1 = ["hi", "There"]
str1 = "hi"


char1 = ["h", "i"]
result = string_list(str1)
print(result)

result = list_string(list1)
print(result)


result = string_list_byChar("guowong")
print(result)

result = charList_string(['g','u', 'o'])
print(result)

result = int_string(123)
print(result)

result = string_int("456")
print(result)
'''

