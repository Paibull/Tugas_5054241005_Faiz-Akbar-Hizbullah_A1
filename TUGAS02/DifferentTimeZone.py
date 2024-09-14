from datetime import datetime, timedelta

# Fungsi untuk menghitung selisih waktu
def hitung_waktu_tunggu(waktu_mulai, waktu_sekarang):
    # Konversi string waktu ke objek datetime
    format_waktu = "%H:%M:%S"
    
    # Konversi waktu mulai siaran (dalam GMT+2 ke GMT+7)
    waktu_mulai_gmt7 = datetime.strptime(waktu_mulai, format_waktu) + timedelta(hours=5)
    #Mengubah var waktu_mulai menjadi format_waktu dan jam ditambah 5
    
    # Konversi waktu sekarang (sudah dalam GMT+7)
    waktu_sekarang = datetime.strptime(waktu_sekarang, format_waktu)

    # Hitung selisih waktu
    selisih = waktu_mulai_gmt7 - waktu_sekarang
    
    # Jika acara sudah lewat, tampilkan pesan
    if selisih.total_seconds() <= 0:
        return "See you on the next Pear Event!"
    
    # Konversi selisih ke format jam:menit:detik
    jam, sisa_detik = divmod(int(selisih.total_seconds()), 3600)
    menit, detik = divmod(sisa_detik, 60)
    
    return f"{jam:02}:{menit:02}:{detik:02}"

# Input dari pengguna
waktu_mulai = input("Masukkan waktu mulai siaran (HH:MM:SS): ")
waktu_sekarang = input("Masukkan waktu sekarang (HH:MM:SS): ")

# Hitung dan tampilkan hasil
hasil = hitung_waktu_tunggu(waktu_mulai, waktu_sekarang)
print(hasil)
