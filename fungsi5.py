def luas_pergi (sisi):
    return sisi * sisi

#tidak menghasilkan output
luas_pergi(10)

#menghasilkan output
print('luas persegi dengan sisi 4 adalah:', luas_pergi(4))

#kita juga bisa simpan di dalam variabel
persegi_besar = luas_pergi(100)
persegi_kecil = luas_pergi(50)

print('total luas persegi besar dan kecil adalah:', persegi_besar + persegi_kecil)