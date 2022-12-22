# import os
# out = os.path.dirname("/dwh.cfg")
# f = open("dwh.cfg", "r")
# print(f.read())
# print(out)




# import os.path
  
# # file name   
# file_name = 'dwh.cfg'
  
  
# # prints the absolute path of current
# # working directory with  file name
# print(os.path.abspath(file_name))
# files = os.path.abspath(file_name)
# f = open(files, "r")
# print(f.read())


import os
working_directory = os.getcwd()
file_path = working_directory + '/de_udacity/datawarehouse/dwh.cfg'
print(file_path)
f = open(file_path, "r")
print(f.read())





# import os  
# path ='/'
# name ='dwf.cfg'
# def find(name, path):
#     for root, dirs, files in os.walk(path):
#         if name in files:
#             print(name)  
#             #   abspath =  os.path.join(root, name) 
#             #   print (abspath)
