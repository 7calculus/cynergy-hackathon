r1 = input('enter the first roman: ')
r2 = input('enter the second roman: ')

def convert(r):
    num = 0
    di = {'X':10, 'V':5, 'I': 1, 'C': 100, 'D': 500, 'M': 1000, 'L': 50}
    for i in range(len(r)):
        maxm = -1
        maxm = max(maxm, di[r[i]])
    for i in range(len(r)):
        if(di[r[i]] < maxm):
            num -= di[r[i]]
        else:
            num += di[r[i]]
    return num

def c_back(val):
    fnly =""
    di1 = {'X':10, 'V':5, 'I': 1, 'C': 100, 'D': 500, 'M': 1000, 'L': 50}
    di2 = {10: 'X', 5: 'V', 1: 'I', 100: 'C', 500: 'D', 1000: 'M', 50: 'L'}
    fnly = ''
    for i in str(val):
        if i == '4':
            fnly = "IV" + fnly
        if i == '9':
            fnly = "IX" + fnly
           
            
        fnly = di2[int(i)] + fnly
            #continue

    return fnly



print(c_back(convert(r1) + convert(r2)))