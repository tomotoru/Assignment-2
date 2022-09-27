from __future__ import annotations

"""
PokeTeam File for all PokeTeam related method implementation.

Create the PokeTeam class.
"""
__author__ = "Scaffold by Jackson Goerner, Code by How Yew Wai and Koh Zi Xin"

from enum import Enum, auto
from pokemon_base import PokemonBase, ATTACK_MULTIPLIER, PokeType
from pokemon import *
from random_gen import RandomGen
from stack_adt import ArrayStack
from queue_adt import CircularQueue
from array_sorted_list import ArraySortedList, ListItem 

class Action(Enum):
    """
    This is the class of Action, the members are ATTACK, SWAP, HEAL and SPECIAL.
    """
    ATTACK = auto()
    SWAP = auto()
    HEAL = auto()
    SPECIAL = auto()
    
class Criterion(Enum):
    """
    This is the class of Criterion, the members are SPD, HP, LV and DEF.
    """
    SPD = auto()
    HP = auto()
    LV = auto()
    DEF = auto()

class PokeTeam:
    """
    This is the class of PokeTeam, which has 1 class (AI) and 13 instance methods.

    Unless stated otherwise, all instance methods below have best / worst case complexity O(1).
    """

    class AI(Enum):
        """
        This is the class of AI, the members are ALWAYS_ATTACK, SWAP_ON_SUPER_EFFECTIVE, RANDOM and USER_INPUT.
        This can be used to select which AI to follow.
        """
        ALWAYS_ATTACK = auto()
        SWAP_ON_SUPER_EFFECTIVE = auto()
        RANDOM = auto()
        USER_INPUT = auto()

    # PokeTeam class variables
    TEAM_LIMIT = 6
    NUM_OF_HEALS = 3
    BASE_POKEMON = [Charmander, Bulbasaur, Squirtle, Gastly, Eevee]
    POKEDEX_ORDERING = [Charmander, Charizard, Bulbasaur, Venusaur, Squirtle, Blastoise, Gastly, Haunter, Gengar, Eevee]

    def __init__(self, team_name: str, team_numbers: list[int], battle_mode: int, ai_type: PokeTeam.AI, criterion = None, criterion_value = None) -> None:
        """
        Constructor of the class that initializes the required instance variables. 

        4 compulsory parameters:
        :parameter team_name: The team name of the PokeTeam
        :parameter team_numbers: A list that specifies how many Charmanders/Bulbasaurs/Squirtles/Gastlys/Eevees should be added to the team.
        :parameter battle_mode: The battle mode of the PokeTeam
        :parameter ai_type: The AI mode of the PokeTeam

        2 optional parameters
        :parameter criterion: The criterion to sort the order of the pokemons in the team
        :parameter criterion_value: The criterion_value

        :return: None

        :time complexity: Best Case = Worst Case = O(1)
        """
        # Pre condition check for argument, team_name
        if not(isinstance(team_name, str)):
            raise TypeError("team name should be in str type")
        else:
            self.team_name = team_name

        # Pre condition check for argument, team_numbers
        if sum(team_numbers) > 6:
            raise ValueError("Total number of pokemons in a team must not exceed 6")
        else:
            self.team_numbers = team_numbers
        
        # Pre condition check for argument, battle_mode
        # invalid battle_mode
        if battle_mode not in [0, 1, 2]:
            raise ValueError("Invalid battle mode")
        else:
            # valid battle_mode
            self.battle_mode = battle_mode
            if self.battle_mode == 0:
                # battle_mode 0 is handled by using ArrayStack
                self.team = ArrayStack(self.TEAM_LIMIT)
            elif self.battle_mode == 1:
                # battle_mode 1 is handled by using CircularQueue
                self.team = CircularQueue(self.TEAM_LIMIT)
            elif self.battle_mode == 2:
                # battle_mode 2 is handled by using ArraySortedList
                self.team = ArraySortedList(self.TEAM_LIMIT)
        
        # Pre condition check for argument, ai_type
        if not(isinstance(ai_type, PokeTeam.AI)):
            raise ValueError("ai_type must be an instance of PokeTeam.AI Enum")
        else:
            self.ai_mode = ai_type.name

        # Pre condition check for argument, criterion
        # if battle_mode = 2 and no criterion given
        if self.battle_mode == 2 and not(isinstance(criterion, Criterion)):
            raise ValueError("Battle mode 2 required a criterion")
        elif self.battle_mode == 2 and isinstance(criterion, Criterion):
            self.criterion = criterion.name
            
        self.criterion_value = criterion_value
        self.heal_count = 0
        self.num_of_special = 0
        self.assign_team(self.battle_mode)
    
    def get_criterion(self, criterion: Criterion, poke: PokemonBase) -> int:
        """
        Method that returns an integer which is either the speed, hp value, level and defence.

        :return: integer value

        :time complexity: Best Case = Worst Case = O(1)
        """
        if criterion == "SPD":
            return poke.get_speed()
        elif criterion == "HP":
            return poke.get_hp()
        elif criterion == "LV":
            return poke.get_level()
        elif criterion == "DEF":
            return poke.get_defence()
    
    def assign_team(self, battle_mode: int) -> None:
        """
        Method that used to assign pokemons in the team in correct order for each battle mode.

        :parameter battle_mode: The battle mode of the PokeTeam

        :time complexity: Best Case = Worst Case = O(1)
        """
        # The last pokemon in the team push in the ArrayStack first.
        if self.battle_mode == 0:
            for i in range(1, len(self.team_numbers) + 1):
                for j in range(self.team_numbers[len(self.team_numbers) - i]):
                    self.team.push(self.BASE_POKEMON[len(self.team_numbers) - i]())

        # Append the pokemon in the team one by one by using the CircularQueue.
        elif self.battle_mode == 1:
            for i in range(len(self.team_numbers)):
                for j in range(self.team_numbers[i]):
                    self.team.append(self.BASE_POKEMON[i]())
    
        # The pokemon is added in the team by decreasing default by using the ArraySortedList.
        elif self.battle_mode == 2:
            for i in range(len(self.team_numbers)):
                for j in range(self.team_numbers[i]):
                    self.team.add(ListItem(self.BASE_POKEMON[i](), - self.get_criterion(self.criterion, self.BASE_POKEMON[i]())))
            
            # all pokemons have same base level
            if self.criterion == "LV":
                self.tie_podekex_order(self.team)
            
    def tie_podekex_order(self, list: ArraySortedList) -> None:
        """
        Method that used to sort the pokemons in pokedex order as they are having the same value for criterion.

        :parameter list: team in ArraySortedList

        :time complexity: Best Case = Worst Case = O(1)
        """
        temp_array_sorted_list = ArraySortedList(len(list))

        # go through the team
        for i in range(len(list)):
            # check if it is in decreasing order
            if self.num_of_special % 2 == 0 and list[i].key < 0:
                # search the pokemon of the team in POKEDEX_ORDERING to sort them by the pokedex order
                for j in range(len(self.POKEDEX_ORDERING)):
                    if isinstance(list[i].value, self.POKEDEX_ORDERING[j]):
                        # use the value of pokedex order as key to sort the team
                        temp_array_sorted_list.add(ListItem(list[i].value, j))
        
        # clear the pokemons                 
        self.team.clear()

        # go through the temporary team
        for i in range(len(temp_array_sorted_list)):
            # add the pokemons in the team
            self.team.add(ListItem(temp_array_sorted_list[i].value, i))

    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size = None, ai_mode = None, **kwargs) -> PokeTeam:
        """
        Method that used to create a random team by the team_name, battle_mode, team_size and ai_mode given.

        2 compulsory parameters:
        :parameter team_name: The team name of the PokeTeam
        :parameter battle_mode: The battle mode of the PokeTeam

        2 optional parameters:
        :parameter team_size: Total number of pokemons in the team
        :parameter ai_mode: The AI mode of the PokeTeam

        :**kwargs: This is used to pass a keyworded variable-length argument list, in this case it is for criterion.
        
        :time complexity: Best Case = Worst Case = O(1)
        """
        # if no team_size given
        if team_size == None:
            team_size = RandomGen.randint(PokeTeam.TEAM_LIMIT // 2, PokeTeam.TEAM_LIMIT)
        
        # create a ArraySortedList named sorted_list to help in getting the team_numbers
        sorted_list = ArraySortedList(PokeTeam.TEAM_LIMIT)
        sorted_list.add(ListItem(0, 0))
        sorted_list.add(ListItem(team_size, team_size))

        # generate 4 random numbers from 0 to team size and insert them into the sorted_list
        for i in range(0, 4):
            num = RandomGen.randint(0, team_size)
            sorted_list.add(ListItem(num, num))

        # use an inbuilt list to get all the numbers in int type to do calculation
        temp = []
        for i in range(len(sorted_list)):
            num_of_each_pokemon = int(str(sorted_list[i]))
            temp.append(num_of_each_pokemon)

        # use an inbuilt list to store the team_numbers
        team_numbers = []
        for i in range(1, len(temp)):
            team_numbers.append(temp[i] - temp[i - 1])

        # if ai_mode is not given, pick PokeTeam.AI.RANDOM
        if ai_mode == None:
            ai_mode = PokeTeam.AI.RANDOM

        # get the criterion passed by **kwargs if battle_mode is 2
        if battle_mode == 2:
            for key, value in kwargs.items():
                return PokeTeam(team_name, team_numbers, battle_mode, ai_mode, criterion=value)
        else:
            return PokeTeam(team_name, team_numbers, battle_mode, ai_mode)
        
    def return_pokemon(self, poke: PokemonBase) -> None:
        """
        Method that used to return a pokemon to the team from the field.

        :parameter poke: Pokemon object to be returned
        
        :time complexity: Best Case = Worst Case = O(1)
        """
        if self.team.is_full():
            raise Exception("The team is full and cannot return pokemon back")
        # fainted pokemon not returned bac to the team
        elif not poke.is_fainted():
            if self.battle_mode == 0:
                self.team.push(poke)
            elif self.battle_mode == 1:
                self.team.append(poke)
            elif self.battle_mode == 2:
                # team in decreasing order
                if self.num_of_special % 2 == 0:
                    self.team.add(ListItem(poke, - self.get_criterion(self.criterion, poke)))
                # team in increasing order
                else:
                    self.team.add(ListItem(poke, self.get_criterion(self.criterion, poke)))
            
    def retrieve_pokemon(self) -> PokemonBase | None:
        """
        Method that used to retrieve a pokemon from the team to the field.

        :return: Pokemon object retrieved or None (if the team is empty)
        
        :time complexity: Best Case = Worst Case = O(1)
        """
        if self.team.is_empty():
            return None
        elif self.battle_mode == 0:
            retrieved_pokemon = self.team.pop()
            return retrieved_pokemon
        elif self.battle_mode == 1:
            retrieved_pokemon = self.team.serve()
            return retrieved_pokemon
        elif self.battle_mode == 2:
            retrieved_pokemon = self.team.delete_at_index(0)
            return retrieved_pokemon.value

    def special(self) -> None:
        """
        Method that used to do the special action on the team.

        For battle mode 0: Battle mode 0 special swaps the first and last pokemon on the team.
        For battle mode 1: Battle mode 1 special swaps the first and second halves of the team and reverses the order of the previously front half of the team.
        For battle mode 2: Battle mode 2 special reverse the sorting order of the team.
        """
        # battle mode 0
        if self.battle_mode == 0:
            after_special = ArrayStack(len(self.team))
            # first pokemon
            after_special.push(self.team.pop())
            # pokemon between first pokemon and last pokemon
            for i in range(1, len(self.team)):
                after_special.push(self.team[i])
            # last pokemon
            after_special.push(self.team[0])

            self.team.clear()
            for i in range(len(after_special)):
                self.team.push(after_special[i])
            
            self.num_of_special += 1

        # battle mode 1
        elif self.battle_mode == 1:
            # if a team has odd numbers of pokemons
            if len(self.team) % 2 == 0:
                first_halve = CircularQueue(int(len(self.team) / 2))
                second_halve = CircularQueue(int(len(self.team) / 2))
                half_line = int(len(self.team) / 2)
                for i in range(len(self.team)):
                    if i < half_line:
                        first_halve.append(self.team.serve())
                    else:
                        second_halve.append(self.team.serve())
            # if a team has even numbers of pokemons
            else:
                first_halve = CircularQueue(len(self.team) // 2)
                second_halve = CircularQueue(len(self.team) // 2 + 1)
                for i in range(len(self.team)):
                    if i < len(self.team) // 2:
                        first_halve.append(self.team.serve())
                    else:
                        second_halve.append(self.team.serve())
        
            # swaps the first and second halves of the team and reverses the order of the first_halve
            for i in range(len(second_halve)):
                self.team.append(second_halve[i])
            for i in range(len(first_halve) - 1, -1, -1):
                self.team.append(first_halve[i])

            self.num_of_special += 1

        # battle mode 2
        elif self.battle_mode == 2:
            reverse_team = ArraySortedList(len(self.team))
            # add the pokemons to the ArraySortedList, named reverse_team
            for i in range(len(self.team)):
                reverse_team.add(ListItem(self.team[i].value, i))

            # clear the pokemons in the team
            self.team.clear()

            # add the pokemons into the team starting from the last pokemon in the team
            for i in range(len(reverse_team) - 1, -1, -1):
                self.team.add(ListItem(reverse_team[i].value, - i))
            
            self.num_of_special += 1
    
    def regenerate_team(self) -> None:
        """
        Method that used to regenerate the team.
        """
        self.team.clear()
        if self.battle_mode == 0:
            self.team = ArrayStack(self.TEAM_LIMIT)
        elif self.battle_mode == 1:
            self.team = CircularQueue(self.TEAM_LIMIT)
        elif self.battle_mode == 2:
            self.team = ArraySortedList(self.TEAM_LIMIT)

        # call the assign_team() method to assign the pokemons in the team based on the team's battle mode
        self.assign_team(self.battle_mode)

    def __str__(self) -> str:
        """
        Magic method - Method for printing a string (team).

        :return: The string to be printed with team_name, battle_mode and the pokemons with their level and hp
        """
        empty_string = ""

        # pokemons are pushed by reversing order into the team (ArrayStack) in battle mode 1
        if self.battle_mode == 0:
            # access the pokemon by reversing order
            for i in range(len(self.team) - 1, -1, -1):
                empty_string += str(self.team[i])
                if i != 0:
                    empty_string += ", "
        else:
            for i in range(len(self.team)):
                empty_string += str(self.team[i])
                if i != len(self.team) - 1:
                    empty_string += ", "

        return "{0} ({1}): [{2}]".format(self.team_name, self.battle_mode, empty_string)

    def is_empty(self) -> bool:
        """
        Method that returns True if the caller team is empty, False otherwise.
        
        :return: boolean value (True - team is empty, False - team is not empty)
        """
        return self.team.is_empty()
    
    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        """
        Method that used to choose battle option of the team.

        :parameter my_pokemon: caller team pokemon
        :parameter their_pokemon: opposing team pokemon

        :return: one of the members of Action class
        """
        # ALWAYS_ATTACK always choose attack action
        if self.ai_mode == "ALWAYS_ATTACK":
            return Action.ATTACK

        # SWAP_ON_SUPER_EFFECTIVE can do attack or swap action depends on the opposing pokemon
        elif self.ai_mode == "SWAP_ON_SUPER_EFFECTIVE":
            attack_poke_type_index = PokeType[their_pokemon.get_poke_type()].value
            defend_poke_type_index = PokeType[my_pokemon.get_poke_type()].value
            opposing_pokemon_effective_attack = their_pokemon.get_attack_damage() * ATTACK_MULTIPLIER[attack_poke_type_index][defend_poke_type_index]

            if opposing_pokemon_effective_attack >= (1.5 * their_pokemon.get_attack_damage()):
                return Action.SWAP
            else:
                return Action.ATTACK

        # RANDOM takes one of the actions from the class Action
        elif self.ai_mode == "RANDOM":
            actions = list(Action)
            # more than 3 heals, cannot choose heal action
            if self.heal_count >= self.NUM_OF_HEALS:
                actions.remove(Action.HEAL)
                return actions[RandomGen.randint(0, len(actions) - 1)]
            else:
                action = actions[RandomGen.randint(0, len(actions) - 1)]
                if action == Action.HEAL:
                    self.heal_count += 1
                return action

        # USER_INPUT
        else:
            actions = list(Action)
            user_input_prompt = "Please enter action selection (1 - 4): "
            invalid_type_input_prompt = "Please input numbers within 1 - 4"

            valid_input = False
            while not valid_input:
                try:
                    user_input = int(input(user_input_prompt))
                    if user_input < 1 or user_input > len(actions):
                        raise ValueError
                        
                except ValueError:
                    print(invalid_type_input_prompt)

                else:
                    action = actions[user_input - 1]
                    valid_input = True
            
            return action
    
    @classmethod
    def leaderboard_team(cls):
        raise NotImplementedError()
