b = 99
while b > 0:
    if b == 2:
        print('%d bottles of beer on the wall, %d bottles of beer; take one down, pass it around, %d bottle of beer on the wall\n' % (b, b, b-1))
        b -= 1
    else:
        print('%d bottles of beer on the wall, %d bottles of beer; take one down, pass it around, %d bottles of beer on the wall\n' % (b, b, b - 1))
        b -= 1
