muffins = 10
cupcakes = 10
Buying = input("Do you want to buy a muffin or a cupcake?")


while Buying != '0':
    if Buying == 'muffin' and muffins > 0:
        muffins = muffins - 1
        if Buying == 'muffin' and muffins == 0:
            print("muffins out of stock")
    if Buying == 'cupcake' and cupcakes > 0:
        cupcakes = cupcakes - 1
        if Buying == 'cupcake' and cupcakes == 0:
            print("cupcakes out of stock")
    Buying = input("Do you want to buy a muffin or a cupcake?")
print("muffins", muffins, "cupcakes", cupcakes)
