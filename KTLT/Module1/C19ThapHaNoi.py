def move(n,A,B,C):
    if n==1:
        print(f'Move {A} ==> {C}')
    else:
        move(n-1,A,C,B)
        print(f'Move {A} ==> {C}')
        move(n-1,B,A,C)

move(3,'A','B','C')
print('Chuyển với n=4: ')
move(4,'A','B','C')
