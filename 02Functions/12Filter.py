# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# filter()函数返回一个Iterator，要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip() # 删除字符串中开头结尾处的空白字符

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 埃氏筛法求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisble(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisble(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 回文数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))