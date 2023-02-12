'''
Игра "Простая текстовая RPG"

Программа написана по урокам с YouTube анала Sima Games
@sima_games
https://www.youtube.com/@sima_games
'''


import random

hp = 0 
coins = 0
damage = 0

def printParametrs():
    print("У тебя {0} жизней, {1} монет и {2} урона.".format(hp, coins, damage))

def printHp():
    print("У тебя", hp, "жизнейю.")

def printCoins():
    print("У тебя", coins, "монет.")

def printDamage():
    print("У тебя", damage, "урона.")

def meetShop():
    global hp
    global coins
    global damage

    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            printCoins()
            return True
        print("У тебя маловато монет!")
        return False

    weaponLvl = random.randint(1, 3)
    weaponDmg = random.randint(1, 5) * weaponLvl
    weapons = ["АК-47", "Железный меч", "Волшебная палочка", "Розовый единорог", "Граната", "Дубина", "Яд", "Лук", "Арбалет"]
    weaponRarities = ["Испорченный", "Редкий", "Легендарный"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weaponCost = random.randint(1, 10) * weaponLvl
    weapon = random.choice(weapons)

    oneHpCost = 5
    threeHPCost = 12

    print("На пути тебе встретилсяв торговец!")
    printParametrs()

    while input("Что ты будешь делать (зайти/уйти): ").lower() == "зайти":
        print("1) Одна единица здоровья -", oneHpCost, "монет")
        print("2) Три единицы здоровья -", threeHPCost, "монет")
        print("3) {0} {1} = {2} урон. Стоимость - {3} монет".format(weaponRarity, weapon, weaponDmg, weaponCost))

        choise = input("Что хочешь приобрести: ")
        if choise == "1":
            if buy(oneHpCost):
                hp += 1
                printHp()
        elif choise == "2":
            if buy(threeHPCost):
                hp += 3
                printHp()
        elif choise == "3":
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
        else:
            print("Я такое не продаю.")


def meetMonster():
    global hp
    global coins
    
    monsterLvl = random.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsters = ['Liliput', 'Gigant', 'Krab', 'Plankton', 'Titan', 'Ant']
    monster = random.choice(monsters)

    print("Ты набрел на монстра - {0}, у него {1} уровень, {2} жизней и {3} урона!".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParametrs()

    while monsterHp > 0:
        choice = input("Что будешь делать (атака/бег): ").lower()

        if choice == "атака":
            monsterHp -= damage
            print(f"Ты атаковал монстра и у него осталось {monsterHp} жизней.")
        elif choice == "бег":
            chance = random.randint(0, monsterLvl)
            if chance == 0:
                print("Тебе удалось сбежать с поля боя!")
                break
            else:
                print("Монстр оказался чересчур сильным и догнал тебя...")
        else:
            continue

        if monsterHp > 0:
            hp -= monsterDmg
            if hp <= 0:
                print("К сожалению монстр оказался слишком сильнрвм и ты был повержен...")
            else:
                print(f"Монстр атаковал и у тебя осталось {hp} жизней.")

        if hp <= 0:
            break
    
    else:
        loot = random.randint(0, 2) + monsterLvl
        coins += loot
        print(f"Тебе удалось одалеть монстра! За это ты получил {loot} монет.")
        printCoins()




def initGame(initHp, initCoins, initDmg):
    global hp
    global coins
    global damage

    hp = initHp 
    coins = initCoins
    damage = initDmg

    print("Ты отправился в странствие на встречу приключениям и опасностям. Удачного путешествия!")

    printParametrs()

def gameLoop():
    situation = random.randint(0, 10)
    if situation == 0:
       # input("shop")
       meetShop()
    elif situation == 1:
       # input("monster")
       meetMonster()
    else:
        input("Блуждаю...")    

initGame(3, 5, 1)

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала (да/нет): ").lower() == "да":
            initGame(3, 5, 1)
        else:
            break
