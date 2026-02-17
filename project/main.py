from bank import Bank

bank = Bank()

running = True

while running:

    print("\n=== TABUNGAN DIGITAL ===")
    print("1. Login")
    print("2. Daftar")
    print("3. Keluar")
    

    pilih = input("Pilih: ")

    user = None

    # ===== DAFTAR =====
    if pilih == "2":

        nama = input("Nama: ")
        nomor = input("Nomor: ")
        tgl = input("Tanggal lahir: ")
        tempat = input("Tempat lahir: ")

        user = bank.daftar(nama, nomor, tgl, tempat)

    # ===== LOGIN =====
    elif pilih == "1":

        nomor = input("Nomor: ")
        rid = input("Random ID: ")

        user = bank.login(nomor, rid)

    # ===== KELUAR =====
    elif pilih == "3":
        running = False
        print("Program selesai")
        break

    # ===== MENU TRANSAKSI =====
    if user:

        transaksi_running = True

        while transaksi_running:
            
            print("\n=== MENU ===")
            print("1. Tambah saldo")
            print("2. Tarik tunai")
            print("3. Transfer")
            print("4. Cek saldo")
            print("5. Kembali ke menu utama")


            aksi = input("Pilih: ")

            if aksi == "5":
                transaksi_running = False
                continue

            if aksi == "4":
                print("Saldo sekarang:", user.saldo)
                continue


            jumlah_input = input("Jumlah: ")

            if jumlah_input.strip() == "":
                print("⚠ Jumlah tidak boleh kosong!")
                continue

            if not jumlah_input.isdigit():
                print("⚠ Harus angka!")
                continue

            jumlah = int(jumlah_input)

            tujuan = input("Nomor tujuan (kosongkan jika bukan transfer): ")

            bank.transaksi(user, aksi, jumlah, tujuan)

            print("Saldo sekarang:", user.saldo)
