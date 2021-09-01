def copy_string(x,y):
    if len(y)==0:
        return x
    else:
        c=copy_string(x,y[1:-1])
        print(y[1:-1])
        return c

x=input()
y=input()
print(copy_string(x,y))