import os



# os.chdir(r"C:\Users\U1142017\Desktop\AWS COMPUTE")
# print(os.listdir())

#This gives root path for the folder given in walk command and it gives directories present and files present

for root, directory, file in os.walk(os.getcwd()):
    for f in file:
        if ".json" in f:
            print(f)

os.mkdir("abc")
print(os.getcwd())

print(os.listdir(os.getcwd()))

