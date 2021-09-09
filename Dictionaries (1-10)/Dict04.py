def func_remove_items(cart):
    cart={'Shirt': 1,
    'Socks': 4,
    'Bag': 1,
    'Notebook': 6,
    'Telephone': 1,
    'Pencil': 4,
    'Pen': 2
    }
    cart.pop('Telephone')
    return cart
a=func_remove_items({})
print(a)