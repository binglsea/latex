import math


########
#### 验证正整数 n 是否为素数。
# ? 不合理地验证一个非整数是否为素数的结果是什么？
def isPrime(n):
    if n < 2:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:  # 排除大于 2 的偶数
        return False
    # No else: to work on cases when n > 3

    # for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


########
#### Version 1: 找出小于 n 的全部素数，假定 n > 2。
##   输入：正整数 n。
##   小于正整整 n 的所有素数的列表。
def primesLessThanN_v1(n):
    primes = [];
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)

    return primes


########
#### 找出小于 n 的全部素数，假定 n > 2。
##   输入：正整数 n。
##   输出：小于正整整 n 的所有素数的列表。
def primesLessThanN_v2(n):
    primes = [];
    if n < 2:
        return primes

    # 候选的素数集合
    candidates = list(range(2, n))
    while len(candidates) > 0:
        # 候选集里的第一个数不被更小的素数整除，所以确认它为素数
        primes.append(candidates[0])
        # 筛法：用刚确认的素数去除候选集里的数，被整除的数筛掉
        candidates = list(filter(lambda x: x % candidates[0] != 0, candidates[1:]))

    return primes


########
#### 找出小于 n 的全部素数，假定 n > 2。
##   输入：正整数 n。
##   输出：小于正整整 n 的所有素数的列表。
def primesLessThanN(n):
    if n < 2:
        return []
    if n == 3:
        return [2]

    # 建立一个从 3 到 n（但不包括 n ）的奇数的列表作为素数候选
    candidates = list(range(3, n, 2));
    # 在此列表中，[0:lastFoundPrimeIndex] 段子已确认为素数
    lastFoundPrimeIndex = 0
    upperBound = len(candidates)
    stopSieve = int(math.sqrt(n))
    # while lastFoundPrimeIndex < upperBound - 1:
    while lastFoundPrimeIndex < upperBound - 1 and candidates[lastFoundPrimeIndex] < stopSieve:
        lastFoundPrime = candidates[lastFoundPrimeIndex]

        okIndex = lastFoundPrimeIndex + 1
        checkingIndex = lastFoundPrimeIndex + 1
        while checkingIndex < upperBound:
            if candidates[checkingIndex] % lastFoundPrime != 0:
                candidates[okIndex] = candidates[checkingIndex]
                okIndex += 1
            checkingIndex += 1

        lastFoundPrimeIndex += 1
        upperBound = okIndex

    return [2] + candidates[:upperBound]


########
#### 把一个正整数分解成素数幂的乘积。
##   输入：待分解的正整数。
##   输出：字典，键为所包含的素数因子，值为所包含的该素数因子最高幂的指数。
def decomposePositiveInt(n):
    if n <= 1:
        return {}

    primeFactorCandidates = primesLessThanN_v1(n + 1)
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


########
#### 秦九韶算法（或 Euclid Algorithm）求二正在整数的最大公因子。
##   输入：两个正整数 a 和 b。
##   输出：三个数组成的列表 [d, ]。
def gcdEuclidAlgorithm(a, b):
    return ()
