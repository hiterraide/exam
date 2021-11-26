abc = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
zxc = [abc.values()]
for i in abc.values():
    if i%2==0:
        i='even'
    else:
        i='odd' 
    print(i)
