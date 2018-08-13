#from books import Books
class Student:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address

count = 0
try: 
	count = int(input("enter the no. of students: "))

except ValueError:
	print("invalid format")

else:
	student = []
	for i in range(count):
	    x = input("Enter name: ")
	    y = input("Enter address: ")
	    stud = Student(x, y)
	    student.append(stud)

finally:
	disp = map(lambda stud: stud.getName() + " " + stud.getAddress(), student)
	print(list(disp))


"""for i in range(n):
    x = input("Enter name: ")
    y = input("Enter address: ")
    stud = Student(x, y)
    student.append(stud)

disp = map(lambda stud: stud.getName() + " " + stud.getAddress(), student)
print(list(disp))
book1= Books(43, "how to be a annoying person", "ramesh magante" ) 
book1.showAuthor()   """