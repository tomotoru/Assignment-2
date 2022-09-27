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

    def __init__(self, verbosity=0) -> None:
        self.verbosity = verbosity

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        """
        This method is used to perform the battle between team1 and team2. This battle should return 0, 1 or 2
        which represents draw, and 1 or 2 representing player 1 or 2 winning respectively
        """
        # Retrieve the pokemon from team1 and team2
        team1_pokemon = team1.retrieve_pokemon()
        team2_pokemon = team2.retrieve_pokemon()

        while True:

            team1_action = team1.choose_battle_option(team1_pokemon, team2_pokemon)
            team2_action = team2.choose_battle_option(team2_pokemon, team1_pokemon)

            # if ACTION = swap, return_pokemon and retrieve_pokemon
            if team1_action == Action(2) or team2_action == Action(2):
                if team1_action == Action(2):
                    team1.return_pokemon(team1_pokemon)
                    team1_pokemon = team1.retrieve_pokemon()
                else:
                    team2.return_pokemon(team2_pokemon)
                    team2_pokemon = team2.retrieve_pokemon()

            # if ACTION = special, return_pokemon, special action (according to the battle mode) and retrieve_pokemon
            if team1_action == Action(4) or team2_action == Action(4):
                if team1_action == Action(4):
                    team1.return_pokemon(team1_pokemon)
                    team1.special()
                    team1_pokemon = team1.retrieve_pokemon()
                else:
                    team2.return_pokemon(team2_pokemon)
                    team2.special()
                    team2_pokemon = team2.retrieve_pokemon()

            # if ACTION = heal, check if less than thrice, else return the pokemon back to the team and team2 wins
            if team1_action == Action(3) or team2_action == Action(3):
                if team1_action == Action(3):
                    if team1.heal_count >= team1.NUM_OF_HEALS:
                        return 2
                    else:
                        team1.heal_count = team1.heal_count + 1
                        team1_pokemon.heal()
                else:
                    if team2.heal_count >= team2.NUM_OF_HEALS:
                        return 1
                    else:
                        team2.heal_count = team2.heal_count + 1
                        team2_pokemon.heal()

            """
            If ACTION = attack, check if the pokemon is inflicted with "paralysis", if it is, halves the speed of
            the pokemon, else get the current speed of the pokemon. 
            """
            if team1_action == Action(1) and team2_action == Action(1):
                if  team1_pokemon.is_paralysis():
                    team1_pokemon_speed = int(team1_pokemon.get_speed() // 2)
                else:
                    team1_pokemon_speed = team1_pokemon.get_speed()

                if team2_pokemon.is_paralysis():
                    team2_pokemon_speed = int(team2_pokemon.get_speed() // 2)
                else:
                    team2_pokemon_speed = team2_pokemon.get_speed()

                # If team1_pokemon_speed greater than team2_pokemon_speed, team1_pokemon attack team2_pokemon, and if
                # team2_pokemon is not fainted, team2_pokemon will attack team1_pokemon
                if team1_pokemon_speed > team2_pokemon_speed:
                    team1_pokemon.attack(team2_pokemon)
                    if not team2_pokemon.is_fainted():
                        team2_pokemon.attack(team1_pokemon)

                # If team2_pokemon_speed greater than team1_pokemon_speed, team2_pokemon attack team1_pokemon, and if
                # team1_pokemon is not fainted, team1_pokemon will attack team2_pokemon
                elif team2_pokemon_speed > team1_pokemon_speed:
                    team2_pokemon.attack(team1_pokemon)
                    if not team1_pokemon.is_fainted():
                        team1_pokemon.attack(team2_pokemon)

                # If team1_pokemon_speed equals to team2_pokemon_speed, team1_pokemon attack team2_pokemon, and
                # team2_pokemon will attack team1_pokemon
                elif team1_pokemon_speed == team2_pokemon_speed:
                    team1_pokemon.attack(team2_pokemon)
                    team2_pokemon.attack(team1_pokemon)

            elif team1_action == Action(1):
                team1_pokemon.attack(team2_pokemon)

            elif team2_action == Action(1):
                team2_pokemon.attack(team1_pokemon)

            # print("Pokemon1 fainted", team1pokemon.is_fainted())
            # print("Pokemon2 fainted", team2pokemon.is_fainted())

            # if both pokemon still alive, -1 HP
            if not team1_pokemon.is_fainted() and not team2_pokemon.is_fainted():
                team1_pokemon.lose_hp(1)
                team2_pokemon.lose_hp(1)

            # check is_fainted for one of the pokemons, the other pokemon will level up (update HP)
            if not team1_pokemon.is_fainted() and team2_pokemon.is_fainted():
                team1_pokemon.level_up()

            elif not team2_pokemon.is_fainted() and team1_pokemon.is_fainted():
                team2_pokemon.level_up()

            # check if pokemon have not fainted and can evolve, they evolve
            if not team1_pokemon.is_fainted() and not team2_pokemon.is_fainted():
                if team1_pokemon.should_evolve():
                    team1_pokemon = team1_pokemon.get_evolved_version()

                if team2_pokemon.should_evolve():
                    team2_pokemon = team2_pokemon.get_evolved_version()

            # Fainted pokemon are returned and a new pokemon is retrieved from the team.
            # If no pokemon can be retrieved (the team is empty), then the opposing player
            # wins. If both teams are empty, the result is a draw it will return 0
            if team1_pokemon.is_fainted() or team2_pokemon.is_fainted():

                # if both pokemon is fainted then team which is empty will lose else
                # fainted pokemon will be returned and new pokemon will be retrived
                if team1_pokemon.is_fainted() and team2_pokemon.is_fainted():
                    if team1.is_empty() and team2.is_empty():
                        team1.return_pokemon(team1_pokemon)
                        team2.return_pokemon(team2_pokemon)
                        return 0
                    elif not team1.is_empty() and team2.is_empty():
                        team1.return_pokemon(team1_pokemon)
                        team2.return_pokemon(team2_pokemon)
                        return 1
                    elif team1.is_empty() and not team2.is_empty():
                        team1.return_pokemon(team1_pokemon)
                        team2.return_pokemon(team2_pokemon)
                        return 2
                    else:
                        team1.return_pokemon(team1_pokemon)
                        team2.return_pokemon(team2_pokemon)
                        team1_pokemon = team1.retrieve_pokemon()
                        team2_pokemon = team2.retrieve_pokemon()

                elif not team1_pokemon.is_fainted() and team2_pokemon.is_fainted():
                    if team2.is_empty():
                        team2.return_pokemon(team2_pokemon)
                        return 1
                    else:
                        team2.return_pokemon(team2_pokemon)
                        team2_pokemon = team2.retrieve_pokemon()
                else:
                    if team1.is_empty():
                        team1.return_pokemon(team1_pokemon)
                        return 2
                    else:
                        team1.return_pokemon(team1_pokemon)
                        team1_pokemon = team1.retrieve_pokemon()
