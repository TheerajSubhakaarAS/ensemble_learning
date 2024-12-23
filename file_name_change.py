import os 

path = "Multiple_dataset"
dis_list = os.listdir(path)
for i in dis_list:
    new_path = str(path)+"/"+str(i)
    dis_list1 = os.listdir(new_path)
    for j in dis_list1:
        new_path1 = new_path+"/"+str(j)
        print(new_path1)