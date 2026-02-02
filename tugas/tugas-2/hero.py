class Hero:
    def __init__(self, name, hp, job):
        self.name = name
        self.job = job
        self.__hp = hp 
        print(f"✨ [{job}] Hero {self.name} telah di summon!")

    def get_hp(self):
        return self.__hp
    
    def set_hp(self, number):
        self.__hp += number

    def is_alive(self):
        return self.__hp > 0

    def heal(self):
        if not self.is_alive():
            print(f"💀 {self.name} sudah mati, tidak bisa heal!")
            return

        print(f"🧪 {self.name} meminum potion...")
        heal_amount = 20
        self.__hp += heal_amount
        print(f"💚 HP {self.name} bertambah +{heal_amount}")

    def take_damage(self, damage):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0

        print(f"💥 {self.name} terkena {damage} damage\n")
        if self.__hp == 0:
            print(f"🚫 {self.name} tereliminasi dari arena!")
    
    def attack(self, enemy, damage):
        if not self.is_alive():
            print(f"💀 {self.name} sudah mati dan tidak bisa menyerang!")
            return

        print(f"⚔️ {self.name} menyerang {enemy.name}!")
        enemy.take_damage(damage)

    def __str__(self):
        status = "🟢 HIDUP" 
        if self.__hp == 0:
            status = "💀 MATI" 

        return f"[{self.job}] {self.name} | HP: {self.__hp} | {status}"
    
    def ultimate(self, enemy):
        print(f"⚔️ {self.name} bengong!")
