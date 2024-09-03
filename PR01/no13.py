kapasitasSesi = 30

jumlahSiswa=int(input('Masukkan jumlah siswa =>'))

jumlahSesi=jumlahSiswa/kapasitasSesi # formula menentukan jumlah sesi
sisaSiswa=jumlahSiswa%kapasitasSesi # formula menentukan sisa siswa yang perlu penambahan sesi
if(sisaSiswa>0): 
    jumlahSesi+=1 # penambahan sesi karena terdapat siswa yang tersisa
    
print(f'Jumlah siswa yang terdaftar adalah {jumlahSiswa} siswa')
print(f'Jumlah sesi yang diperlukan adalah {int(jumlahSesi)} sesi')
print(f'Jumlah siswa yang tersisa adalah {sisaSiswa} siswa')
    
