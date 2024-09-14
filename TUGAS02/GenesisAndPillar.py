# Input
jumpAbility = int(input())  # Nilai maksimum lompatan B
pillars = list(map(int, input().split()))  # Jarak antara tiang-tiang

# Cek apakah semua jarak bisa dilompati
canJump = all(pilar <= jumpAbility for pilar in pillars) # Jika semua kondisi benar, mengembalikan nilai True

# Output hasil
if canJump:
    print("YES HE CAN")
else:
    print("NO HE CAN'T")
