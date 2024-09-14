# Fungsi untuk memeriksa apakah data berada dalam x% dari nilai referensi
def within_x_percent(ref, data, x): 
    lower_bound = ref - (x / 100 * ref) # Batas bawah 
    upper_bound = ref + (x / 100 * ref) # Batas atas
    return lower_bound <= data <= upper_bound # jika data/input suhu yang dimasukkan sesuai, maka mengembalikan nilai True

# Titik didih normal dari beberapa zat
boiling_points = {
    "Air": 100,
    "Merkuri": 357,
    "Tembaga": 1187,
    "Perak": 2193,
    "Emas": 2660
}

def identify_substance(observed_boiling_point):
    for substance, normal_boiling_point in boiling_points.items(): # Mengakses tiap unsur, titik didih nomal dalam dict boiling_points
        # Mengecek input titik didih, apakah ada yang sesuai dengan data boiling_points dengan toleransi 5%
        if within_x_percent(normal_boiling_point, observed_boiling_point, 5):
            return substance # Mengembalikan nilai substance yang sesuai
    return "Zat tidak dikenal" # Jika tidak ada substance yang cocok

# Meminta input dari pengguna
try:
    observed_boiling_point = float(input("Masukkan titik didih yang diamati (°C) => "))

    # Identifikasi zat berdasarkan titik didih yang diamati
    result = identify_substance(observed_boiling_point)

    # Menampilkan hasil
    print(f"Hasil identifikasi: {result}")
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")


    