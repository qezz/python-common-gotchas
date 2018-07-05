def create_multipliers():
    return [lambda x : i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))

def fixed_create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]

for multiplier in fixed_create_multipliers():
    print(multiplier(2))
