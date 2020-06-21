print("** 1.  string to list and back #1 -- char by char **")
# to convert string and list
txt = "guowong"
print(type(txt))
print(txt)

txtlist = list(txt)   # from string to list
print(txtlist)

txt = ''.join(txtlist)  # from list to re-join back to string
print(type(txt))
print(txt)
print("\n\n")
