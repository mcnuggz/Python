def cough_decorator(func):
    
    def func_wrapper():
        #code before function
        print("*cough*")
        func()
        #code after function
        print("*cough*")
    
    return func_wrapper

@cough_decorator
def question():
    print("can you give me a discount on that?")

@cough_decorator
def answer():
    print("No. It's only a dollar you cheapskate...")


question()
answer()