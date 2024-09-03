takeOffSpeed=float(input('Masukkan kecepatan takeoff pesawat (km/hr) =>'))
jarak=float(input('Masukkan jarak dari ketapel hingga pesawat takeoff (m) =>'))

speedms=takeOffSpeed*(1000/3600) # Mengubah dari km/h ke m/s
waktu=(2*jarak)/speedms
percepatan=speedms/waktu

print(f'Pesawat membutuhkan percepatan sebesar {percepatan:.2f} m/s\xb2 \nselama {waktu:.2f} s untuk mencapai kecepatan takeoff')

