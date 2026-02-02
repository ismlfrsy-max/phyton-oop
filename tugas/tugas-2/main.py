from monster import Monster
from warrior import Warrior
from mage import Mage
from archer import Archer
from assasin import Assasin
import random

print("== SUMMON SEMUA HERO ==")
Thorin = Warrior("Thorin", 100)
Arcana = Mage("Arcana", 100)
Aelric = Archer("Aelric", 100)
Nyx = Assasin("Nyx", 100)

print("\n== SUMMON BOSS ==")
Peterson = Monster("Peterson King", 300)

running = True
while running:
    print("=" * 25) 
    print("== STATUS BOS ==")
    print(Peterson)

    print("\n== PILIHAN AKSI : ==")
    print("*** 1. ATTACK")
    print("*** 2. HEAL")
    print("*** 3. ULTIMATE")
    print("*** 4. EXIT\n")

    try:
        aksi = int(input(">>> AKSI MU : "))
    except ValueError:
        print("❌ AKSI harus angka 1-4!")
        continue

    raid_party = [Thorin, Arcana, Aelric, Nyx]

    if aksi == 1:
        for party in raid_party:
            party.attack(Peterson, 10)

    elif aksi == 2:
        for party in raid_party:
            party.heal()

    elif aksi == 3:
        for party in raid_party:
            party.ultimate(Peterson)

    elif aksi == 4:
        running = False
        print("== GAME BERAKHIR, BYE BYE! ==")
        break

    else:
        print("== ⚠️ AKSI SALAH, COBA 1-4! ==")

    # boss menyerang balik satu hero random
    target = random.choice(raid_party)
    print("\n== BOSS MENYERANG BALIK ==")
    Peterson.attack(target)

    if Peterson.hp == 0:
        print("== BOS TELAH MATI, GAME SELESAI! ==")
        running = False
