def lampu_lalu_lintas(M, N, T):
    # Durasi untuk setiap warna lampu
    durasi_merah = 20
    durasi_kuning = 5
    durasi_hijau = 60
    waktu_dalam_siklus = durasi_merah + durasi_kuning + durasi_hijau
    
    # M = 12
    # N = 12
    # T = 200
    
    # Hitung waktu yang tersisa dalam satu siklus penuh
    total_siklus = T // waktu_dalam_siklus # 2 siklus
    
    if total_siklus > 1:  
        sub_waktu_siklus = T*(durasi_merah+durasi_kuning+durasi_hijau) # 170 detik
        sisa_durasi = T % waktu_dalam_siklus # 30 detik
        sisa_lampu_hijau  = abs(sisa_durasi - (durasi_merah+durasi_kuning)) # 5 detik
        lama_lampu_hijau = (durasi_hijau*total_siklus) + sisa_lampu_hijau # 125
    else:
        lama_lampu_hijau = durasi_hijau
  
    mobil_lewat = lama_lampu_hijau // 5  # Setiap 5 detik, satu mobil bisa lewat
    
    if mobil_lewat > M + 1:
        sisa_mobil = (M + N + 1) - mobil_lewat
        return "YES!", sisa_mobil
    elif mobil_lewat == M + 1:
        sisa_mobil = N 
        return "YES!", sisa_mobil
    else:
        # Jika tidak semua mobil bisa lewat
        sisa_mobil = (M + N + 1) - mobil_lewat
        return "NO!", sisa_mobil

# Input dari pengguna
M, N, T = map(int, input("Masukkan jumlah mobil di depan, mobil di belakang, dan waktu yang telah berlalu: ").split())

# Panggil fungsi dan cetak hasilnya
hasil, sisa_mobil = lampu_lalu_lintas(M, N, T)
print(f"{hasil} {sisa_mobil}")
