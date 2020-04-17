def answer1(data, n):
    newList = []
    for i in range(len(data)):
        newList.append(data[i])
        if newList.count(data[i]) > n:
            newList.pop(-1)

    return newList

def answer2(data, n):
    newList = []
    for i in range(len(data)):



def main():
    data = [1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 6, 6]
    n = 2
    print(answer(data, n))


main()
