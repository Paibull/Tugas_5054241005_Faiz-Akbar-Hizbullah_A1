def cekData(data):
    if 0.0 <= data <= 1.0:
        return 250
    elif 1.0 < data <= 2.0:
        return 500
    elif 2.0 < data <= 5.0:
        return 1000
    elif 5.0 < data <= 10.0:
        return 1500
    elif data > 10.0:
        return 2000
    else:
        return None 

try:
    data = float(input("Masukkan jumlah data yang digunakan (dalam GB) => "))
    
    biaya = cekData(data)

    if biaya is None:
        print("Data yang dimasukkan tidak valid. Harap masukkan jumlah data yang valid")
    else:
        print(f"Total biaya yang harus dibayar : {biaya}")

except ValueError:
    print("Masukkan nilai numerik yang valid untuk jumlah data")
