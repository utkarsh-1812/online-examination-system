
def decor(f):
    print('decor')
    def wrap(a, b):
        print('wrap')
        try:
            d=(f(a, b))
        except Exception as e: 
            d=(0,e)
        return d
    return wrap


@decor
def divide(a, b):
    return a/b


print(divide(2, 3), divide(9, 0))
