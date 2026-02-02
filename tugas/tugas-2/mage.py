from hero import Hero

class Mage(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, job="Mage")

    def ultimate(self, enemy):
        dmg = 85
        print(f"{self.name} menggunakan skill: FIRE ARROW")
        print(f"dengan damage {dmg} DMG")
        enemy.take_damage(dmg)

    def combo(self, enemy):
        dmg = 20
        print(f"{self.name} menggunakan combo: WATER CANON x3 {dmg*3} DMG")
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
