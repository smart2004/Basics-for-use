li = '1111101'
overall = sum(int(bit) * (2 ** i) for i, bit in enumerate(li[::-1]))
print(overall)
