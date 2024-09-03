m=int(input('Masukkan nilai m =>'))
n=int(input('Masukkan nilai n =>'))

if m <= n: # pengecekan m > n
    print('Nilai m harus lebih besar daripada n')
    
else:
    side1=(m**2)-(n**2) # formula untuk mencari panjang sisi 1 
    side2=2*(m*n)  # formula untuk mencari panjang sisi 2  
    hypotenuse=(m**2)+(n**2) # formula untuk mencari panjang sisi miring

print(f'{side1},{side2},{hypotenuse}')




