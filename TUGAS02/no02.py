def calculateBMI(beratLB,tinggiINCH):
    bmi=(beratLB/tinggiINCH**2)*703
    
    if bmi<18.5:
        return f"Score {bmi:.2f}, Underweight"
    elif bmi < 25:
        return f"Score {bmi:.2f}, Normal"
    elif bmi < 30:
        return f"Score {bmi:.2f}, Overweight"
    else:
        return f"Score {bmi:.2f}, Obese"
beratLB = float(input('Masukkan berat (lb) => '))
tinggiINCH = float(input('Masukkan tinggi (inch) => '))

print(calculateBMI(beratLB,tinggiINCH))