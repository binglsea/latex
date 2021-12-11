import re

x = "100以内有25个质数。不实际计算的话,51和91很容易被误判为是质数。"
y = re.sub("质数", "素数", x)
z = x.replace("素数", "质数")
print(x)
