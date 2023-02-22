from time import time
from . import Database
from .Util import random_string
import time
import os


# Create database
def create_first_data():
    kode = input("Kode : ")
    nama = input("Nama : ")
    bahan = input("Jenis Bahan : ")
    stok = int(input("Jumlah Stok : "))
    lokasi = input("Lokasi Gudang : ")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(4)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M%z",time.gmtime())
    data["kode"] = kode + Database.TEMPLATE["kode"]
    data["nama"] = nama + Database.TEMPLATE["nama"]
    data["bahan"] = bahan + Database.TEMPLATE["bahan"]
    data["stok"] = str(stok)
    data["lokasi"] = lokasi + Database.TEMPLATE["lokasi"]+"\n"

    data_str = f'{data["pk"]},{data["date_add"]},{data["kode"]},{data["nama"]},{data["bahan"]},{data["stok"]},{data["lokasi"]}'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data gagal dimasukkan")


# 1. Cek stok (all stok update)
def cekStok(**kwargs): # **kwargs  --> mengembalikan sesuatu dari read ini
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_item = len(content) # menampilkan jumlah item, karena datanya berbentuk list di data.txt
            if "index" in kwargs: #dictionary
                index_item = kwargs["index"]-1
                if(index_item < 0 or index_item > jumlah_item):
                    return False
                else: 
                    return content[index_item]
            else:
                return content
    except:
        print("Membaca database error")
        return False



# 2. Tambah item
def tambahItem(kode,nama,bahan,stok,lokasi):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(4)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M%z",time.gmtime())
    data["kode"] = kode + Database.TEMPLATE["kode"]
    data["nama"] = nama + Database.TEMPLATE["nama"]
    data["bahan"] = bahan + Database.TEMPLATE["bahan"]
    data["stok"] = str(stok)
    data["lokasi"] = lokasi + Database.TEMPLATE["lokasi"]+"\n"

    data_str = f'{data["pk"]},{data["date_add"]},{data["kode"]},{data["nama"]},{data["bahan"]},{data["stok"]},{data["lokasi"]}'
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file: 
            file.write(data_str)     #pakai append
    except:
        print("Data gagal ditambahkan")



# 3. Update stok
def update(no_item,pk,date_add,kode,nama,bahan,stok,lokasi):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(4)
    data["date_add"] = date_add
    data["kode"] = kode
    data["nama"] = nama
    data["bahan"] = bahan
    data["stok"] = stok
    data["lokasi"] = lokasi

    data_str = f'{data["pk"]},{data["date_add"]},{data["kode"]},{data["nama"]},{data["bahan"]},{data["stok"]},{data["lokasi"]}'

    panjang_data = len(data_str)

    try:
        with(open(Database.DB_NAME,'r+',encoding="utf-8")) as file: # r+ karena read database dan menimpanya dengan data update terbaru
            file.seek(panjang_data*(no_item-1))
            file.write(data_str)
    except:
        print("Error update data")




# 4. Delete stok
def delete(no_item):
    try:
        with open(Database.DB_NAME,'r') as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_item - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("Database error")

    os.rename("data_temp.txt",Database.DB_NAME)