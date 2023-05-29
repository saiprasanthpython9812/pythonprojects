import os
import shutil
# os.chdir(r"C:\Users\U1142017\Desktop\AWS COMPUTE")
# print(os.listdir())

# This gives root path for the folder given in walk command and it gives directories present and files present

# for root, directory, file in os.walk(os.getcwd()):
#     for f in file:
#         if ".json" in f:
#             print(f)
#
# os.mkdir("abc")
# print(os.getcwd())
#
# print(os.listdir(os.getcwd()))

# directory = "sidhufolder"
#
# path = os.path.join(os.getcwd(), directory)
#
# if not os.path.exists(path):
#     os.mkdir(path)
# else:
#     os.rmdir(path)

# print(os.listdir(os.getcwd()))
# path = os.path.join(os.getcwd(), 'osmodule.py')
# print(os.path.getctime(path))
#
# print(os.path.getsize(path))
path = r"C:\Users\U1142017\Downloads\sample"
os.chdir(path)
files_list = os.listdir()
print(files_list)

path_desktop = r"C:\Users\U1142017\Downloads\TEST"
list_extensions=[]
for file in files_list:
    ext = file.split(".")[-1]
    list_extensions.append(ext)
print(list_extensions)
list_extensions = set(list_extensions)
print(list_extensions)

for ex in list_extensions:
    if not os.path.exists(os.path.join(path_desktop, ex)):
        os.mkdir(os.path.join(path_desktop, ex))
    for f in files_list:
        if ex in f:
            shutil.copy(f,path_desktop+"\\"+ex)














