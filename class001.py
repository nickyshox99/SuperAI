# nameList = ['winn','thanarak','somchai']

# def countnamewithalphabet(alphabet):
#     count = 0
#     for name in nameList:
#         if alphabet in name:
#             count = count+1
#     return count

# print(str(countnamewithalphabet('i')))

class student:
    def __init__(self,studentName,age,sex):
        self.Name = studentName
        self.Age = age
        self.Sex = sex
    
x = student("Big",20,"Male")
y = student("Bee",20,"Male")

print(x.Name)
print(y.Name)

