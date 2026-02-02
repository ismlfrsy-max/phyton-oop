from hero import Hero

class Archer(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, job="Archer")

    def ultimate(self, enemy):
        dmg = 80
        print(f"{self.name} menggunakan skill: RAIN ARROW")
        print(f"dengan damage {dmg} DMG")
        enemy.take_damage(dmg)

    def combo(self, enemy):
        dmg = 10
        print(f"{self.name} menggunakan combo: WIND ARROW x3 {dmg*3} DMG")
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
