def solution(number):
    sumlist = []
    for i in range(1, number):
        if (i%3 == 0 or i%5 == 0):
            sumlist.append(i)
    return sum(sumlist)