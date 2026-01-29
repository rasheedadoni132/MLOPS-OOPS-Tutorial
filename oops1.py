# intiate class
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print('Started executing attribute/data')
        self.id = 123
        self.salary = 50000
        self.designation = 'SDE'
        print('attributes/data have been initiated')
    
    def travel(self, destination):
        print('This travel method called manually')
        print(f"Employee is now travelling to {destination}")



# creating instance/object
sam = employee()

# printing the attributes
print(sam.id)

# calling a method
sam.travel("kerala")