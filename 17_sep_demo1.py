# passing positional arguments to decorators
def accept_the_arguments(function_to_decorator):
    def inner_function(*args, **kwargs):
        print("positional arguments are", args)
        print("The Keyword arguments are", kwargs)
        function_to_decorator(*args)
    return inner_function

@accept_the_arguments
def function_with_args(a,b,c):
    print(a,b,c)

function_with_args(10,20,30)