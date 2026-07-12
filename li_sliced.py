li = '1111101'
overal = sum(int(bit) * (2 ** i) for i, bit in enumerate(li[::-1]))
print(overal)
