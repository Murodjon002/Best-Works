def odd_item_list(numbers):
    k=0
    sam=[]
    while len(numbers)>k:
        sam.append(numbers[k])
        k+=1

    return sam[1::2]
print(odd_item_list(input()))