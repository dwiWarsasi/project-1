from . import Operasi


# 1. Cek stok (seluruh stok tersedia)
def cekStok_console():
    data_file = Operasi.cekStok()

    index = "No"
    kode = "Kode"
    nama = "Nama"
    bahan = "Bahan"
    stok = "Stok"
    lokasi = "Lokasi Gudang"

    # Header
    print("\n"+"="*115)
    print(f"{index:4} | {kode:10} | {nama:25} | {bahan:25} | {stok:20} |{lokasi:15} ")
    print("="*115)

    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",") #karena kalau langsung print(data_file) = data masih rancu belum dipisahkan jadi beberapa string
        pk = data_break[0]
        date_add = data_break[1]
        kode = data_break[2]
        nama = data_break[3]
        bahan = data_break[4]
        stok = data_break[5]
        lokasi = data_break[6]
        print(f"{index+1:4}.| {kode:10} | {nama:25} | {bahan:25} | {stok:20} | {lokasi:14} ")

    # Footer
    print("="*115+"\n")



# 2. Tambah item 
def tambahItem_console():
    print("\n"+"="*115+"\n")
    print("silahkan tambah stok barang".upper()+"\n")
    kode = input("Kode : ")
    nama = input("Nama : ")
    bahan = input("Jenis Bahan : ")
    while(True):
        try:
            stok = int(input("Jumlah Stok : "))
            break
        except:
            print("Stok harus berupa angka, silahkan masukkan stok yang benar!")
    lokasi = input("Lokasi Gudang : ")

    Operasi.tambahItem(kode,nama,bahan,stok,lokasi)
    print("\nBerikut adalah stok yang ada di gudang setelah ditambahkan item baru :")
    cekStok_console() #data akan bergabung bersama dnegan data lainnya, karena ngeread data di cekStok_console()
    # langsung ter update di stok karena 'a', langsung menambah list setelahnya. begituuuu





# 3. Update stok
def update_console():
    cekStok_console() #menampilkan seluruh stok (No.1)
    while(True):
        print("Silahkan pilih No.item yang ingin di update")
        no_item = int(input("Pilih No. item yang akan di update : "))
        data_item = Operasi.cekStok(index=no_item) #index=keyword, no_item=argument

        if data_item:
            break
        else:
            print("Nomor tidak valid, silahkan masukkan lagi")

    data_break = data_item.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    kode = data_break[2]
    nama = data_break[3]
    bahan = data_break[4]
    stok = data_break[5]
    lokasi = data_break[6][:-1] # -1 karena pada data.txt belakangnya ada \n. jadi diread hanya data pertama sampai data -1 saja
    
    while(True):
        # data yang ingin di update
        print("\n"+"="*115)
        print("Silahkan pilih data apa yang ingin anda update")
        print(f"1. Kode   : {kode}")
        print(f"2. nama   : {nama}")
        print(f"3. bahan  : {bahan}")
        print(f"4. stok   : {stok}")
        print(f"5. lokasi : {lokasi}")

        # memilih mode untuk update
        user_option = input("Pilih data (1-5) : ")
        print("\n"+"="*115)

        match user_option:
            case "1": kode = input("Kode     : ")
            case "2": nama = input("nama     : ")
            case "3": bahan = input("bahan    : ")
            case "4":
                while(True):
                    try:
                        stok = int(input("Jumlah Stok : "))
                        break
                    except:
                        print("Stok harus berupa angka, silahkan masukkan stok yang benar!")
            case "5": lokasi = input("lokasi  : ")
            case _: print("Index tidak sesuai")

        print("\nData berhasil di update :")
        print(f"1. Kode   : {kode}")
        print(f"2. nama   : {nama}")            
        print(f"3. bahan  : {bahan}")    # konfirmasi data sebelum di update
        print(f"4. stok   : {stok}")
        print(f"5. lokasi : {lokasi}")

        is_done = input("Apakah anda yakin data akan di update ? (y/n) : ")
        if(is_done == "y" or is_done == "Y"):
            break

    Operasi.update(no_item,pk,date_add,kode,nama,bahan,stok,lokasi)



# 4. Delete stok
def delete_console():
    cekStok_console()
    while(True):
        print("Silahkan pilih No. item yang ingin dihapus")
        no_item = int(input("Nomor item : "))
        data_item = Operasi.cekStok(index=no_item)

        if data_item:
            data_break = data_item.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            kode = data_break[2]
            nama = data_break[3]
            bahan = data_break[4]
            stok = data_break[5]
            lokasi = data_break[6]

            # data yang ingin dihapus
            print("\nData yang ingin anda hapus :")
            print(f"1. Kode   : {kode}")
            print(f"2. nama   : {nama}")
            print(f"3. bahan  : {bahan}")    #konfirmasi dulu sebelum data dihapus
            print(f"4. stok   : {stok}")
            print(f"5. lokasi : {lokasi}")
            is_done = input("Apakah anda yakin? (y/n) : ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_item)
                break
        else:
            print("Nomor tidak valid, silahkan masukkan kembali")
    print("Data telah berhasil dihapus")


