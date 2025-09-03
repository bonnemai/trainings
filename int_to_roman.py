
def intToRoman( num: int) -> str:
    _map={1:'I', 5:'V', 10:'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    if num in _map: 
        return _map[num]

    results=''
    if num>=1000: 
        nb_M=num//1000
        results+='M'*nb_M
        num=num%1000
    if num>=500:
        nb=num//100
        if nb==9:
            results+='CM'
        else:
            # nb=num//500
            results+='D'
            num=num%500
    if 100<=num<=499:
        nb=num//100
        if nb==4:
            results+='CD'
        else:
            results+='C'*nb
    num=num%100
    if num>=50:
        nb=num//10
        if nb==9:
            results+='XC'
        else:
            results+='L'
            num=num%50
        # else:
        #     results+='L'*nb
    if 10<=num<=49:
        nb=num//10
        if nb==4:
            results+='XL'
        else:
            results+='X'*nb
    num=num%10
    if num>=5:
        if num==9:
            results+='IX'
        else:
            results+='V'
            num=num%5
    if 1<=num<=5:
        # if num==9:
        #     results+='IX'
        # if num==5:
        #     results+='V'
        if num==4:
            results+='IV'
        else:
            nb=num
            results+='I'*nb
    return results
        

tests=[
    (60, 'LX'),
    (3749, 'MMMDCCXLIX'),
    (3900, 'MMMCM'), 
    (3009, 'MMMIX'), 
    (58, 'LVIII'),
    (3000, 'MMM'), 
    (3049, 'MMMXLIX'), 
    (3090, 'MMMXC'),
]
for (s, expected_results) in tests: 
    res=intToRoman(s)
    print (res==expected_results, s, res, expected_results)
