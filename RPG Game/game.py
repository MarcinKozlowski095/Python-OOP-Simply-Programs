"""
Zadanie: Gra RPG
Stwórz klasy dla gry RPG. Klasa Postac powinna mieć atrybuty jak imie, zdrowie, sila, oraz mana. 
Dodaj klasy Wojownik i Mag, które będą dziedziczyć po klasie Postac i będą miały dodatkowe unikalne atrybuty oraz metody.
"""

class Character:
    def __init__(self, name, hp, str, mana):
        self.name = name
        self.hp = hp
        self.str = str
        self.mana = mana

    def display(self):
        return f"Character: {self.name}, zdrowie: {self.hp}, siła: {self.str}, mana: {self.mana}"

    def attack(self):
        print(f'{self.name} attack!')

    def defence(self):
        print(f'{self.name} defend!')

class Worior(Character):
    def __init__(self, name, hp, str, mana, tarcza):
        super().__init__(name, hp, str, mana)
        self.tarcza = tarcza

    def block(self):
        print(f'{self.name} block attack!')

class Mage(Character):
    def __init__(self, name, hp, str, mana, spells):
        super().__init__( name, hp, str, mana)
        self.spells = spells

    def use_sepll(self, spell):
        if spell in self.spells:
            print(f'{self.name} use {spell}')
        else:
            print(f'{self.name} dont know {spell}')


worrior = Worior('Kratos', 1000, 200, 10, True)
mage = Mage('Tris', 700, 10, 200, ['Fire Bolt', 'Protect'])

print(worrior.display())
worrior.attack()
worrior.defence()
worrior.block()

print(mage.display())
mage.attack()
mage.defence()
mage.use_sepll('Fire Bolt')
mage.use_sepll('Ice Blast')
