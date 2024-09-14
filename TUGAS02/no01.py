SALESTAX = 0.05 

# pembeli student
def studentBuyer(totPurchase):
    discount = 0.20
    totDiscount = totPurchase*discount
    afterDiscount = totPurchase-totDiscount
    tax = (totPurchase-totDiscount)*SALESTAX
    total = totPurchase-totDiscount-tax
    print(f'Total belanja : ${totPurchase:.2f}')
    print(f'Diskon siswa (20%) : ${totDiscount:.2f}')
    print(f'Total diskon : ${afterDiscount:.2f}')
    print(f'Total pajak (5%) : ${tax:.2f}')
    print(f'Total : ${total:.2f}')
#pembeli nonstudent    
def nonstudentBuyer(totPurchase):
    discount = 0
    totDiscount = totPurchase*discount
    afterDiscount = totPurchase-totDiscount
    tax = (totPurchase-totDiscount)*SALESTAX
    total = totPurchase-totDiscount-tax
    print(f'Total belanja : ${totPurchase:.2f}')
    print(f'Diskon siswa (20%) : ${totDiscount:.2f}')
    print(f'Total diskon : ${afterDiscount:.2f}')
    print(f'Total pajak (5%) : ${tax:.2f}')
    print(f'Total : ${total:.2f}')
# input   
totPurchase = float(input('Masukkan total belanja => '))
recogBuyer = input('apakah pembeli seorang siswa (y/n) => ')

#checking
match recogBuyer:
    case 'y'|'Y':
        studentBuyer(totPurchase)
    case 'n'|'N':
        nonstudentBuyer(totPurchase)
    case _:
        print("Input tidak valid. Masukkan hanya 'y', 'Y', 'n', atau 'N'")
    