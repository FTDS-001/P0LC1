import pandas as pd
df = pd.read_csv(NMC1-9)

def conv_ohm(V,I):
    convert_ohm = V/I
    return convert_ohm

def conv_watt(V,I):
    convert_watt = V * I
    retun convert_watt

    loop = True
    while loop
        menu ="""
    (1)'Hambatan dalam satuan OHM'
    (2)'Daya dalam watt'

    Pilihan? (1-2): """
        try:
            choice=input(menu)
        except :
            choice = 0
        
        if choice not in range(1,2):
        print "Pilih 1, 2."
        print

         elif choice in range(1,2):
        if choice == 1:
            print
            print "Menghitung V = R x I"
            R = input(" Input Resistansi = ")
            I = input(" Input Arus = ")
            V = VIR(0, I, R)
            print " Voltage =", V.calcV()
 
        elif choice == 2:
            print
            print "Menghitung I = V / R"
            V = input(" Input Voltage = ")
            R = input(" Input Resistansi = ")
            I = VIR(V, 0, R)
            print " Current =", I.calcI()
 
        else:
            print('salah input')
 
        raw_input('Tekan Enter untuk melanjutkan...')
 
    else :
        loop = False 

        print ("Selesai")

    

    