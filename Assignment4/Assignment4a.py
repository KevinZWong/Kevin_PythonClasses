print("4.9")
print("Enter weight and price for package 1: weight,price")
package1 = input()
print("Enter weight and price for package 2: weight,price")
package2 = input()
package1 = package1.split(",")
package2 = package2.split(",")
package1_int = int(package1[0])/int(package1[1])
package2_int = int(package2[0])/int(package2[1])
if package1_int > package2_int:
    print("Package1 is the better deal.")
elif package1_int < package2_int:
    print("Package2 is the better deal.")
else: 
    print("Both packages are equal.")
    
