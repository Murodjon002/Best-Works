def func_data_list(data):
    data={"Name": "Jamol",
"Age": 21,
"City": "Namangan",
"Job": "Driver",
"Phone": 998949876543}
    list1=[]
    list1.append(data["Name"])
    list1.append(data["Phone"])
    list1.append(data["City"])
    
    return list1
a=func_data_list({})
print(a)