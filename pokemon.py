"""
Pokemon file for all pokemons class implementation.

Defines the Pokemon classes, all classes are child class of PokemonBase class.
"""
__author__ = "Scaffold by Jackson Goerner, Code by Koh Zi Xin"

from pokemon_base import PokemonBase, PokeType
# from random import randint

class Charizard(PokemonBase):
    """
    Charizard Class, Derived from The PokemonBase Class
    """
    NAME = "Charizard"
    TYPE = PokeType.FIRE
    BASE_LEVEL = 3
    BASE_HP = 15
    DEFENCE = 4

    def __init__(self) -> None:
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE)
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        self.speed = 9 + 1 * self.get_level()
        return self.speed

    def get_attack_damage(self) -> int:
        self.attack_damage = 10 + 2 * self.get_level()
        return self.attack_damage

    def get_defence(self) -> int:
        return self.DEFENCE

    def get_max_hp(self) -> int:
        self.max_hp = 12 + 1 * self.get_level()
        return self.max_hp

    def defend(self, damage: int) -> None:
        PokemonBase.defend(self, damage)
        if damage > self.get_defence():
            self.lose_hp(damage * 2)
        else:
            self.lose_hp(damage)

    def get_evolved_version(self) -> PokemonBase:
        PokemonBase.get_evolved_version(self)

class Charmander(PokemonBase):
    """
    Charmander Class, Derived from The PokemonBase Class
    """
    NAME = "Charmander"
    TYPE = PokeType.FIRE
    BASE_LEVEL = 1
    BASE_HP = 9
    DEFENCE = 4

    def __init__(self) -> None:
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE)
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        self.speed = 7 + 1 * self.get_level()
        return self.speed

    def get_attack_damage(self) -> int:
        self.attack_damage = 6 + 1 * self.get_level()
        return self.attack_damage

    def get_defence(self) -> int:
        return self.DEFENCE

    def get_max_hp(self) -> int:
        self.max_hp = 8 + 1 * self.get_level()
        return self.max_hp

    def defend(self, damage: int) -> None:
        PokemonBase.defend(self, damage)
        if damage > self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_evolved_version(self) -> PokemonBase:
        PokemonBase.get_evolved_version(self)
        evolved_pokemon = Charizard
        return evolved_pokemon()


class Venusaur(PokemonBase):
    """
    Venusaur Class, Derived from The PokemonBase Class
    """
    NAME = "Venusaur"
    TYPE = PokeType.GRASS
    BASE_LEVEL = 2
    BASE_HP = 21
    ATTACK_DAMAGE = 5
    DEFENCE = 10

    def __init__(self) -> None:
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE)
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        self.speed = 3 + (self.get_level() // 2)
        return self.speed

    def get_attack_damage(self) -> int:
        return self.ATTACK_DAMAGE

    def get_defence(self) -> int:
        return self.DEFENCE

    def get_max_hp(self) -> int:
        self.max_hp = 20 + (self.get_level() // 2)
        return self.max_hp

    def defend(self, damage: int) -> None:
        PokemonBase.defend(self, damage)
        if damage > (self.get_defence() + 5):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_evolved_version(self) -> PokemonBase:
        PokemonBase.get_evolved_version(self)

class Bulbasaur(PokemonBase):
    """
    Bulbasaur Class, Derived from The PokemonBase Class
    """
    NAME = "Bulbasaur"
    TYPE = PokeType.GRASS
    BASE_LEVEL = 1
    BASE_HP = 13
    ATTACK_DAMAGE = 5
    DEFENCE = 5

    def __init__(self) -> None:
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE)
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        self.speed = 7 + (self.get_level() // 2)
        return self.speed

    def get_attack_damage(self) -> int:
        return self.ATTACK_DAMAGE

    def get_defence(self) -> int:
        return self.DEFENCE

    def get_max_hp(self) -> int:
        self.max_hp = 12 + 1 * self.get_level()
        return self.max_hp

    def defend(self, damage: int) -> None:
        PokemonBase.defend(self, damage)
        if damage > (self.get_defence() + 5):
            self.lose_hp(damage)
        else:
            self.lose_hp(self.get_hp() // 2)

    def get_evolved_version(self) -> PokemonBase:
        PokemonBase.get_evolved_version(self)
        evolved_pokemon = Venusaur
        return evolved_pokemon()


class Blastoise(PokemonBase):
    """
    Blastoise Class, Derived from The PokemonBase Class
    """
    NAME = "Blastoise"
    TYPE = PokeType.WATER
    BASE_LEVEL = 3
    BASE_HP = 21
    SPEED = 10

    def __init__(self) -> None:
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE)
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        return self.SPEED

    def get_attack_damage(self) -> int:
        self.attack_damage = 8 + (self.get_level() // 2)
        return self.attack_damage

    def get_defence(self) -> int:
        self.defence = 8 + self.get_level()
        return self.defence

    def get_max_hp(self) -> int:
        self.max_hp = 15 + 2 * self.get_level()
        return self.max_hp

    def defend(self, damage: int) -> None:
        PokemonBase.defend(self, damage)
        if damage > (self.get_defence() * 2):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_evolved_version(self) -> PokemonBase:
        PokemonBase.get_evolved_version(self)

class Squirtle(PokemonBase):
    """
    Squirtle Class, Derived from The PokemonBase Class
    """
    NAME = "Squirtle"
    TYPE = PokeType.WATER
    BASE_LEVEL = 1
    BASE_HP = 11
    SPEED = 7

    def __init__(self) -> None:
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE)
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        return self.SPEED

    def get_attack_damage(self) -> int:
        self.attack_damage = 4 + (self.get_level() // 2)
        return self.attack_damage

    def get_defence(self) -> int:
        self.defence = 6 + self.get_level()
        return self.defence

    def get_max_hp(self) -> int:
        self.max_hp = 9 + 2 * self.get_level()
        return self.max_hp

    def defend(self, damage: int) -> None:
        PokemonBase.defend(self, damage)
        if damage > (self.get_defence() * 2):
            self.lose_hp(damage)
        else:
            self.lose_hp(self.get_hp() // 2)

    def get_evolved_version(self) -> PokemonBase:
        PokemonBase.get_evolved_version(self)
        evolved_pokemon = Blastoise
        return evolved_pokemon()


class Gengar(PokemonBase):
    """
    Gengar Class, Derived from The PokemonBase Class
    """
    NAME = "Gengar"
    TYPE = PokeType.GHOST
    BASE_LEVEL = 3
    BASE_HP = 13
    ATTACK_DAMAGE = 18
    SPEED = 12
    DEFENCE = 3

    def __init__(self) -> None:
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE)
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        return self.SPEED

    def get_attack_damage(self) -> int:
        return self.ATTACK_DAMAGE

    def get_defence(self) -> int:
        return self.DEFENCE

    def get_max_hp(self) -> int:
        self.max_hp = 12 + (self.get_level() // 2)
        return self.max_hp

    def defend(self, damage: int) -> None:
        PokemonBase.defend(self, damage)
        self.lose_hp(damage)

    def get_evolved_version(self) -> PokemonBase:
        PokemonBase.get_evolved_version(self)

class Haunter(PokemonBase):
    """
    Haunter Class, Derived from The PokemonBase Class
    """
    NAME = "Haunter"
    TYPE = PokeType.GHOST
    BASE_LEVEL = 1
    BASE_HP = 9
    ATTACK_DAMAGE = 8
    SPEED = 6
    DEFENCE = 6

    def __init__(self) -> None:
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE)
        self.name = self.NAME
        self.level = self.get_level()

    def get_speed(self) -> int:
        return self.SPEED

    def get_attack_damage(self) -> int:
        return self.ATTACK_DAMAGE

    def get_defence(self) -> int:
        return self.DEFENCE

    def get_max_hp(self) -> int:
        self.max_hp = 9 + (self.get_level() // 2)
        return self.max_hp

    def defend(self, damage: int) -> None:
        PokemonBase.defend(self, damage)
        self.lose_hp(damage)

    def get_evolved_version(self) -> PokemonBase:
        PokemonBase.get_evolved_version(self)
        evolved_pokemon = Gengar
        return evolved_pokemon()

class Gastly(PokemonBase):
    """
    Gastly Class, Derived from The PokemonBase Class
    """
    NAME = "Gastly"
    TYPE = PokeType.GHOST
    BASE_LEVEL = 1
    BASE_HP = 6
    ATTACK_DAMAGE = 4
    SPEED = 2
    DEFENCE = 8

    def __init__(self) -> None:
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE)
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        return self.SPEED

    def get_attack_damage(self) -> int:
        return self.ATTACK_DAMAGE

    def get_defence(self) -> int:
        return self.DEFENCE

    def get_max_hp(self) -> int:
        self.max_hp = 6 + (self.get_level() // 2)
        return self.max_hp

    def defend(self, damage: int) -> None:
        PokemonBase.defend(self, damage)
        self.lose_hp(damage)

    def get_evolved_version(self) -> PokemonBase:
        PokemonBase.get_evolved_version(self)
        evolved_pokemon = Haunter
        return evolved_pokemon()


class Eevee(PokemonBase):
    """
    Eevee Class, Derived from The PokemonBase Class
    """
    NAME = "Eevee"
    TYPE = PokeType.NORMAL
    BASE_LEVEL = 1
    BASE_HP = 10

    def __init__(self) -> None:
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE)
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        self.speed = 7 + self.get_level()
        return self.speed

    def get_attack_damage(self) -> int:
        self.attack_damage = 6 + self.get_level()
        return self.attack_damage

    def get_defence(self) -> int:
        self.defence = 4 + self.get_level()
        return self.defence

    def get_max_hp(self) -> int:
        return self.BASE_HP

    def defend(self, damage: int) -> None:
        PokemonBase.defend(self, damage)
        if damage >= self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(0)

    def get_evolved_version(self) -> PokemonBase:
        PokemonBase.get_evolved_version(self)