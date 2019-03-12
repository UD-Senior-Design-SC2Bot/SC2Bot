import pickle
print("Hi!")
with open("collected_data//DESKTOP-UE0NSJE - 20190311-163034.dat", "rb") as f:
    data = pickle.load(f)
    for frame in data:
        print(frame)