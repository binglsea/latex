import re

x = "100以内有25个质数。不实际计算的话,其中51和91很容易被误判为是质数。"
x = re.sub("质数", "素数", x)
x = x.replace("其中", '')
print(x)
