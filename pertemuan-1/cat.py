#diawali class NamaClass
class Cat:
    #self merepresentasikan objek itu sendiri
    #__init__ adalah konstruktor untuk inisialisasi objek=
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    def sleep(self, duration):
        print(f"turu {duration} menit")

# buat objek dari class Cat
belang = Cat("mix", 5)
oyen = Cat("orange", 4)

#print("obj belang:", belang)
#print("obj oyen:", oyen)
belang.sleep(30)
oyen.sleep(45)
print(f"warna si belang: {belang.color}")
print(f"berat si belang: {belang.weight} kg")