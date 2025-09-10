# #create directory
# import os
# directory = "my_folder"
# os.mkdir(directory)
# print("directory created")



# #delete directory
# import os
# os.rmdir("my_folder")
# print("directory deleted")



# #current working directory
# import os
# print(os.getcwd())



# #list files and directories
# import os
# print("list and directories: ")
# print(os.listdir())



# #path exist or not
# import os
# if os.path.exists("my_folder"):
#     print("path exists")
# else:
#     print("path doesn't exists")    



#check if path is file or directory
import os
path = "my_folder"
if os.path.isdir(path):
    print("it is directory")
elif os.path.isfile(path):
    print("it is file")
else:
    print("doesn't exist")        