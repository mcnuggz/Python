nums = [1,2,3,4,5,6]

# def square(number):
#     return number * number

#to pass in multiple arguments for lambdas, use a comma. (lambda: n,x)
print(list(map(lambda n: n * n,nums)))