print("")
print("=================== BAZAAR KERAMIK HSI ===================")
print("")
customer = input("Nama Customer\t\t: ")
sales = input("Nama SPG/SPM\t\t: ")
date = input("Date [D for Default]\t: ")

nama_barang = []
harga_barang = []
jumlah_set = []
jumlah_pcs = []
subtotal = []
paket = []
pembelian = 0
total_bayar_awal = 0
total_pcs = 0
total_set = 0


x = 1
while x == 1:
    print("")
    pembelian += 1
    print("Barang Ke\t:", pembelian)
    nama_barang.append(input("Nama Barang\t: "))
    jumlah_set.append(int(input("Jumlah Set\t: ")))
    jumlah_pcs.append(int(input("Jumlah Pcs\t: ")))
    harga_barang.append(int(input("Harga Barang\t: ")))

    
    lanjut = input("Lanjut Y/n: ")
    if lanjut == "N" or lanjut == "n":
        x = 0
    else:
        print("")

for i in range(pembelian):
    jumlah = harga_barang[i] * jumlah_set[i]
    subtotal.append(jumlah)

for i in range(pembelian):
    set = jumlah_pcs[i] / jumlah_set[i]
    paket.append(set)

for i in subtotal:
    total_bayar_awal += i

for i in jumlah_pcs:
    total_pcs += i

for i in jumlah_set:
    total_set += i

deposit = 3000000
total_bayar_akhir = total_bayar_awal - deposit

def struk():
    
    print("\n")
    print("PT. Haeng Nam Sejahtera Indonesia".center(60))
    print("Jl. Mercedez Benz Desa Cicadas Kec Gunung Putri".center(60))
    print("Kabupaten Bogor - Jawa Barat Indonesia".center(60))
    print("Telp 021 867 1739 - Fax 021 867 0553".center(60))
    print("____________________________________________________________")
    print("")
    print("Customer\t: ", customer)
    print("SPB/SPG \t: ", sales)

    if date == "D" or date == "d":
        import datetime
        x = datetime.datetime.now()
        print("Date \t \t: ", x.strftime("%a %d %b %G %X"))
    else:
        print("Date \t \t: ", date)
    print("____________________________________________________________")
    print("")
    print("No.\tNama Barang\t\tSet\tQty\tSub Total")
    print("")
    for i in range(pembelian):
        
        print("\t%s"% nama_barang[i])  
        print("%i.\tRp.%i /%ipcs\t\t%i\t%i \tRp.%i"%(i+1, harga_barang[i], paket[i], jumlah_set[i], jumlah_pcs[i], subtotal[i]))
        print("____________________________________________________________")
        print("")
    print("Total Keseluruhan  \t \t%i\t%i\tRp.%i"%(total_set, total_pcs,total_bayar_awal))
    print("Total Bayar\t \t\t\t \tRp.%i"% deposit)
    print("\t\t\t\t\t\t___________-")
    print("")
    print("\t\t\t\t\t \tRp.%i"% total_bayar_akhir)
    print("\n")
    print("Terima Kasih".center(60))
    print("")
    print("Untuk BKP, Harga termasuk PPN") 
    print("Barang yang sudah di beli tidak dapat DITUKAR /")
    print("DIKEMBALIKAN")
    print("")
    print("Semoga Harimu Menyenangkan")
    print("Selamat Datang Kembali")
    print("")

struk()

x = 1
while x == 1:
    print("\n")
    print("====== Menu Lanjutan =======".center(60))
    print("| Tekan 1 untuk mengubah   |".center(60))
    print("| Tekan 2 untuk menambah   |".center(60))
    print("| Tekan 3 untuk menghapus  |".center(60))
    print("| Tekan 4 untuk selesai    |".center(60))
    print("============================".center(60))

    print("")
    nomor = int(input("Pilih nomor \t[1/2/3/4]: "))
    if nomor == 1:
        x = 2
        while x == 2:
            print("")
            print("Tekan 0 untuk mengubah Nama & Tgl")
            nomor_ubah = int(input("Nomor yang ingin Anda Ubah: "))
            if nomor_ubah > pembelian:
                print("Nomor Tidak ada dalam List")
                x = 2
            elif nomor_ubah == 0:
                x = 2
                while x == 2:

                    print("")
                    print("================ BAZAAR KERAMIK HSI ================")
                    print("")
                    print("")
                    customer1 = input("Nama Customer [D untuk Default]\t: ")
                    if customer1 == "D" or customer1 == "d":
                        print("")
                    else:
                        customer = customer1

                    sales1 = input("Nama SPG/SPM  [D untuk Default]\t: ")
                    if sales1 == "D" or sales1 == "d":
                        print("")
                    else:
                        sales = sales1

                    date1 = input("Date [D untuk Default]  \t: ")
                    if date1 == "D" or date1 == "d":
                        print("")
                    else:
                        date = date1

                    struk()
                    print("")
                    lanjut = input("Masih ingin Mengubah Nama & Tanggal? [Y/n]: ")
                    if lanjut == "N" or lanjut == "n":
                        x = 1
                    else:
                        print("") 
            else:
                print("")
                print("Barang Ke\t:", nomor_ubah)
                nama_barang[nomor_ubah - 1] = input("Nama Barang\t: ")
                jumlah_set[nomor_ubah -1] = int(input("Jumlah Set\t: "))
                jumlah_pcs[nomor_ubah -1] = int(input("Jumlah Pcs\t: "))
                harga_barang[nomor_ubah -1] = int(input("Harga Barang\t: "))


                total_bayar_awal = 0
                total_pcs = 0
                total_set = 0  
                
                jumlah = harga_barang[nomor_ubah -1] * jumlah_set[nomor_ubah -1]
                subtotal[nomor_ubah - 1] = jumlah

                set = jumlah_pcs[nomor_ubah -1] / jumlah_set[nomor_ubah -1]
                paket[nomor_ubah - 1] = set

                for i in subtotal:
                    total_bayar_awal += i

                for i in jumlah_pcs:
                    total_pcs += i

                for i in jumlah_set:
                    total_set += i

                deposit = 3000000
                total_bayar_akhir = total_bayar_awal - deposit

                struk()
                print("")
                lanjut = input("Masih ingin Mengubah? [Y/n]: ")
                if lanjut == "N" or lanjut == "n":
                    x = 1
                else:
                    print("") 

    elif nomor == 2:
        x = 2
        while x == 2:
            print("")
            pembelian += 1
            print("Barang Ke\t:", pembelian)
            nama_barang.append(input("Nama Barang\t: "))
            jumlah_set.append(int(input("Jumlah Set\t: ")))
            jumlah_pcs.append(int(input("Jumlah Pcs\t: ")))
            harga_barang.append(int(input("Harga Barang\t: ")))

            jumlah = harga_barang[pembelian - 1] * jumlah_set[pembelian - 1]
            subtotal.append(jumlah)

            set = jumlah_pcs[pembelian - 1] / jumlah_set[pembelian - 1]
            paket.append(set)

            total_bayar_awal += subtotal[pembelian - 1]
            total_pcs += jumlah_pcs[pembelian - 1]
            total_set += jumlah_set[pembelian - 1]

            deposit = 3000000
            total_bayar_akhir = total_bayar_awal - deposit  

            struk() 
            print("")
            lanjut = input("Masih ingin Menambahkan? [Y/n]: ")
            if lanjut == "N" or lanjut == "n":
                x = 1
            else:
                print("")

    elif nomor == 3:
        x = 2
        while x == 2:
            print("")
            print("Tekan 0 untuk menghapus semua")
            nomor_hapus = int(input("Nomor yang ingin Anda Hapus?: "))
            if nomor_hapus > pembelian:
                print("Nomor Tidak ada dalam List")
                x = 2
            elif nomor_hapus == 0:
                print("")
                nama_barang = []
                harga_barang = []
                jumlah_set = []
                jumlah_pcs = []
                subtotal = []
                paket = []
                pembelian = 0
                total_bayar_awal = 0
                total_pcs = 0
                total_set = 0

                total_bayar_awal = 0
                total_pcs = 0
                total_set = 0  
                
                for i in subtotal:
                    total_bayar_awal += i

                for i in jumlah_pcs:
                    total_pcs += i

                for i in jumlah_set:
                    total_set += i

                deposit = 3000000
                total_bayar_akhir = total_bayar_awal - deposit

                struk()
                print("")
                lanjut = input("Masih ingin Menghapus? [Y/n]: ")
                if lanjut == "N" or lanjut == "n":
                    x = 1
                else:
                    print("")

            else:
                print("")
                nama_barang.pop(nomor_hapus - 1)
                jumlah_set.pop(nomor_hapus - 1)
                jumlah_pcs.pop(nomor_hapus - 1)
                harga_barang.pop(nomor_hapus - 1)
                subtotal.pop(nomor_hapus - 1)
                paket.pop(nomor_hapus - 1)
                pembelian -= 1

                total_bayar_awal = 0
                total_pcs = 0
                total_set = 0  
                
                for i in subtotal:
                    total_bayar_awal += i

                for i in jumlah_pcs:
                    total_pcs += i

                for i in jumlah_set:
                    total_set += i

                deposit = 3000000
                total_bayar_akhir = total_bayar_awal - deposit

                struk()
                print("")
                lanjut = input("Masih ingin Menghapus? [Y/n]: ")
                if lanjut == "N" or lanjut == "n":
                    x = 1
                else:
                    print("") 
    
    elif nomor == 4:
        x = 0
        struk()
        print("\n")
    else:
        print("")
        print("Kode tidak ada didalam menu")