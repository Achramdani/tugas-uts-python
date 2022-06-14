class harga:
    def kontingen():
        bataku = (
           'Ananda coffe','list Menu Minuman Kopi','===============================' , 'A. Es Kopi Susu    : Rp 11.000', 'B. ES Kopi Coklat  : Rp 12.000' , 'C. ES Kopi Hitam   : Rp. 11.000','D. Ice Americano   : Rp. 14.000',' ================================')
        for i in bataku:
            print(i)

        pesan=str(input("masukkan list abjad menu kopi ="))
        jumlahpesan=int(input("masukkan jumlah pesanan ="))
        if pesan == "a":
           listnama= "ES Kopi Susu"
           harga=(11000*jumlahpesan)
           ppn= int(harga * 0.1)
           if jumlahpesan >= 5:
              diskon = int(harga*0.2)
              totalharga=int(harga-diskon+ppn)
           else:
              diskon =(0)
              totalharga=int(harga+ppn)
        elif pesan == "b":
            listnama= "ES Kopi Coklat"
            harga = (12000*jumlahpesan)
            ppn = int(harga * 0.1)
            if jumlahpesan >= 5:
               diskon = int(harga * 0.2)
               totalharga =int(harga-diskon+ppn)
            else:
                diskon =(0)
                totalharga=int(harga+ppn)
        elif pesan == "c":
            listnama= "ES Kopi hitam"
            harga=int(11000*jumlahpesan)
            ppn = int(harga * 0.1)
            diskon=0
            totalharga=int(harga+ppn)
        elif pesan == "d":
            listnama= "ES Americano"
            harga=int(14000*jumlahpesan)
            ppn = int(harga * 0.1)
            diskon=0
            totalharga = int(harga+ppn)
        else:
            listnama = "_"
            harga = "_"
            ppn ="_"
            diskon = "_"
            totalharga = "_"
            pilihan=input("menu tidak tersedia, silahkan masukkan abjad yang tersedia silahkan ulangi kembali Y/N =")

        print("---------------------")
        print("Ananda Coffe")
        print("---------------------")
        print("Menu :",listnama)
        print("Jumlah Pesan :", jumlahpesan)
        print("Harga :", harga)
        print("Diskon :", diskon)
        print("PPN :", ppn)
        print("---------------------")
        print("Jumlah Bayar :", totalharga)
        print("---------------------")
        pilihan=input("apakah anda ingin order kembali Y/N =")

x = harga
x.kontingen()

