import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("selamat datang di program".upper().center(70))
    print("Cek Stok Gudang tokoku official".upper().center(70))
    print((str("="*30)) + "  Tahun 2023  " + (str("="*30)))

    # check database ada atau tidak
    CRUD.init_console()

    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("selamat datang di program".upper().center(70))
        print("Cek Stok Gudang tokoku official".upper().center(70))
        print((str("="*30)) + "  Tahun 2023  " + (str("="*30)))

        print(f"1. Cek stok")
        print(f"2. Tambah Item")
        print(f"3. Update Stok")
        print(f"4. Delete Stok")
        print(f"5. Exit\n")

        user_option = input("Silahkan pilih menu utama [1-5] : ")


        match user_option:
            case "1" : CRUD.cekStok_console()
            case "2" : CRUD.tambahItem_console()
            case "3" : CRUD.update_console()
            case "4" : CRUD.delete_console()
            case "5" : print("Anda telah keluar dari program")

        is_done = input("Apakah anda sudah selesai ? (y/n) : ")
        if(is_done == "y" or is_done == "Y"):
            break

    print("Kamu telah keluar program, terimakasih")