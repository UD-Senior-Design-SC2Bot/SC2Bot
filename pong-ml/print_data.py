import pickle
print("Hi!")
with open("collected_data//FRANKHULMES-PC - 03-25-2019 14 hr - 41 m - 31 s.dat", "rb") as f:
    data = pickle.load(f)
    for frame in data:
        print(frame)