# Mengecek tahun kabisat
def kabisat(tahun):
    if tahun % 400 == 0: # Habis dibagi 400 = kabisat
        return 1 
    elif tahun % 100 == 0: # Habis dibagi 100 != kabisat
        return 0
    elif tahun % 4 == 0: # Habis dibagi 4 = kabisat
        return 1
    else: 
        return 0
    
# Fungsi kalkulasi hari
def calculateHari(hari, bulan, tahun):
    # Non kabisat
    hariTiapBulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Jika kabisat, Februari diganti dari 28 ke 29
    if kabisat(tahun):
        hariTiapBulan[1] = 29
    
    # Hitung total hari 
    totHari = sum(hariTiapBulan[:bulan-1]) + hari
    return totHari

# Input 
hari = int(input("Masukkan hari (1-31): "))
bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

# Output
hasil = calculateHari(hari, bulan, tahun)
print(f"Tanggal {hari}/{bulan}/{tahun} adalah hari ke-{hasil} dalam setahun.")
