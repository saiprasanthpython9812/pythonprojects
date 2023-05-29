import os
import datetime

# print(dir(os))
path = os.getcwd()
new_path = path + "\\" + "newpractice.py"
print(new_path)

new_file_stat = os.stat(new_path)

print(new_file_stat)

created_time = new_file_stat.st_ctime

print(created_time)

date_needed = datetime.datetime.fromtimestamp(created_time)
print(date_needed)




