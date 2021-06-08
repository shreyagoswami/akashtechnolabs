n1 = 10
print(n1, "is a type", type(n1))

n2 = 20.5
print(n2, "is a type", type(n2))
print(n2, "is a complex number", isinstance(20.5, int))

n3 = 1 + 2j
print(n3, "is a complex number?", isinstance(1 + 2j, complex))
