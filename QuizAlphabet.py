nameList = ['winn','thanarak','somchai']

def countnamewithalphabet(alphabet):
    count = 0
    for name in nameList:
        if alphabet in name:
            count = count+1
    return count

print(str(countnamewithalphabet('n')))