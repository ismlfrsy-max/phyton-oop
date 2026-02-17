from santri import Santri

class Bank:

    def __init__(self):
        self.users = []

    def daftar(self, nama, nomor, tgl, tempat):

        user = Santri(nama, nomor, tgl, tempat)
        self.users.append(user)

        print("Daftar berhasil.")
        print("Random ID:", user.random_id)

        return user

    def login(self, nomor, random_id):

        for u in self.users:
            if u.nomor == nomor and u.random_id == random_id:
                print("Login berhasil.")
                return u

        print("Login gagal.")
        return None

    def cari(self, nomor):

        for u in self.users:
            if u.nomor == nomor:
                return u

    def transaksi(self, user, aksi, jumlah, nomor_tujuan=None):

        if aksi == "1":
            user.tambah(jumlah)
            print("Saldo bertambah.")

        elif aksi == "2":
            if not user.tarik(jumlah):
                print("Saldo tidak cukup.")

        elif aksi == "3":
            tujuan = self.cari(nomor_tujuan)

            if tujuan:
                if user.transfer(tujuan, jumlah):
                    print("Transfer berhasil.")
                else:
                    print("Saldo tidak cukup.")

