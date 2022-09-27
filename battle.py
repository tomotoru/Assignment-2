"""
This task implements the battle logic described in the Background section of the assessment
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from enum import Enum
from gc import is_finalized
from pokemon_base import PokemonBase
from random_gen import RandomGen
from poke_team import Action, PokeTeam, Criterion
from print_screen import print_game_screen

class Battle:

    def __init__(self, verbosity=0) -> None:
        self.verbosity = verbosity

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        """
        This method is used to perform the battle between team1 and team2. This battle should return 0, 1 or 2
        which represents draw, and 1 or 2 representing player 1 or 2 winning respectively
        """
        # Retrieve the pokemon from team1 and team2
        poke1 = team1.retrieve_pokemon()
        poke2 = team2.retrieve_pokemon()
        lose1 = False
        lose2 = False

        while True:
            # print(team1pokemon, team2pokemon)
            action1 = team1.choose_battle_option(poke1, poke2)
            action2 = team2.choose_battle_option(poke2, poke1)
            # print(team1action, team2action)


            if action1 == Action.SWAP:
                team1.return_pokemon(poke1)
                poke1 = team1.retrieve_pokemon()

            if action2 == Action.HEAL:
                team2.return_pokemon(poke2)
                poke2 = team2.retrieve_pokemon()

            if action1 ==  Action.HEAL:
                if team1.heal_count <= 3:
                    poke1.heal()
                else:
                    team1.return_pokemon(poke1)
                    team2.return_pokemon(poke2)
                    return 2

            if action2 ==  Action.HEAL:
                if team2.heal_count <= 3:
                    poke2.heal()
                else:
                    team1.return_pokemon(poke1)
                    team2.return_pokemon(poke2)
                    return 1

            if action1 == Action.SPECIAL:
                team1.return_pokemon(poke1)
                team1.special()
                poke1 = team1.retrieve_pokemon()

            if action2 == Action.SPECIAL:
                team2.return_pokemon(poke2)
                team2.special()
                poke2 = team2.retrieve_pokemon()

            if action1 == Action.ATTACK:
                poke1_speed = poke1.get_speed()
                poke2_speed = poke2.get_speed()
                if poke1.is_paralyzed():
                    poke1_speed = poke1.get_speed()/2
                if poke2.is_paralyzed():
                    poke2_speed = poke2.get_speed()/2

                if poke1_speed >= poke2_speed:
                    poke1.attack(poke2)
                    if not poke2.is_fainted():
                        poke2.attack(poke1)

                else:
                    poke2.attack(poke1)
                    if not poke1.is_fainted():
                        poke1.attack(poke2)

            if not (poke1.is_fainted() and poke2.is_fainted()):
                poke1.lose_hp(1)
                poke2.lose_hp(1)

            if not poke1.is_fainted() and poke2.is_fainted():
                poke1.level_up()

                if poke1.can_evolve():
                    if poke1.should_evolve():
                        poke1 = poke1.get_evolved_version()

            elif poke1.is_fainted() and not poke2.is_fainted():
                poke2.level_up()

                if poke2.can_evolve():
                    if poke2.should_evolve():
                        poke2 = poke2.get_evolved_version()

            if poke1.is_fainted() and team1.is_empty():
                lose1 = True

            elif poke1.is_fainted() and not team1.is_empty():
                poke1 = team1.retrieve_pokemon()

            if poke2.is_fainted() and team2.is_empty():
                lose2 = True

            elif poke2.is_fainted() and not team2.is_empty():
                poke2 = team2.retrieve_pokemon()

            if lose1 and lose2:
                return 0

            elif not lose1 and lose2:
                return 1

            elif lose1 and not lose2:
                return 2

if __name__ == "__main__":
    '''
    b = Battle(verbosity=3)
    RandomGen.set_seed(16)
    t1 = PokeTeam.random_team("Cynthia", 2, criterion=Criterion.SPD)
    t1.ai_type = PokeTeam.AI.USER_INPUT
    t2 = PokeTeam.random_team("Barry", 1)
    print(b.battle(t1, t2))
    '''
    RandomGen.set_seed(192837465)
    team1 = PokeTeam("Brock", [1, 1, 1, 1, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.HP)
    team2 = PokeTeam("Misty", [0, 0, 0, 3, 3], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.SPD)
    b = Battle(verbosity=0)
    print(b.battle(team1, team2))
