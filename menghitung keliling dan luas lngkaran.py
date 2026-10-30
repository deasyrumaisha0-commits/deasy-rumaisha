print("--- program lingkaran ---")
print("pilih menu: ")
print("1. Hitung Keliling Lingkaran")
print("2. Hitung Luas Lingkaran")

pilihan = int(input("Masukan pilihan (1 atau 2): "))

if pilihan == 1:
    r = float(input("Masukan nilai r: "))
    keliling = 2 * 3.14 * r
    print(f"Keliling Lingkaran: {keliling:.2f}")
elif pilihan == 2:
    r = float(input("masukan nilai r: "))
    luas = 3.14 * (r**2)
    print(f"Luas Lingkaran: {luas:.2f}")
else:
    print("Pilihan tidak valid. Silahkan masukan angka 1 atau 2.")