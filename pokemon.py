"""
Pokemon file for all pokemons class implementation.

Defines the Pokemon classes, all classes are child class of PokemonBase class.
"""
__author__ = "Scaffold by Jackson Goerner, Code by Koh Zi Xin"

from pokemon_base import PokemonBase, PokeType

class Charizard(PokemonBase):
    """
    Charizard Class, Derived from The PokemonBase Class
    """
    # Charizard has class variables of NAME, TYPE, BASE_LEVEL, BASE_HP and DEFENCE as they are constant values
    NAME = "Charizard"
    TYPE = PokeType.FIRE
    BASE_LEVEL = 3
    BASE_HP = 15
    DEFENCE = 4

    def __init__(self) -> None:
        """
        Values of Charizard's attributes during instantiation
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE) # Inherits the methods from PokemonBase class
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        """
        Method that returns the speed attribute of Charizard
        return: the speed of Charizard
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the speed of Charizard depends on its current level 
        self.speed = 9 + 1 * self.get_level()
        return self.speed

    def get_attack_damage(self) -> int:
        """
        Method that returns the attack damage attribute of Charizard
        return: the attack damage of Charizard
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the attack damage of Charizard depends on its current level 
        self.attack_damage = 10 + 2 * self.get_level()
        return self.attack_damage

    def get_defence(self) -> int:
        """
        Method that returns the defence attribute of Charizard
        return: the defence of Charizard
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.DEFENCE

    def get_max_hp(self) -> int:
        """
        Method that returns the maximum hp attribute of Charizard
        return: the maximum hp value of Charizard
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the maximum hp of Charizard depends on its current level 
        self.max_hp = 12 + 1 * self.get_level()
        return self.max_hp

    def defend(self, damage: int) -> None:
        """
        Method that returns the defence calculation of Charizard
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        # If effective attack is greater than Charizard's defence, Charizard loses HP equal to twice the effective attack.
        # Otherwise, it loses HP equal to the effective attack
        if damage > self.get_defence():
            self.lose_hp(damage * 2)
        else:
            self.lose_hp(damage)

    def get_evolved_version(self) -> PokemonBase:
        """
        Method that returns the respective evolved pokemon but in the case of Charizard, it does not evolve anymore since it is an evolved pokemon already
        return: the respective evolved pokemon 
        time complexity: Best Case = Worst Case = O(1)
        """
        raise Exception("This pokemon cannot be evolved")

class Charmander(PokemonBase):
    """
    Charmander Class, Derived from The PokemonBase Class
    """
    # Charmander has class variables of NAME, TYPE, BASE_LEVEL, BASE_HP and DEFENCE as they are constant values
    NAME = "Charmander"
    TYPE = PokeType.FIRE
    BASE_LEVEL = 1
    BASE_HP = 9
    DEFENCE = 4
    
    def __init__(self) -> None:
        """
        Values of Charmander's attributes during instantiation
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE) # Inherits the methods from PokemonBase class
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        """
        Method that returns the speed attribute of Charmander
        return: the speed of Charmander
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the speed of Charmander depends on its current level 
        self.speed = 7 + 1 * self.get_level()
        return self.speed

    def get_attack_damage(self) -> int:
        """
        Method that returns the attack damage attribute of Charmander
        return: the attack damage of Charmander
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the attack damage of Charmander depends on its current level 
        self.attack_damage = 6 + 1 * self.get_level()
        return self.attack_damage

    def get_defence(self) -> int:
        """
        Method that returns the defence attribute of Charmander
        return: the defence of Charmander
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.DEFENCE

    def get_max_hp(self) -> int:
        """
        Method that returns the maximum hp attribute of Charmander
        return: the maximum hp value of Charmander
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the maximum hp of Charmander depends on its current level 
        self.max_hp = 8 + 1 * self.get_level()
        return self.max_hp

    def defend(self, damage: int) -> None:
        """
        Method that returns the defence calculation of Charmander
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        # If effective attack is greater than Charizard's defence, Charmander loses HP equal to twice the effective attack.
        # Otherwise, it loses HP equal to half the effective attack 
        if damage > self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_evolved_version(self) -> PokemonBase:
        """
        Method that returns the respective evolved pokemon 
        return: the evolved pokemon which is Charizard
        time complexity: Best Case = Worst Case = O(1)
        """
        evolved_pokemon = Charizard()
        difference_of_hp = self.get_max_hp() - self.get_hp()
        evolved_pokemon.hp = evolved_pokemon.get_max_hp() - difference_of_hp
        return evolved_pokemon



class Venusaur(PokemonBase):
    """
    Venusaur Class, Derived from The PokemonBase Class
    """
    # Venusaur has class variables of NAME, TYPE, BASE_LEVEL, BASE_HP, ATTACK_DAMAGE and DEFENCE as they are constant values
    NAME = "Venusaur"
    TYPE = PokeType.GRASS
    BASE_LEVEL = 2
    BASE_HP = 21
    ATTACK_DAMAGE = 5
    DEFENCE = 10
    
    def __init__(self) -> None:
        """
        Values of Venusaur's attributes during instantiation
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE) # Inherits the methods from PokemonBase class
        self.name = self.NAME
        self.level = self.BASE_LEVEL
        self.hp = self.get_max_hp()

    def get_speed(self) -> int:
        """
        Method that returns the speed attribute of Venusaur
        return: the speed of Venusaur
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the speed of Venusaur depends on its current level 
        self.speed = 3 + (self.get_level() // 2)
        return self.speed

    def get_attack_damage(self) -> int:
        """
        Method that returns the attack damage attribute of Venusaur
        return: the attack damage of Venusaur
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.ATTACK_DAMAGE

    def get_defence(self) -> int:
        """
        Method that returns the defence attribute of Venusaur
        return: the defence of Venusaur
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.DEFENCE

    def get_max_hp(self) -> int:
        """
        Method that returns the maximum hp attribute of Venusaur
        return: the maximum hp value of Venusaur
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the maximum hp of Venusaur depends on its current level 
        self.max_hp = 20 + (self.get_level() // 2)
        return self.max_hp

    def defend(self, damage: int) -> None:
        """
        Method that returns the defence calculation of Venusaur
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        # If the effective attack is greater than (Venusaur’s defence +5), Venusaur loses HP equal to the effective attack. 
        # Otherwise, it loses HP equal to half the effective attack 
        if damage > (self.get_defence() + 5):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_evolved_version(self) -> PokemonBase:
        """
        Method that returns the respective evolved pokemon but in the case of Venusaur, it does not evolve anymore since it is an evolved pokemon already
        return: the respective evolved pokemon 
        time complexity: Best Case = Worst Case = O(1)
        """
        raise Exception("This pokemon cannot be evolved")

class Bulbasaur(PokemonBase):
    """
    Bulbasaur Class, Derived from The PokemonBase Class
    """
    # Bulbasaur has class variables of NAME, TYPE, BASE_LEVEL, BASE_HP, ATTACK_DAMAGE and DEFENCE as they are constant values
    NAME = "Bulbasaur"
    TYPE = PokeType.GRASS
    BASE_LEVEL = 1
    BASE_HP = 13
    ATTACK_DAMAGE = 5
    DEFENCE = 5
    
    def __init__(self) -> None:
        """
        Values of Bulbasaur's attributes during instantiation
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE) # Inherits the methods from PokemonBase class
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        """
        Method that returns the speed attribute of Bulbasaur
        return: the speed of Bulbasaur
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the speed of Bulbasaur depends on its current level 
        self.speed = 7 + (self.get_level() // 2)
        return self.speed

    def get_attack_damage(self) -> int:
        """
        Method that returns the attack damage attribute of Bulbasaur
        return: the attack damage of Bulbasaur
        time complexity: Best Case = Worst Case = O(1)
        """ 
        return self.ATTACK_DAMAGE

    def get_defence(self) -> int:
        """
        Method that returns the defence attribute of Bulbasaur
        return: the defence of Bulbasaur
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.DEFENCE

    def get_max_hp(self) -> int:
        """
        Method that returns the maximum hp attribute of Bulbasaur
        return: the maximum hp value of Bulbasaur
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the maximum hp of Bulbasaur depends on its current level 
        self.max_hp = 12 + 1 * self.get_level()
        return self.max_hp

    def defend(self, damage: int) -> None:
        """
        Method that returns the defence calculation of Bulbasaur
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        # If n the effective attack is greater than (Bulbasaur’s defence +5), Bulbasaur loses HP equal to the effective attack.
        # Otherwise, it loses HP equal to half the effective attack 
        if damage > (self.get_defence() + 5):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_evolved_version(self) -> PokemonBase:
        """
        Method that returns the respective evolved pokemon 
        return: the evolved pokemon which is Venusaur
        time complexity: Best Case = Worst Case = O(1)
        """
        evolved_pokemon = Venusaur()
        difference_of_hp = self.get_max_hp() - self.get_hp()
        evolved_pokemon.hp = evolved_pokemon.get_max_hp() - difference_of_hp
        return evolved_pokemon


class Blastoise(PokemonBase):
    """
    Blastoise Class, Derived from The PokemonBase Class
    """
    # Blastoise has class variables of NAME, TYPE, BASE_LEVEL, BASE_HP and SPEED as they are constant values
    NAME = "Blastoise"
    TYPE = PokeType.WATER
    BASE_LEVEL = 3
    BASE_HP = 21
    SPEED = 10
    
    def __init__(self) -> None:
        """
        Values of Blastoise's attributes during instantiation
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE) # Inherits the methods from PokemonBase class
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        """
        Method that returns the speed attribute of Blastoise
        return: the speed of Blastoise
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.SPEED

    def get_attack_damage(self) -> int:
        """
        Method that returns the attack damage attribute of Blastoise
        return: the attack damage of Blastoise
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the attack damage of Blastoise depends on its current level
        self.attack_damage = 8 + (self.get_level() // 2)
        return self.attack_damage

    def get_defence(self) -> int:
        """
        Method that returns the defence attribute of Blastoise
        return: the defence of Blastoise
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the defence of Blastoise depends on its current level
        self.defence = 8 + self.get_level()
        return self.defence

    def get_max_hp(self) -> int:
        """
        Method that returns the maximum hp attribute of Blastoise
        return: the maximum hp value of Blastoise
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the maximum hp of Blastoise depends on its current level 
        self.max_hp = 15 + 2 * self.get_level()
        return self.max_hp

    def defend(self, damage: int) -> None:
        """
        Method that returns the defence calculation of Blastoise
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        # If the effective attack is greater than double Blastoise’s defence, Blastoise loses HP equal to the effective attack.
        # Otherwise, it loses HP equal to half the effective attack 
        if damage > (self.get_defence() * 2):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_evolved_version(self) -> PokemonBase:
        """
        Method that returns the respective evolved pokemon but in the case of Blastoise, it does not evolve anymore since it is an evolved pokemon already
        return: the respective evolved pokemon 
        time complexity: Best Case = Worst Case = O(1)
        """
        raise Exception("This pokemon cannot be evolved")

class Squirtle(PokemonBase):
    """
    Squirtle Class, Derived from The PokemonBase Class
    """
    # Squirtle has class variables of NAME, TYPE, BASE_LEVEL, BASE_HP and SPEED as they are constant values
    NAME = "Squirtle"
    TYPE = PokeType.WATER
    BASE_LEVEL = 1
    BASE_HP = 11
    SPEED = 7
    
    def __init__(self) -> None:
        """
        Values of Squirtle's attributes during instantiation
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE) # Inherits the methods from PokemonBase class
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        """
        Method that returns the speed attribute of Squirtle
        return: the speed of Squirtle
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.SPEED

    def get_attack_damage(self) -> int:
        """
        Method that returns the attack damage attribute of Squirtle
        return: the attack damage of Squirtle
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the attack damage of Squirtle depends on its current level 
        self.attack_damage = 4 + (self.get_level() // 2)
        return self.attack_damage

    def get_defence(self) -> int:
        """
        Method that returns the defence attribute of Squirtle
        return: the defence of Squirtle
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the defence of Squirtle depends on its current level
        self.defence = 6 + self.get_level()
        return self.defence

    def get_max_hp(self) -> int:
        """
        Method that returns the maximum hp attribute of Squirtle
        return: the maximum hp value of Squirtle
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the maximum hp of Squirtle depends on its current level 
        self.max_hp = 9 + 2 * self.get_level()
        return self.max_hp

    def defend(self, damage: int) -> None:
        """
        Method that returns the defence calculation of Squirtle
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        # If the effective attack is greater than twice of Squirtle’s defence, Squirtle loses HP equal to the effective attack.
        # Otherwise, it loses only half as much of the HP as the effective attack
        if damage > (self.get_defence() * 2):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage // 2)

    def get_evolved_version(self) -> PokemonBase:
        """
        Method that returns the respective evolved pokemon 
        return: the evolved pokemon which is Blastoise
        time complexity: Best Case = Worst Case = O(1)
        """
        evolved_pokemon = Blastoise()
        difference_of_hp = self.get_max_hp() - self.get_hp()
        evolved_pokemon.hp = evolved_pokemon.get_max_hp() - difference_of_hp
        return evolved_pokemon


class Gengar(PokemonBase):
    """
    Gengar Class, Derived from The PokemonBase Class
    """
    # Gengar has class variables of NAME, TYPE, BASE_LEVEL, BASE_HP, ATTACK_DAMAGE, SPEED and DEFENCE as they are constant values
    NAME = "Gengar"
    TYPE = PokeType.GHOST
    BASE_LEVEL = 3
    BASE_HP = 13
    ATTACK_DAMAGE = 18
    SPEED = 12
    DEFENCE = 3
    
    def __init__(self) -> None:
        """
        Values of Gengar's attributes during instantiation
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE) # Inherits the methods from PokemonBase class
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        """
        Method that returns the speed attribute of Gengar
        return: the speed of Gengar
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.SPEED

    def get_attack_damage(self) -> int:
        """
        Method that returns the attack damage attribute of Gengar
        return: the attack damage of Gengar
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.ATTACK_DAMAGE

    def get_defence(self) -> int:
        """
        Method that returns the defence attribute of Gengar
        return: the defence of Gengar
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.DEFENCE

    def get_max_hp(self) -> int:
        """
        Method that returns the maximum hp attribute of Gengar
        return: the maximum hp value of Gengar
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the maximum hp of Gengar depends on its current level 
        self.max_hp = 12 + (self.get_level() // 2)
        return self.max_hp

    def defend(self, damage: int) -> None:
        """
        Method that returns the defence calculation of Gengar
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        # Loses HP equal to the effective attack
        self.lose_hp(damage)

    def get_evolved_version(self) -> PokemonBase:
        """
        Method that returns the respective evolved pokemon but in the case of Gengar, it does not evolve anymore since it is an evolved pokemon already
        return: the respective evolved pokemon 
        time complexity: Best Case = Worst Case = O(1)
        """
        raise Exception("This pokemon cannot be evolved")

class Haunter(PokemonBase):
    """
    Haunter Class, Derived from The PokemonBase Class
    """
    # Haunter has class variables of NAME, TYPE, BASE_LEVEL, BASE_HP, ATTACK_DAMAGE, SPEED and DEFENCE as they are constant values
    NAME = "Haunter"
    TYPE = PokeType.GHOST
    BASE_LEVEL = 1
    BASE_HP = 9
    ATTACK_DAMAGE = 8
    SPEED = 6
    DEFENCE = 6
    
    def __init__(self) -> None:
        """
        Values of Haunter's attributes during instantiation
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE) # Inherits the methods from PokemonBase class
        self.name = self.NAME
        self.level = self.get_level()

    def get_speed(self) -> int:
        """
        Method that returns the speed attribute of Haunter
        return: the speed of Haunter
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.SPEED

    def get_attack_damage(self) -> int:
        """
        Method that returns the attack damage attribute of Haunter
        return: the attack damage of Haunter
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.ATTACK_DAMAGE

    def get_defence(self) -> int:
        """
        Method that returns the defence attribute of Haunter
        return: the defence of Haunter
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.DEFENCE

    def get_max_hp(self) -> int:
        """
        Method that returns the maximum hp attribute of Haunter
        return: the maximum hp value of Haunter
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the maximum hp of Haunter depends on its current level 
        self.max_hp = 9 + (self.get_level() // 2)
        return self.max_hp

    def defend(self, damage: int) -> None:
        """
        Method that returns the defence calculation of Haunter
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        # Loses HP equal to the effective attack
        self.lose_hp(damage)

    def get_evolved_version(self) -> PokemonBase:
        """
        Method that returns the respective evolved pokemon 
        return: the evolved pokemon which is Gengar
        time complexity: Best Case = Worst Case = O(1)
        """
        evolved_pokemon = Gengar()
        difference_of_hp = self.get_max_hp() - self.get_hp()
        evolved_pokemon.hp = evolved_pokemon.get_max_hp() - difference_of_hp
        return evolved_pokemon

class Gastly(PokemonBase):
    """
    Gastly Class, Derived from The PokemonBase Class
    """
    # Gastly has class variables of NAME, TYPE, BASE_LEVEL, BASE_HP, ATTACK_DAMAGE, SPEED and DEFENCE as they are constant values
    NAME = "Gastly"
    TYPE = PokeType.GHOST
    BASE_LEVEL = 1
    BASE_HP = 6
    ATTACK_DAMAGE = 4
    SPEED = 2
    DEFENCE = 8
    
    def __init__(self) -> None:
        """
        Values of Gastly's attributes during instantiation
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE) # Inherits the methods from PokemonBase class
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        """
        Method that returns the speed attribute of Gastly
        return: the speed of Gastly
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.SPEED

    def get_attack_damage(self) -> int:
        """
        Method that returns the attack damage attribute of Gastly
        return: the attack damage of Gastly
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.ATTACK_DAMAGE

    def get_defence(self) -> int:
        """
        Method that returns the defence attribute of Gastly
        return: the defence of Gastly
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.DEFENCE

    def get_max_hp(self) -> int:
        """
        Method that returns the maximum hp attribute of Gastly
        return: the maximum hp value of Gastly
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the maximum hp of Gastly depends on its current level 
        self.max_hp = 6 + (self.get_level() // 2)
        return self.max_hp

    def defend(self, damage: int) -> None:
        """
        Method that returns the defence calculation of Gastly
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        # Loses HP equal to the effective attack
        self.lose_hp(damage)

    def get_evolved_version(self) -> PokemonBase:
        """
        Method that returns the respective evolved pokemon 
        return: the evolved pokemon which is Haunter
        time complexity: Best Case = Worst Case = O(1)
        """
        evolved_pokemon = Haunter()
        difference_of_hp = self.get_max_hp() - self.get_hp()
        evolved_pokemon.hp = evolved_pokemon.get_max_hp() - difference_of_hp
        return evolved_pokemon


class Eevee(PokemonBase):
    """
    Eevee Class, Derived from The PokemonBase Class
    """
    # Eevee has class variables of NAME, TYPE, BASE_LEVEL and BASE_HP as they are constant values
    NAME = "Eevee"
    TYPE = PokeType.NORMAL
    BASE_LEVEL = 1
    BASE_HP = 10
    
    def __init__(self) -> None:
        """
        Values of Eevee's attributes during instantiation
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        PokemonBase.__init__(self, self.BASE_HP, self.TYPE) # Inherits the methods from PokemonBase class
        self.name = self.NAME
        self.level = self.BASE_LEVEL

    def get_speed(self) -> int:
        """
        Method that returns the speed attribute of Eevee
        return: the speed of Eevee
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the speed of Eevee depends on its current level 
        self.speed = 7 + self.get_level()
        return self.speed

    def get_attack_damage(self) -> int:
        """
        Method that returns the attack damage attribute of Eevee
        return: the attack damage of Eevee
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the attack damage of Eevee depends on its current level 
        self.attack_damage = 6 + self.get_level()
        return self.attack_damage

    def get_defence(self) -> int:
        """
        Method that returns the defence attribute of Eevee
        return: the defence of Eevee
        time complexity: Best Case = Worst Case = O(1)
        """
        # We call self.get_level() since the defence of Eevee depends on its current level
        self.defence = 4 + self.get_level()
        return self.defence

    def get_max_hp(self) -> int:
        """
        Method that returns the maximum hp attribute of Eevee
        return: the maximum hp value of Eevee
        time complexity: Best Case = Worst Case = O(1)
        """
        return self.BASE_HP

    def defend(self, damage: int) -> None:
        """
        Method that returns the defence calculation of Eevee
        return: None
        time complexity: Best Case = Worst Case = O(1)
        """
        # If the effective attack is greater or equal to Eevee’s defence, Eevee loses HP equal to the effective attack
        # Otherwise, it loses 0 HP
        if damage >= self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(0)

    def get_evolved_version(self) -> PokemonBase:
        """
        Method that returns the respective evolved pokemon but in the case of Eevee, it does not evolve 
        return: the respective evolved pokemon 
        time complexity: Best Case = Worst Case = O(1)
        """
        raise Exception("This pokemon cannot be evolved")
