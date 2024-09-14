def breadMachine():
    
    breadTime = {
        'W': {'kneading': 15, 'rising': 60, 'secondary_kneading': 18, 'secondary_rising': 20, 'shaping': 2, 'final_rising': 75, 'baking': 45, 'cooling': 30},
        'S': {'kneading': 20, 'rising': 60, 'secondary_kneading': 33, 'secondary_rising': 30, 'shaping': 2, 'final_rising': 75, 'baking': 35, 'cooling': 30} 
    }

    if type not in breadTime :
        print('Input salah')
        return
    
    # Mengakses key dalam Breadtime
    time = breadTime[type]
    
    # Size double
    if double:
        for step in time:
             if step != 'shaping':  # Karena nilai shaping sangat kecil/tidak berpengaruh
                time[step] = round(time[step] * 1.5) # Peningkatan waktu 50%
                
    # Tampilan instruksi (Input User)
    print(f"Selected Bread Type: {'White' if type == 'W' else 'Sweet'}")
    print(f"Double Loaf: {'Yes' if double else 'No'}")
    print(f"Manual Baking: {'Yes' if manual else 'No'}")
    
    # Tampilan instruksi
    print("\nBread Machine Instructions:")
    print(f"Primary kneading: {time['kneading']} mins")
    print(f"Primary rising: {time['rising']} mins")
    print(f"Secondary kneading: {time['secondary_kneading']} mins")
    print(f"Secondary rising: {time['secondary_rising']} mins")
    print(f"Loaf shaping: {time['shaping']} seconds")
    print(f"Final rising: {time['final_rising']} mins")
    
    # Pengecekan manual baking
    if manual:
        print("Stop after the loaf-shaping cycle.")
        print("Remove the dough for manual baking.")
    else:
        print(f"Baking: {time['baking']} mins")
    
    print(f"Cooling: {time['cooling']} mins")
        
# Input
type = input('Masukkan tipe roti =>').upper()
double = input('Apakah size double =>').lower().strip() == 'yes' # doubleInput akan bernilai true jika input = yes
manual = input('Apakah memanggangnya manual =>').lower().strip =='yes' # manualInput akan bernilai true jika input = yes
    
# Output
breadMachine(type,double,manual)    

    
