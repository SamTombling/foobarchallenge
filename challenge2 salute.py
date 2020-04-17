s = "--->-><-><-->-"
sList = []
j = 0
sCount = 0

for i in range(len(s)):
    sList.append(s[i])


for i in range(len(sList)):
    if sList[i] != ">":
        sList[i] = "-"
    else:
        for j in range(len(sList)):
            if sList[j] == "<":
                sCount = sCount + 2





print(sCount)