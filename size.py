import os

path = r"C:\Users\U1142017\Downloads\sample"
print(os.listdir(path))
os.chdir(path)
for f in os.listdir(path):
    if (os.path.getsize(f)/(1024*1024)) > 10:
        print(f)

for root, directory, file in os.walk(path):
    print(file)