#=================================
# Convert a number into a list
print("** 3.  number to list and back #1 -- digit by digit **")
nums = 12345
print(type(nums))
print(nums)

strNums = str(nums)
print(type(strNums))
print(strNums)

numsList = list(strNums)
print(type(numsList))
print(numsList)

strNums = ''.join(numsList)
print(type(strNums))
print(strNums)

nums = int(strNums)
print(type(nums))
print(nums)
print("\n\n")