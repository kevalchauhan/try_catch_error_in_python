while True:
    print('press k to exit')
    a = input("enter a number")
    if a == 'k':
        break
    try:
        a = int(a)
        if a > 6:
            print("you enter higher number")
    except Exception as e:
        print(e)
print('thanks for palying')
