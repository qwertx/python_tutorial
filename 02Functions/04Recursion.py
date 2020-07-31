# 递归
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

# 尾递归
# python没有对尾递归做优化，仍然会导致栈溢出
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(1))
print(fact(5))
print(fact(100))

# 练习
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')