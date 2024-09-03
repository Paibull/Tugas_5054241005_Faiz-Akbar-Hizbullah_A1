tinggi = float(input('Masukkan tinggi bendungan (m) => ' )) #input tinggi bendungan
aliran = float(input('Masukkan aliran air (m\xB3/s) => ')) #input aliran bendungan

gravitasi = 9.8 #define gravitasi
efisiensi = 0.9 #define efisiensi

massa = aliran * 1000 #formula mengubah meter kubik ke kg
usaha = massa * gravitasi * tinggi #formula usaha
daya = (usaha * efisiensi)/1e6 #formula mengubah watt ke megawatt

print(f'Daya yang dihasilkan bendungan adalah sekitar {daya:.2f} MW') #output hasil prediksi