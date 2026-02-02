from hero import Hero

class Assasin(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, job="Assasin")

    def ultimate(self, enemy):
        dmg = 90
        print(f"{self.name} menggunakan skill: SHADOW KILL")
        print(f"dengan damage {dmg} DMG")
        enemy.take_damage(dmg)
