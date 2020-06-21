print("** 2.  string to list and back #2 -- word by word **")
txt2 = "guo chang wong"
print(type(txt2))
print(txt2)

txtlist2 = txt2.split()  # from string to list
print(type(txtlist2))
print(txtlist2)

txt2 = ' '.join(txtlist2)
print(type(txt2))
print(txt2)
print("\n\n")