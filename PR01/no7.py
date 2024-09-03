energiPerBarrel=5800000 
gallonPerBarrel=42

gallon=int(input('Berapa galon oli yang terbakar =>'))
effisiensi=int(input('Berapa efisiensi sistem pemanas rumah (%)=>'))

effisiensi/=100 # mengubah persenan menjadi bentuk desimal
BTU=((gallon/gallonPerBarrel)*energiPerBarrel)*effisiensi #formula menentukan BTU

print(f'Panas yang disalurkan adalah {BTU:.2f} BTU')
