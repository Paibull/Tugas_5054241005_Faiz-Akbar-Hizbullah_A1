def inputUser():
    return int(input('Enter number of Miles >> '))

def firstService(distance): 
    if 1500 < distance <= 3000:
        return "Vehicle must be service"
    else:
        return "The vehicle is not yet due for service."
         
def secondService():
    if 3001 < distance <= 4500:
        return "Vehicle must be service"
    else:
        return "The vehicle is not yet due for service."


try:
    print('(1) First Free Service')
    print('(2) Second Free Service')

    option = int(input('Enter the Free Service number >> '))
    
    if option == 1:
        distance = inputUser()
        print(firstService(distance))
    elif option == 2:
        distance = inputUser()
        print(secondService(distance))
    else:
        raise ValueError("Masukkan input antara 1 atau 2")
    
except ValueError as e:
    print(f'Kesalahan : {e}')

    


