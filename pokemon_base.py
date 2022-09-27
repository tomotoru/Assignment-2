from __future__ import annotations

"""
PokemonBase File for Base Pokemon Method Implementation.

Defines the PokemonBase class, an abstract Parent Class for the Pokemons.
"""
__author__ = "Scaffold by Jackson Goerner, Code by Tan Shuen Y'ng, Joanna Moy, Koh Zi Xin and How Yew Wai"

from abc import ABC, abstractmethod
from random_gen import RandomGen
from enum import Enum

ATTACK_MULTIPLIER = [
    [1, 2, 0.5, 1, 1],
    [0.5, 1, 2, 1, 1],
    [2, 0.5, 1, 1, 1],
    [1.25, 1.25, 1.25, 2, 0],
    [1.25, 1.25, 1.25, 0, 1]
]


class PokeType(Enum):
    """
    This is the class of PokeType, the members are FIRE, GRASS, WATER, GHOST and NORMAL.
    """
    FIRE = 0
    GRASS = 1
    WATER = 2
    GHOST = 3
    NORMAL = 4


class PokemonBase(ABC):
    """
    This is the class of PokemonBase, which has 22 instance methods.

    Unless stated otherwise, all instance methods below have best / worst case complexity O(1).
    """

    def __init__(self, hp: int, poke_type: PokeType) -> None:
        """
        Constructor of the class that initializes the required instance variables.

        :parameter hp: The hp value of the pokemon
        :parameter poke_type: The type of the pokemon
        :return: None

        :time complexity: Best Case = Worst Case = O(1), as there are only assignments and comparisons.
        """
        # Precondition check - no point to create a fainted pokemon
        if hp <= 0:
            raise ValueError("hp must not be a negative integer or 0")
        else:
            self.max_hp = hp
            self.hp = hp

        # Precondition check - poke_type must be an instance of PokeType Enum (FIRE, GRASS, WATER, GHOST and NORMAL)
        if not (isinstance(poke_type, PokeType)):
            raise ValueError("poke_type must be an instance of PokeType Enum")
        else:
            self.poke_type = poke_type.name

        self.level = 1
        self.speed = None
        self.attack_damage = None
        self.defence = None
        self.asleep = False
        self.confused = False
        self.halve_effective_attack = False
        self.paralyzed = False

    def is_fainted(self) -> bool:
        """
        Method that returns False if the caller pokemon is alive, True otherwise.

        :return: boolean value (True - fainted, False - Alive)

        :time complexity: Best Case = Worst Case = O(1)
        """
        return self.get_hp() <= 0

    def get_level(self) -> int:
        """
        Getter method - Returns the Level of the pokemon.

        :return: The level value of the pokemon

        :time complexity: Best Case = Worst Case = O(1)
        """
        return self.level

    def level_up(self) -> None:
        """
        Method that increase the level of pokemon by 1 on every call.

        :time complexity: Best Case = Worst Case = O(1)
        """
        difference_of_hp = self.get_max_hp() - self.get_hp()
        self.level += 1
        self.hp = self.get_max_hp() - difference_of_hp

    @abstractmethod
    def get_speed(self) -> int:
        """
        Getter method - Returns the speed of the pokemon.

        :return: The speed of the pokemon

        :time complexity: Best Case = Worst Case = O(1)
        """
        pass

    @abstractmethod
    def get_attack_damage(self) -> int:
        """
        Getter method - Returns the attack damage of the pokemon.

        :return: The attack damage of the pokemon

        :time complexity: Best Case = Worst Case = O(1)
        """
        pass

    @abstractmethod
    def get_defence(self) -> int:
        """
        Getter method - Returns the defence of the pokemon.

        :return: The defence of the pokemon

        :time complexity: Best Case = Worst Case = O(1)
        """
        pass

    def get_hp(self) -> int:
        """
        Getter method - Returns the current hp of the pokemon.

        :return: The hp value of the pokemon

        :time complexity: Best Case = Worst Case = O(1)
        """
        return self.hp

    @abstractmethod
    def get_max_hp(self) -> int:
        """
        Getter method - Returns the maximum hp of the pokemon.

        :return: The maximum hp value of the pokemon

        :time complexity: Best Case = Worst Case = O(1)
        """
        pass

    def lose_hp(self, lost_hp: int) -> None:
        """
        Method to lose hp of the caller pokemon.

        :parameter lose_hp: Integer value of hp to be lost
        :return: None

        :pre-condition: hp must be an integer value.

        :time complexity: Best Case = Worst Case = O(1)
        """
        if not (isinstance(lost_hp, int)):
            raise TypeError("damage taken must be an integer")
        self.hp = self.get_hp() - lost_hp

    @abstractmethod
    def defend(self, damage: int) -> None:
        """
        Method to do the defence calculation of the caller pokemon, abstract now as defence calculation is not set for the base class.
        The defence calculation is different for each pokemons.

        :parameter damage: Integer value of effective damage
        :return: None

        :pre-condition: Effective damage must be an integer value.

        :time complexity: Best Case = Worst Case = O(1)
        """
        if not (isinstance(damage, int)):
            raise TypeError("effective damage caused must be an integer")
        pass

    def is_paralyzed(self):
        return self.paralyzed

    def is_asleep(self) -> bool:
        """
        Method that returns True if the caller pokemon is asleep, False otherwise.

        :return: boolean value (True - asleep, False - awake)

        :time complexity: Best Case = Worst Case = O(1)
        """
        return self.asleep

    def is_confused(self) -> bool:
        """
        Method that returns True if the caller pokemon is confused, False otherwise.

        :return: boolean value (True - confused, False - not confused)

        :time complexity: Best Case = Worst Case = O(1)
        """
        return self.confused

    def attack(self, other: PokemonBase):
        """
        Method that do the attack by the caller pokemon.

        :parameter other: a pokemon which is the defending pokemon in this case

        :time complexity: Best Case = Worst Case = O(1)
        """

        attack_itself = RandomGen.random_chance(0.5)

        # check whether attacking pokemon can do a successful attack
        if not self.is_asleep():
            # confused attacking pokemon attacks itself
            if self.is_confused() and attack_itself:
                attack_poke_type_index = PokeType[self.get_poke_type()].value
                defend_poke_type_index = PokeType[self.get_poke_type()].value
                effective_attack = self.get_attack_damage() * ATTACK_MULTIPLIER[attack_poke_type_index][
                    defend_poke_type_index]

                if self.halve_effective_attack:
                    self.defend(int(effective_attack * 0.5))
                else:
                    self.defend(int(effective_attack))

                # status effect
                is_inflict = RandomGen.random_chance(0.2)

                if is_inflict:
                    if self.poke_type == 'Fire':
                        self.lose_hp(1)
                        self.halve_effective_attack = True
                    elif self.poke_type == 'Grass':
                        self.lose_hp(3)
                    elif self.poke_type == 'Water':
                        self.paralyzed = True
                    elif self.poke_type == 'Ghost':
                        self.asleep = True
                    else:
                        self.confused = True

            # confused attacking pokemon attacks the defending pokemon
            else:
                attack_poke_type_index = PokeType[self.get_poke_type()].value
                defend_poke_type_index = PokeType[other.get_poke_type()].value
                effective_attack = self.get_attack_damage() * ATTACK_MULTIPLIER[attack_poke_type_index][
                    defend_poke_type_index]

                if self.halve_effective_attack:
                    other.defend(int(effective_attack * 0.5))
                else:
                    other.defend(int(effective_attack))

                # status effect
                is_inflict = RandomGen.random_chance(0.2)

                if is_inflict:
                    if self.poke_type == 'Fire':
                        other.lose_hp(1)
                        other.halve_effective_attack = True
                    elif self.poke_type == 'Grass':
                        other.lose_hp(3)
                    elif self.poke_type == 'Water':
                        other.paralyzed = True
                    elif self.poke_type == 'Ghost':
                        other.asleep = True
                    else:
                        other.confused = True

    def get_poke_name(self) -> str:
        """
        Getter method - To return the name of the pokemon.

        :return: The name of the pokemon

        :time complexity: Best Case = Worst Case = O(1)
        """
        return self.name

    def set_poke_type(self, poke_type: PokeType) -> None:
        """
        Setter method - To set the type of the pokemon.

        :parameter hp: PokeType instance to be set for the type of the pokemon
        :return: None

        :pre-condition: poke_type must be an instance of PokeType Enum.

        :time complexity: Best Case = Worst Case = O(1)
        """
        if not (isinstance(poke_type, PokeType)):
            raise ValueError("poke_type must be an instance of PokeType Enum")
        else:
            self.poke_type = poke_type.name

    def get_poke_type(self) -> str:
        """
        Getter method - To return the type of the pokemon.

        :return: The string of the type of the pokemon

        :time complexity: Best Case = Worst Case = O(1)
        """
        return self.poke_type

    def __str__(self) -> str:
        """
        Magic method - Method for printing a string.

        :return: The string to be printed with level, name and hp of the pokemon

        :time complexity: Best Case = Worst Case = O(1), the characters of strings that are concatenated are known which will be constant.
        """
        return "LV. {} {}: {} HP".format(self.get_level(), self.get_poke_name(), self.get_hp())

    def should_evolve(self) -> bool:
        """
        Method that return True if the pokemon is not fainted and hit the base level of its evolved pokemon, False otherwise.

        :return: The boolean value. (True - not fainted and at the level that should evolve, False otherwise)

        :pre-condition: pokemon must be can evolved.

        :time complexity: Best Case = Worst Case = O(1)
        """
        # Precondition check
        if not self.can_evolve():
            raise ValueError("This pokemon cannot be evolved.")
        elif not self.is_fainted() and self.get_level() == 3 and (
                self.get_poke_name() == "Charmander" or self.get_poke_name() == "Squirtle" or self.get_poke_name() == "Haunter"):
            return True
        elif not self.is_fainted() and self.get_level() == 2 and self.get_poke_name() == "Bulbasaur":
            return True
        elif not self.is_fainted() and (
                self.get_level() == 1 or self.get_level() == 2) and self.get_poke_name() == "Gastly":
            return True
        else:
            return False

    def can_evolve(self) -> bool:
        """
        Method that returns True if the base pokemon has its evolved-to pokemon, False otherwise.

        :return: The boolean value. (True - can evolve, False cannot evolve)

        :time complexity: Best Case = Worst Case = O(1), the characters of strings that are concatenated are known which will be constant.
        """
        if self.get_poke_name() == 'Charmander' or self.get_poke_name() == 'Squirtle' or self.get_poke_name() == 'Bulbasaur' or self.get_poke_name() == 'Gastly' or self.get_poke_name() == 'Haunter':
            return True
        else:
            return False

    @abstractmethod
    def get_evolved_version(self) -> PokemonBase:
        """
        Method that returns the respective evolved pokemon.

        :return: the respective evolved pokemon

        :pre-condition: pokemon must be can evolve and should evolve.

        :time complexity: Best Case = Worst Case = O(1)
        """
        if not self.can_evolve() or not self.should_evolve():
            raise ValueError("This pokemon cannot and should not be evolved.")
        pass

    def heal(self) -> None:
        """
        Method to fully heal the pokemon. (hp = max_hp)

        :return: None

        :time complexity: Best Case = Worst Case = O(1)
        """
        self.hp = self.max_hp