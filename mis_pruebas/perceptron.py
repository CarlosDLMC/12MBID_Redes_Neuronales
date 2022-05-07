import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def activate(x):
    return 0 if x < 0.5 else 1


calculate = np.vectorize(activate)


training_inputs = np.array([[0, 0, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])

training_outputs = np.array([[0, 1, 0, 1]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3, 1)) - 1
output = None
for i in range(10):
    output = sigmoid( training_inputs.dot(synaptic_weights) )
    error = training_outputs - output
    adjustments = np.dot(training_inputs.T, error * (output * (1 - output)))
    print(f"adjustments: {adjustments}")
    synaptic_weights += adjustments

new_case = np.array([[1, 0, 0]])
result = calculate(np.dot(new_case, synaptic_weights))

def request_calculation(s):
    new_case = np.array([[int(number) for number in s.split()]])
    result = calculate(np.dot(new_case, synaptic_weights))
    return result[0][0]

while True:
    res = input("Enter the 3 first numbers of the array: ")
    if res.upper() == "Q":
        break
    print(f"The answer is {request_calculation(res)}")

