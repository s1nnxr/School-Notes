import sys
print(type(z), sys.getsizeof(z))

from decimal import Decimal, getcontext

getcontext().prec = 5           # nastavení přesnosti na 5 desetinných míst
a = Decimal('1') / Decimal('7')
print(type(a), a)

# Zaokrouhlování

from decimal import Decimal, ROUND_HALF_UP

value = Decimal('2.675')
rounded = value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(rounded)


from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_DOWN, ROUND_UP, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN
# běžné zaokrouhlování ROUND_HALF_UP
value = Decimal('1.55')

print("ROUND_CEILING:  ", value.quantize(Decimal('0.1'), rounding=ROUND_CEILING))   # 1.6
print("ROUND_FLOOR:    ", value.quantize(Decimal('0.1'), rounding=ROUND_FLOOR))     # 1.5
print("ROUND_DOWN:     ", value.quantize(Decimal('0.1'), rounding=ROUND_DOWN))      # 1.5
print("ROUND_UP:       ", value.quantize(Decimal('0.1'), rounding=ROUND_UP))        # 1.6
print("ROUND_HALF_UP:  ", value.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))   # 1.6
print("ROUND_HALF_DOWN:", value.quantize(Decimal('0.1'), rounding=ROUND_HALF_DOWN)) # 1.5
print("ROUND_HALF_EVEN:", value.quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN)) # 1.6


