def sum_atob():
    a = int(input('input a : '))
    b = int(input('input b : '))

    start = min(a,b)
    end = max(a,b)
    result = int((end-start+1)*(start+end)/2)

    for i in range(start, end+1):
        if i< end:
            print(f'{i} + ', end='')
        else:
            print(f'{i} = {result}')