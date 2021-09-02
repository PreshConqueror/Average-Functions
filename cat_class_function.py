#Class and Function

class Cat:
    #public member varaibles of cat age and cat name
    name = ''
    age = 0

    #init method initializing string member variables to empty strings and numeric vales to 0
    def __init__(self):
        self.name = ''
        self.age = 0

    #method populate() used to assign values to the member variables of the class    
    def populate(self, n,a):
        self.name = n
        self.age = a

    #method display() used to display the member variables of the class    
    def display(self):
        print('Cat name:',self.name)
        print('Cat age:',self.age)

c = Cat()
c.display()
#prompting user input to demonstrate the use of the Cat class
n = input('Enter cat name: ')
a = input('Enter cat age: ')
c.populate (n,a)
c.display()
