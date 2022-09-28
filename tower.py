from __future__ import annotations
from linked_list import LinkedList

from poke_team import PokeTeam, Criterion
from battle import Battle
from random_gen import RandomGen

class TowerTeam:
    def __init__(self, tower_team: PokeTeam, number_of_lives: int) -> None:
        self.tower_team = tower_team
        self.number_of_lives = number_of_lives

class BattleTower:

    tower_team_holder = LinkedList()

    def __init__(self, battle: Battle|None=None) -> None:
        self.battle = battle
    
    def set_my_team(self, team: PokeTeam) -> None:
        self.team = team
    
    def generate_teams(self, n: int) -> None:
        if n <= 0:
            raise ValueError("Invalid value passed as parameter")
        else:
            for counter in range(n):
        
                battle_mode = RandomGen.randint(0, 1)
                generated_team = PokeTeam.random_team(f"Team {n+1}", battle_mode)
                number_of_lives = RandomGen.randint(2, 10)

                tower_team = TowerTeam(generated_team, number_of_lives)
                self.tower_team_holder.insert(counter, tower_team)

    # Creating an iterator object
    def __iter__(self):
        self.index = 0
        return self

    # To perform one battle in the tower and return a tuple
    def __next__(self):

        index = self.index

        # when one round of fight is completed removing
        # all teams with 0 lives and restart from begining
        if index >= self.tower_team_holder.length:

            for index in range(self.tower_team_holder.length):
                if self.tower_team_holder[index].number_of_lives == 0:
                    if self.tower_team_holder.length == 1:
                        self.tower_team_holder.clear()
                        raise StopIteration
                    else:
                        self.tower_team_holder.delete_at_index(index)
                        index -= 1
            
            index = 0

        tower_team_obj = self.tower_team_holder[index]
        tower_team = tower_team_obj.tower_team

        # regenarating both teams
        self.team.regenerate_team()
        tower_team.regenerate_team()

        battle_result = self.battle.battle(self.team, tower_team_obj.tower_team)

        if battle_result == 2:
            raise StopIteration
        else:
            tower_team_obj.number_of_lives -= 1

        res, me, other, lives = battle_result, self.team, tower_team, tower_team_obj.number_of_lives

        index += 1

        return (res, me, other, lives)

class BattleTowerIterator:
    
    def avoid_duplicates(self):
        raise NotImplementedError()

    def sort_by_lives(self):
        # 1054
        raise NotImplementedError()

