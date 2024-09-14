def rotate_kittens(number, slice, rotations, index):
    # Inisialisasi list kucing
    kittens = list(number)
    
    # Lakukan rotasi sebanyak `rotations` kali
    for i in range(rotations):
        # Ambil 3 kucing pertama
        first_part = kittens[-slice:]
        # Ambil sisa kucing
        second_part = kittens[:-slice]
        # Gabungkan dengan 3 kucing pertama di belakang
        kittens = first_part + second_part
    
    # Ambil angka pada indeks yang diminta
    result = [kittens[i] for i in index]
    return result

# Input
number = str(input('Masukkan angka => '))
slice = int(input('Masukkan jumlah angka yang ingin di slice => ')) 
rotations = int(input('Masukkan jumlah rotasi => '))
index = list(map(int,input('Masukkan index yang ingin dihasilkan dari proses slice dan rotasi => ').split()))

# Hasil
result = ' '.join(rotate_kittens(number, slice, rotations, index)) # Agar keluaran tidak ada kurung siku list
result1 = rotate_kittens(number, slice, rotations, index)
print(result)
print(result1)