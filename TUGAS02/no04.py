print('O = Orange\nB = Brown\nY = Yellow\nG = Green')
warna = input('Masukkan huruf pertama dari warna tabung gas =>').upper()

list = {
        'O': 'ammonia',
        'B': 'carbon monoxide',
        'Y': 'hydrogen',
        'G': 'oxygen'
    }
if warna in list:
    print(f"Tabung gas berwarna {warna.upper()} berisi {list[warna]}.")
else:
    print("Warna tidak dikenali atau tidak valid.")