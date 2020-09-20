def findMaxValue(lst):
    maxData = lst[0]  
    rng =range(len(lst))  
    for index in rng:                
        if maxData<lst[index]:
            maxData = lst[index]
    return maxData

if __name__ == '__main__':
    listData = [90,20,30,40]
    maxResult = findMaxValue(listData)
    print(maxResult)

