import random

class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        print(f"🐲 Monster {self.name} telah di summon!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

        print(f"💥 {self.name} terkena {damage} damage")
        print(f"❤️ Sisa HP Boss: {self.hp}\n")

        if self.hp == 0:
            print(f"🏆 {self.name} TERKALAHKAN!")
        else:
            self.phase_check()

    def phase_check(self):
        if self.hp <= self.max_hp * 0.2:
            print("🔥 BOSS MODE CRITICAL! DAMAGE MENINGKAT TAJAM!")
        elif self.hp <= self.max_hp * 0.5:
            print("😈 BOSS MODE ENRAGE! SERANGAN LEBIH KUAT!")

    def attack(self, hero):
        if self.hp == 0:
            return

        base_damage = random.randint(10, 20)

        # mode enrage
        if self.hp <= self.max_hp * 0.5:
            base_damage += 10
            print("😈 Boss Enrage Attack!")

        # mode critical
        if self.hp <= self.max_hp * 0.2:
            base_damage += 20
            print("🔥 Boss Critical Attack!")

        print(f"🐲 {self.name} menyerang {hero.name} dengan {base_damage} damage!")
        hero.take_damage(base_damage)

    def __str__(self):
        status = "🟢 HIDUP" 
        if self.hp == 0:
            status = "💀 MATI" 

        return f"[Monster] {self.name} | HP: {self.hp}/{self.max_hp} | {status}"
