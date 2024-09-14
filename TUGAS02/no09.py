tarifWeekdays = 39.99 # Tarif weekdays per menit dalam 600 menit (sen)
extraWeekdays = 0.4 # Tarif extra weekdays 0.4 sen/menit
tarifNight = 0 # Tarif malam gratis
tarifWeekend = 0 # Tarif weekend gratis
tax = 0.0525 # Pajak

print('ChatFlow Wireless 45')
weekDays = int(input('Masukkan jumlah menit hari kerja => '))
night = int(input('Masukkan jumlah menit malam => '))
weekEnd = int(input('Masukkan jumlah menit akhir pekan => '))

# Pengecekan jumlah menit dalam weekdays
if weekDays < 600:
    subWeekdays = tarifWeekdays
else:
    tarifWeekdays = tarifWeekdays + ((weekDays-600) * extraWeekdays)
    subWeekdays = tarifWeekdays


# Total menit
totMinute = weekDays + night + weekEnd

# Tagihan sebelum pajak
tagihan = subWeekdays

# Rata rata biaya per menit
avgTagihan = tagihan / max(1,totMinute) # max() untuk menghindari pembagian oleh 0

# Total Tagihan                                  
finaltagihan = tagihan + (tagihan*tax)

# Output
print(f'Jumlah menit hari kerja : {weekDays}')
print(f'Jumlah menit malam : {night}')
print(f'Jumlah menit akhir pekan : {weekEnd}')
print(f'Tagihan sebelum pajak : {tagihan}')
print(f'Biaya rata-rata per menit : {avgTagihan:.2f}')
print(f'Pajak : {tax*tagihan:.2f}')
print(f'Total tagihan : {finaltagihan:.2f}')
