import pickle
x_new = [
    [7.2, 3.2, 4.8, 1.2],
    [6.2, 2.2, 3.8, 0.6]
]
model = pickle.load(open('model.pkl', 'rb'))
predictions = model.predict(x_new)
print("output", predictions)