

def myAtoi(s: str) -> int:
    results=''
    # has_leading_sign=False
    for _char in s: 
        if _char==' ': 
            continue
        # if _char=='-': 
        #     has_leading_sign=True
        if _char in ['-','0','1','2','3','4','5','6','7','8','9']: 
            if _char =='-' and len(results)==0:
                results+=_char
            elif _char=='-': 
                break
            else:
                results+=_char
        else: 
            if results=='': 
                return 0
            else:
                break
    final_result=int(results)
    if final_result< -1*2**31: 
        return -1*2**31
    elif final_result> 2**31-1: 
        return 2**31-1  
    return int(results)

tests=[
    (' -42', -42), 
    (' -042', -42)]
for (str, expected_output) in tests: 
    print(str, myAtoi(str), expected_output)