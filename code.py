def xor (a,b):
    if a == b:
        return 1
    else:
        return 0
def find(lis1, lis2):
    temp = []
    for n in range(0,len(lis1)):
        temp.append(0)
    for i in reversed (range(0,len(lis1))):
        t = xor(lis1[i],lis2[i])
        if t == 1 and i == len(lis1)-1:
            tp = []
            for k in range(0,len(lis1)):
                tp.append(0)
            tp.append(t)
        else:
            temp[i] = t
    return temp
def divide(list):
    temp = list[0]
    for i  in list:
        t = find(temp,i)
        temp = t
    return temp
if __name__ == "__main__":
    print("cyclic rendundancy check")
    t = [[0,1,0,1],[1,0,1,1],[0,1,1,1]]
    res = divide(t)
    print(res)