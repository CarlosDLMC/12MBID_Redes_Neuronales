import numpy as np

def activate(x):
    return 0 if x < 0.5 else 1


a = np.array([1, 0.2, 0, 4])

# print(activate(a)) Esto daría error

calculate = np.vectorize(activate)

print(calculate(a))