import decimal

from decimal import Decimal, getcontext,Context

print(list(map(Decimal,[0.1,0.2,0.3,0.4])))

a = Decimal(0.3)

print(a)

print(a.quantize(Decimal('0.000'), decimal.ROUND_UP))

print(Decimal('Infinity') * (-1))