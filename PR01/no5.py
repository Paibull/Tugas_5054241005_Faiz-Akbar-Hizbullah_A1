volume = int(input('Volume to be infused (ml) => ')) #input volume infus
menit = int(input('Minutes over which to infuse => ')) #input lama infus habis

rate = (volume/menit)*60 #formula rate infus dalam ml/hr

print(f'VTBI : {volume}') #output volume infus
print(f'Rate : {int(rate)} ml/hr') #output rate infus