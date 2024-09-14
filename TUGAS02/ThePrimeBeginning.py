def cekPrima(number):
    
    if number <= 1:
        return False
    
    # Mencari pembagi number berdasarkan rentang akar kuadrat number
    for i in range(2, int(number**0.5) + 1):
        # Jika hasil number dibagi i habis, maka bukan prima
        if number % i == 0:
            return False
    return True

number = int(input('Masukkan angka => '))

if cekPrima(number):
    print(f"{number} adalah bilangan prima.")
else:
    print(f"{number} bukan bilangan prima.")
