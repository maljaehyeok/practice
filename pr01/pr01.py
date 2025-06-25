import math


# 1번
print(abs(-100))
print(round(math.sqrt(3),2))


# 2번
WON = 1
USD = 1,366.37 * WON
EUR = 1,582.43 * WON

notebook_usd = 780 * USD
notebook_eur = 650 * EUR

print(notebook_usd < notebook_eur)


# 3번
pi = math.pi
r_1 = 50
r_2 = 45

circum_out = 2 * pi * r_1
circum_in = 2 * pi * r_2

distance = (circum_out - circum_in)

print(f"몇 미터 더 뒤에서 달려야 할까?\n{round(distance,2)}")

