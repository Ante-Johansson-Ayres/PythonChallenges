import time
delay = 1
tries = 3
backoff = 2
def retry(fun):
    def wrapper(x, y):
        for i in range(tries):
            try:
                result = fun(x,y)
                return result
            except Exception:
                time.sleep(delay^(backoff*i))
                print("Failed! Try no: " + str(i+1) + " (waited " + str(delay^(backoff*i)) + " seconds) \n")
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
