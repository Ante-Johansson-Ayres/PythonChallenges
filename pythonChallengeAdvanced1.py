import time
delay = 1
tries = 3
def retry(fun):
    def wrapper(x, y):
        for i in range(tries):
            try:
                result = fun(x,y)
                return result
            except ZeroDivisionError:
                time.sleep(delay)
                print("Failed! Try no: " + str(i+1) +"\n")
        print("TOTAL FAILURE!")
        return None
    return wrapper
@retry 
def division(x, y):
    return x/y

kvot = division(1,1)
print(kvot)

kvot = division(1,0)
print(kvot)
