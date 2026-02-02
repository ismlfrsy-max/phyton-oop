from hero import Hero

class Warrior(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, job="Warrior")

    def ultimate(self, enemy):
        dmg = 100
        print(f"{self.name} menggunakan skill: GIGANTIC SLASH")
        print(f"dengan damage {dmg} DMG")
        enemy.take_damage(dmg)
