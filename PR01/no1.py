print('TAXI FARE CALCULATOR')
jarakAwal = float(input('Enter beginning odometer reading=> ')) #input jarak awal
jarakAkhir = float(input('Enter beginning odometer reading=> ')) #input jarak akhir

jarak = jarakAkhir - jarakAwal #formula menentukan total jarak
argo = jarak * 1.50 #formula menentukan argo

print('you travel distance of %.2f miles. At $1.50 per mile,' % jarak) #output total jarak
print(f'your fare is {argo:.2f}') #output total argo
