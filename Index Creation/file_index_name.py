import os
arr = os.listdir()
arr = os.listdir("dataset")

index_name = []

for i in range(len(arr)):
    index_name.append((arr[i].replace(" ", "-").replace(".txt", "").lower()))

for i in range(len(arr)):
    arr[i] = "dataset/" + arr[i]

print(arr[1:])
print(index_name[1:])