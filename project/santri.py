from user import User
import random

class Santri(User):

    def __init__(self, nama, nomor, tgl, tempat):
        super().__init__(nama, nomor, tgl, tempat)
        self.random_id = str(random.randint(1000,9999))
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    def tambah(self, jumlah):
        self.__saldo += jumlah

    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True
        return False

    def transfer(self, tujuan, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            tujuan.__saldo += jumlah
            return True
        return False
