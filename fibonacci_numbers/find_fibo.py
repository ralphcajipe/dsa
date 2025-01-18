# Finding The nth Fibonacci Number Using Recursion
# zero-based index


def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)


# 20th Fibonacci number
print(F(19))
