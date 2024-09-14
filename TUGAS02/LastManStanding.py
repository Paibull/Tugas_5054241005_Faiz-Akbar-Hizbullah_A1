def last_man_standing(N, C):
    # Jika sisa bola adalah kelipatan dari 4, maka pemain kedua akan menang
    if N % 3 == 0:
        if C == 1: # Lala
            print("Lala") # Menang
        else:
            print("Lili")
    else:
        if C == 1: # Lala
            print("Lili") # Menang
        else:
            print("Lala")

# Input data
N, C = map(int, input('').split())

# Panggil fungsi
last_man_standing(N, C)
