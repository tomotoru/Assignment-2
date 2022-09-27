"""
This task implements the battle logic described in the Background section of the assessment
"""
__author__ = "Scaffold by Jackson Goerner, Code by Tan Shuen Y'ng and Joanna Moy"

from random_gen import RandomGen
from battle import *
from poke_team import *
from pokemon import *
from stack_adt import * 

class Battle:

    def init(self, verbosity=0) -> None:
        self.verbosity = verbosity

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        """
        This method is used to perform the battle between team1 and team2. This battle should return 0, 1 or 2
        which represents draw, and 1 or 2 representing player 1 or 2 winning respectively
        """
        # Retrieve the pokemon from team1 and team2
        team1pokemon = team1.retrieve_pokemon()
        team2pokemon = team2.retrieve_pokemon()

        while True:
            #print(team1pokemon, team2pokemon)
            team1action = team1.choose_battle_option(team1pokemon, team2pokemon)
            team2action = team2.choose_battle_option(team2pokemon, team1pokemon)
            #print(team1action, team2action)

            # if ACTION = swap, return_pokemon and retrieve_pokemon
            if team1action == Action(2):
                team1.return_pokemon(team1pokemon)
                team1pokemon = team1.retrieve_pokemon()

            if team2action == Action(2):
                team2.return_pokemon(team2pokemon)
                team2pokemon = team2.retrieve_pokemon()

            # if ACTION = special, return_pokemon, special action (according to the battle mode) and retrieve_pokemon
            if team1action == Action(4):
                team1.return_pokemon(team1pokemon)
                team1.special()
                team1pokemon = team1.retrieve_pokemon()

            if team2action == Action(4):
                team2.return_pokemon(team2pokemon)
                team2.special()
                team2pokemon = team2.retrieve_pokemon()

            # if ACTION = heal, check if less than thrice, else return the pokemon back to the team and team2 wins
            if team1action == Action(3):
                if team1.heal_count <= 3:
                    team1pokemon.heal()
                else:
                    team1.return_pokemon(team1pokemon)
                    team2.return_pokemon(team2pokemon)
                    return 2

            # if ACTION = heal, check if less than thrice, else return the pokemon back to the team and team1 wins
            if team2action == Action(3):
                if team2.heal_count <= 3:
                    team2pokemon.heal()
                else:
                    team1.return_pokemon(team1pokemon)
                    team2.return_pokemon(team2pokemon)
                    return 1

            """
            If ACTION = attack, check if the pokemon_status_effect is equal to "paralysis", if it is, halves the speed of
            the pokemon, else get the current speed of the pokemon. 
            """
            if team1action == Action(1) and team2action == Action(1):
                if team1pokemon.status_effect == "PARALYSIS":
                    team1pokemon_speed = int(team1pokemon.get_speed() // 2)
                else:
                    team1pokemon_speed = team1pokemon.get_speed()

                if team2pokemon.status_effect == "PARALYSIS":
                    team2pokemon_speed = int(team2pokemon.get_speed() // 2)
                else:
                    team2pokemon_speed = team2pokemon.get_speed()

                # If team1pokemon_speed greater than team2pokemon_speed, team1pokemon attack team2pokemon, and if
                # team2pokemon is not fainted, team2pokemon will attack team1pokemon
                if team1pokemon_speed > team2pokemon_speed:
                    team1pokemon.attack(team2pokemon)
                    if not team2pokemon.is_fainted():
                        team2pokemon.attack(team1pokemon)

                # If team2pokemon_speed greater than team1pokemon_speed, team2pokemon attack team1pokemon, and if
                # team1pokemon is not fainted, team1pokemon will attack team2pokemon
                elif team2pokemon_speed > team1pokemon_speed:
                    team2pokemon.attack(team1pokemon)
                    if not team1pokemon.is_fainted():
                        team1pokemon.attack(team2pokemon)

                # If team1pokemon_speed equals to team2pokemon_speed, team1pokemon attack team2pokemon, and
                # team2pokemon will attack team1pokemon
                elif team1pokemon_speed == team2pokemon_speed:
                    team1pokemon.attack(team2pokemon)
                    team2pokemon.attack(team1pokemon)

            elif team1action == Action(1):
                team1pokemon.attack(team2pokemon)

            elif team2action == Action(1):
                team2pokemon.attack(team1pokemon)

            # print("Pokemon1 fainted", team1pokemon.is_fainted())
            # print("Pokemon2 fainted", team2pokemon.is_fainted())

            # if both pokemon still alive, -1 HP
            if not team1pokemon.is_fainted() and not team2pokemon.is_fainted():
                team1pokemon.lose_hp(1)
                team2pokemon.lose_hp(1)

            # check is_fainted for one of the pokemons, the other pokemon will level up (update HP)
            if team1pokemon.is_fainted() and not team2pokemon.is_fainted():
                team2pokemon.level_up()

            elif team2pokemon.is_fainted() and not team1pokemon.is_fainted():
                team1pokemon.level_up()

            if team2pokemon.should_evolve():
                team2pokemon = team2pokemon.get_evolved_version()

            if team1pokemon.should_evolve():
                team1pokemon = team1pokemon.get_evolved_version()

            #print(team1pokemon,team2pokemon)

            # if team1pokemon faint and team2pokemon faint, if both team is empty, return the pokemons back to their
            # own team and this battle result 0 which is draw
            if team1pokemon.is_fainted() and team2pokemon.is_fainted():
                if team1.is_empty() and team2.is_empty():
                    team1.return_pokemon(team1pokemon)
                    team2.return_pokemon(team2pokemon)
                    return 0

                # if team1 is not empty and team2 is empty, return the pokemons back to their
                # own team and this battle result 1 which won by player 1
                elif not team1.is_empty() and team2.is_empty():
                    team1.return_pokemon(team1pokemon)
                    team2.return_pokemon(team2pokemon)
                    return 1

                # if team1 is empty and team2 is not empty, return the pokemons back to their
                # own team and this battle result 2 which won by player 2
                elif team1.is_empty() and not team2.is_empty():
                    team1.return_pokemon(team1pokemon)
                    team2.return_pokemon(team2pokemon)
                    return 2

            # if team1pokemon faint, if team1 is empty, return the pokemons back to their
            # own team and this battle result 2 which won by player 2 else if team1 is not empty, retrieve
            # another pokemon from the team
            elif team1pokemon.is_fainted():
                if team1.is_empty():
                    team1.return_pokemon(team1pokemon)
                    team2.return_pokemon(team2pokemon)
                    return 2
                else:
                    team1pokemon = team1.retrieve_pokemon()

            # if team2pokemon faint, if team2 is empty, return the pokemons back to their
            # own team and this battle result 1 which won by player 1 else if team2 is not empty, retrieve
            # another pokemon from the team
            elif team2pokemon.is_fainted():
                if team2.is_empty():
                    team2.return_pokemon(team2pokemon)
                    team1.return_pokemon(team1pokemon)
                    return 1
                else:
                    team2pokemon = team2.retrieve_pokemon()

            print(team1pokemon,team2pokemon)
