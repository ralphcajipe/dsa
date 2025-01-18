print(0)
print(1)
count = 2 # 0 and 1 are already printed


def fibonacci(previous, current):
    global count
    if count < 20:
        new_fibo = previous + current
        print(new_fibo)
        previous = current
        current = new_fibo
        count +=1
        return fibonacci(previous, current)
    else:
        return
    
    
fibonacci(0,1)