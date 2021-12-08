import math

#### 验证正整数 n 是否为素数
#? 不合理地验证一个非整数是否为素数的结果是什么？
def isPrime(n):
    if n < 2:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:  # 排除大于 2 的偶数
        return False
    # No else: to work on cases when n > 3
    
    #for i in range(3, math.floor(math.sqrt(n)), 2):
    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            return False
                   
    return True


#### Version 1: 找出小于 n 的全部素数，假定 n > 2
def primesLessThanN_v1(n):
    primes = [];
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)
            
    return primes


#### 把一个正整数分解成素数幂的乘积
##   输入：待分解的正整数。
##   输出：字典，键为所包含的素数因子，值为所包含的该素数因子的最高幂。
def decomposeInt(n):
    if n <= 1:
        return {}
    
    primeFactorCandidates = primesLessThanN_v1(n+1)
    if n in primeFactorCandidates:
        return {n: 1}
    
    result = {}
    while (n > 1):
        for i in primeFactorCandidates:
            while n % i == 0 and n > 1:
                if i in result:
                    result[i] = result[i] + 1
                else: 
                    result[i] = 1
                    
                n = n / i
    
    return result

# 华罗庚《数论导引》第 3 页例：10725 = 3 * 5^2 * 11 * 13
print("10725 分解为：")
result = decomposeInt(10725)
for key in result:
    print(str(key), "^", str(result[key]))
    
    
# 找出 100 以内的全部素数
for n in range(2, 100):
    if isPrime(n):
        print(str(n), sep=' ', end=' ')
    
    
"""
for n in allPrimesLessThanN_v1(100):
    print(n)
"""
  
"""  
def generatePrimes(n):
    primes = ()
    if n < 2:
        return primes
    primes.append(2)
    
    #for k in range(3, int(math.sqrt(n)))
"""  
    

#%%

print(int(math.sqrt(35)))

