"""
1)later you can try to do there with functions:
    def my_function4(**kid):
  print("His last name is " + kid["lname"])

my_function4(fname = "Tobias", lname = "Refsnes")

2) you can convert this code into object oriented version

"""

#script that creates folder generations.

import os

parent_dir="/Users/mehmet/Desktop/work/myworks/script/deneme/fcc/750-50000"

first_gen=input("Enter first generation folders: ")
first_genl=first_gen.split(";")
path1l=[]
for i1 in first_genl:
    path1=os.path.join(parent_dir,i1)
    os.mkdir(path1)
    path1l.append(path1)

second_gen=input("Enter second generation folders: ")
second_genl=second_gen.split(";")
path2l=[]
for j1 in path1l:
    for i2 in second_genl:
        path2=os.path.join(j1,i2)
        os.mkdir(path2)
        path2l.append(path2)

print("\npath2l-->")
print(path2l)
third_gen=input("Select parent folder from above ';' Enter 3.th generation folders: ")
third_genl=third_gen.split(";")
path3l=[]
if third_genl[0] == "1":
    for j2 in path2l:
        for i3 in third_genl[1:]:
            path3=os.path.join(j2,i3)
            os.mkdir(path3)
            path3l.append(path3)

elif third_genl[0] == "0":
    print("Folder generation has been done!")

else:
    count=0
    while count<len(path2l): # duruma göre 2. jenerasyon klasörlerinde farklı 3.jenerasyon klasör oluşturma
        a=input("Select parent folder from above ';' Enter 3.th generation folders: ")
        al=a.split(";")
        for folder in path2l:
            if al[0] in folder:
                print("folder :",folder)
                for i4 in al[1:]:
                    path33=os.path.join(folder,i4)
                    os.mkdir(path33)
        count+=1
    print("DONE!")
