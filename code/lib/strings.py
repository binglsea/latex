#### 生成一组 Unicode 值在 m 和 n（包括）之间的字符列表。
##   输入：Unicode 起始值 m 和终止值（包括）n。
##   输出：所定范围内相关应字符的列表。
#### Unicode 的各种字符表可见 https://www.unicode.org/charts/
"""
## 用遍历方法生成的，不推荐。
def charactersFromTo(m, n):
  result = []
  for x in range(m, n+1):
    result.append(chr(x))
  return result
"""
def charactersFromTo(m, n):
  return list(map(lambda x: chr(x), list(range(m, n+1))))


#### 汉字表。
def chineseCharacters():
  return charactersFromTo(0x4E00, 0x9FFF)


#### 大写希腊字母表：0x0391 ～ 0x03A9。
def upperCaseGreekAlphabet():
  return charactersFromTo(0x0391, 0x03A9)


#### 小写希腊字母表：0x03B1 ～ 0x03C9。
def lowerCaseGreekAlphabet():
  return charactersFromTo(0x03B1, 0x03C9)


#### 大写俄语字母表：0x0410 ～ 0x042F。
def upperCaseCyrillicAlphabet():
  return charactersFromTo(0x0410, 0x042F)


#### 小写俄语字母表：0x0430 ～ 0x044F。
def lowerCaseCyrillicAlphabet():
  return charactersFromTo(0x0430, 0x044F)


#### 数学运算符号表：0x2200 ～ 0x22FF。
def mathOperators():
  return charactersFromTo(0x2200, 0x22FF)


#print(chineseCharacters())
print(" ".join(upperCaseGreekAlphabet()))
print(" ".join(lowerCaseGreekAlphabet()))

print(upperCaseCyrillicAlphabet())
print(lowerCaseCyrillicAlphabet())
print(" ".join(mathOperators()))
print(mathOperators())

