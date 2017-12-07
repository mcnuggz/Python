#global scoped variable
my_name = 'Ryan'

def print_name():
    #local scope
    my_name = 'Ken'
    print("the name inside the function is", my_name)

print_name()
print("outside the function the name is",my_name)