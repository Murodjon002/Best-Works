def func_digits_list(data):
    result=0
    for i in data.keys():
        if i=="Email":
            result="YES"
    if result!="YES":
        result='NO'

    return result
            
        
        
a=func_digits_list({"Name": "Jamol","Age": 21,"City": "Namangan","Job": "Driver","Phone": 998949876543})
print(a)