#import math
from num_theory import decomposePositiveInt, isPrime
from num_theory import primesLessThanN

# 找出 100 以内的全部素数
for n in range(2, 100):
    if isPrime(n):
        print(str(n), sep=' ', end=' ')
print("")

# 华罗庚《数论导引》，以下简称华著。我们将应用编程好的函数于该书中的例子。

# 华著第 3 页例：10725 = 3 * 5^2 * 11 * 13
print("10725 分解为：")
result = decomposePositiveInt(10725)
for key in result:
    print(str(key), "^", str(result[key]))
    

#华著第 4 页例：2^2281 - 1 是素数。根据因式分解公式反推，2281 应该是素数。
print("{}^{} - 1 是素数。根据因式分解公式反推：{} 是素数。".format(2, 2281, 2281))
print("验证 {} 是素数：{}。".format(2281, isPrime(2281)))


# 找出 100 以内的全部素数
#print(primesLessThanN_v1(1000))
#print(primesLessThanN(100000))


#print(primesLessThanN(10007000))

"""
2 ~ 3 is prime: True
3 ~ 7 is prime: True
5 ~ 31 is prime: True
7 ~ 127 is prime: True
11 ~ 2047 is prime: False
13 ~ 8191 is prime: True
17 ~ 131071 is prime: True
19 ~ 524287 is prime: True
23 ~ 8388607 is prime: False
29 ~ 536870911 is prime: False
31 ~ 2147483647 is prime: True
37 ~ 137438953471 is prime: False
41 ~ 2199023255551 is prime: False
43 ~ 8796093022207 is prime: False
47 ~ 140737488355327 is prime: False
53 ~ 9007199254740991 is prime: False
59 ~ 576460752303423487 is prime: False
61 ~ 2305843009213693951 is prime: True
67 ~ 147573952589676412927 is prime: False
71 ~ 2361183241434822606847 is prime: False
73 ~ 9444732965739290427391 is prime: False
79 ~ 604462909807314587353087 is prime: False
83 ~ 9671406556917033397649407 is prime: False
不要试 89
"""