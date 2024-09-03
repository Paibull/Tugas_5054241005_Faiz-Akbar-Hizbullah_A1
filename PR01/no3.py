def kalkulasiTemp(t): #fungsi temperatur freezer
    return (4*t**2)/(t+2)-20
    
t = list(map(float,input('Masukkan lama waktu dengan format \'j m\'(ex : "2 30")=> ').split())) #input waktu
jam = t[0] #karakter pertama dalam list 't' sebagai jam
menit = t[1] #karakter kedua dalam lits 't' sebagai menit
jam = jam+(menit/60) #formula mengubah jam & menit menjadi jam desimal

print(f'Estimasi suhu setelah {jam} jam freezer mati adalah {kalkulasiTemp(jam):.2f}\u00B0C') #output hasil kalkulasi temperatur