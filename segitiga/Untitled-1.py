rafloat = int(input("jari-jari = "))

if rafloat % 7 == 0:
    print(f"true => luas = 22/7 x r kuadrat")
    luas = 22/7 * rafloat * rafloat
    print(f"hasil luasnya = {luas}")
else:
    print(f"false => luas = 3.14 x r kuadrat")
    luas = 3.14 * rafloat * rafloat
    print(f"hasil luasnya = {luas}")