def fun1():
    pilihan = input("Masukkan 'T' untuk True atau 'F' untuk False: ")
    return pilihan.upper() == 'T' 

def fun2():
    print("fun2 executed")
    return True

print("Testing &&")
if fun1() and fun2():
    print("Test of && complete")

print("Testing ||")
if fun1() or fun2():
    print("Test of || complete")
