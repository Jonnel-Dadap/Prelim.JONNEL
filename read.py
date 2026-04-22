file_path = "C:\\Users\\CLienT\\Desktop\\list of my activity\\python\\prelim\\gradedata.txt"
with open(file_path, 'r') as file:
    content1 = file.read()

file_path = "C:\\Users\\CLienT\\Desktop\\list of my activity\\python\\prelim\\product.txt"
with open(file_path, 'r') as file:
    content2 = file.read()

print(content1)
print("----------------------------------------------------------------------------------------------------")
print(content2)