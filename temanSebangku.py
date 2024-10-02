n, r, c  = map(int, input().split())

kelas = {}
for i in range(n):
    index, posx, posy = map(int,input().split())
    kelas.update({index : [posx, posy]})

hasil = []

for siswa in kelas:
    flag = False
    pos_siswa = kelas[siswa]
    for kawan in kelas:
        pos_kawan = kelas[kawan]
        if siswa != kawan:   
            if pos_siswa[0] == pos_kawan[0]:
                if pos_siswa[1] == (pos_kawan[1] + 1) or pos_siswa[1] == (pos_kawan[1] - 1):
                    hasil.append(kawan)
                    flag = True
                    break
    if flag == False:
        hasil.append(0)

for i in hasil:
    print(i)