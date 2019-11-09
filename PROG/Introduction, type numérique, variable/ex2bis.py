masse_ge: float = 0
masse_laus: float = 0
masse_montr: float = 0

masse_ge = 5000 - (35 * 54.5 + 40 * 35)
masse_laus = masse_ge - 150 * 5
masse_montr = masse_laus - 29 * 12.5

print(masse_ge)
print(masse_laus)
print(masse_montr)
