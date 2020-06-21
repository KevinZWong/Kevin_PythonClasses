def ASCII_char(num):
    TYPE = type(num)
    if TYPE == int:
        return  chr(num)
    else:
        return "Input is not a vaild ASCII"



result = ASCII_char(65)
print(result)
