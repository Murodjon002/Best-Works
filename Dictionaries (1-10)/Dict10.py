def func_digits_list(oldest):
    maxoldest=-1
    for i in oldest.values():
        if i>maxoldest:
            maxoldest=i
    return maxoldest


a=func_digits_list({"Komil": 71,
"Ilhom": 45,
"Rustam": 151,
"Sharof": 29})
print((a))