class Hero:
#pertama kali dipanggil (submit)

    def __init__(self, name, job, hp):
        self.name = name
        self.job = job
        self.hp = int(hp)
        print(f"[{self.job}] Hero {self.name} telah disubmit!")
    
    def heal(self):
        print(f"{self.name} melakukan heal")
        heal_amount = 20
        self.hp += heal_amount
        print(f"hp {self.name} bertambah {heal_amount}")
        
    
    def take_damage(self, damage):
        #self.hp = self.hp - damage
        self.hp -= damage
        print(f"{self.name} terkena {damage} damage")
        print(f"sisa hp: {self.hp}")
        if self.hp == 0:
            print(f"{self.name} tereliminasi dari arena !")
    
    def attack(self, enemy, damage):
        print(f"{self.name} menyerang {enemy.name}")
        enemy.take_damage(damage)
    
    
    def __str__(self):
        status = "😎 hidup" if self.hp > 0 else "💀 mati"
        return f"({self.job}, {self.name}, {self.hp} | hp: {self.hp}, status: {status})"
    
    def ultimate(self, enemy, damage):
        print(f"{self.name} menyerang dengan ultimate")
        
