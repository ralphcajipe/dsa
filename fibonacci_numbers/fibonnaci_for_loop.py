# First 20 Fibonnaci Numbers

previous = 0
current = 1

print(previous)
print(current)

for fibo in range(18):
    new_fibo = previous + current
    print(new_fibo)
    previous = current
    current = new_fibo