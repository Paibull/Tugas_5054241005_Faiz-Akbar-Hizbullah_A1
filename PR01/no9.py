lengthYard=int(input('Masukkan panjang tanah (yard) =>'))*3
widthYard=int(input('Masukkan lebar tanah (yard) =>'))*3
lengthHouse=int(input('Masukkan panjang rumah (yard) =>'))*3
widthHouse=int(input('Masukkan lebar rumah (yard) =>'))*3

luasYard=lengthYard*widthYard # formula menentukan luas tanah
luasHouse=lengthHouse*widthHouse #formula menentukan luas bangunan
finalArea=luasYard-luasHouse # formula untuk menentukan sisa tanah 
cuttingTime=finalArea/2 # formula menentukan waktu memotong rumput

print(f'Untuk memotong rumput seluas {finalArea} ft\xB2 membutuhkan waktu selama {cuttingTime:.0f} detik')

