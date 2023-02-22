from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {                                 #library database
    "pk":"XXXX", #prim key
    "date_add":"yyyy-mm-dd",
    "kode":" ",
    "nama":" ",
    "bahan":" ",
    "stok":" Pcs",
    "lokasi":" "
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database belum ada di sistem, silahkan membuat database baru")
        Operasi.create_first_data()
    