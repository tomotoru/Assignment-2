from poke_team import Action, Criterion, PokeTeam
from random_gen import RandomGen
from pokemon import Bulbasaur, Charizard, Charmander, Gastly, Squirtle, Eevee
from tests.base_test import BaseTest

class TestPokeTeam(BaseTest):

    def test_init_1(self):
        """
        This is to test the __init__() method with invalid battle mode given, 3 which is not a valid input.
        """
        with self.assertRaises(ValueError):
            t = PokeTeam("YOLO", [1, 1, 1, 1, 1], 3, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.HP)
        
    def test_init_2(self):
        """
        This is to test the __init__() method with extra pokemons in a team given, which exceeding the team limit, 6.
        """
        with self.assertRaises(ValueError):
            t = PokeTeam("YOLO", [1, 1, 2, 2, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.HP)

    def test_init_3(self):
        """
        This is to test the __init__() method with correct arguments given.
        Correctly create a PokeTeam object.
        """
        t = PokeTeam("YOLO", [1, 1, 0, 1, 1], 2, PokeTeam.AI.RANDOM, criterion=Criterion.HP)
        n = t.team_name
        self.assertEqual(n, "YOLO")
        b = t.battle_mode
        self.assertEqual(b, 2)
        a = t.ai_mode
        self.assertEqual(a, "RANDOM")
        c = t.criterion
        self.assertEqual(c, "HP")
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Bulbasaur, Eevee, Charmander, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_random(self):
        """
        This is to test the random_team() method with no team size and ai mode given.
        """
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 0)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Squirtle, Gastly, Eevee, Eevee, Eevee, Eevee]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_random_1(self):
        """
        This is to test the random_team() method with team size and ai mode given.
        """
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 0, team_size=5, ai_type=PokeTeam.AI.RANDOM)
        l = len(t.team)
        self.assertEqual(l, 5)
        a = t.ai_mode
        self.assertEqual(a, "RANDOM")

    def test_random_2(self):
        """
        This is to test the random_team() method with no team size and ai mode given.
        Check if the team size is correctly generated and ai_mode is set to RANDOM.
        """
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 0)
        l = len(t.team)
        self.assertEqual((l >= 3 and l <= 6), True)
        a = t.ai_mode
        self.assertEqual(a, "RANDOM")

    def test_random_3(self):
        """
        This is to test the random_team() method by checking whether it can correctly create a team with battle mode 2.
        """
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 2, team_size=4, criterion=Criterion.HP)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Bulbasaur, Eevee, Charmander, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_return_for_fainted_pokemon(self):
        """
        This is to test the return_pokemon() method in the case that the pokemon need to be returned is fainted.
        """
        t = PokeTeam("YEAH", [0, 0, 0, 1, 4], 2, PokeTeam.AI.RANDOM, criterion=Criterion.HP)
        p = t.retrieve_pokemon()
        p.lose_hp(p.get_hp())
        t.return_pokemon(p)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Eevee, Eevee, Eevee, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_return_battle_mode_2_decreasing(self):
        """
        This is to test the return_pokemon() method in the case that the pokemon need to be returned to the team that is sorted in decreasing order.
        """
        t = PokeTeam("YEAH", [1, 1, 0, 1, 1], 2, PokeTeam.AI.RANDOM, criterion=Criterion.HP)
        p = t.retrieve_pokemon()
        p.lose_hp(4)
        t.return_pokemon(p)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Eevee, Charmander, Bulbasaur, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_return_battle_mode_2_increasing(self):
        """
        This is to test the return_pokemon() method in the case that the pokemon need to be returned to the team that is sorted in increasing order after special action.
        """
        t = PokeTeam("YEAH", [1, 1, 0, 1, 1], 2, PokeTeam.AI.RANDOM, criterion=Criterion.LV)
        t.special()
        p = t.retrieve_pokemon()
        p.level_up()
        t.return_pokemon(p)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Gastly, Bulbasaur, Charmander, Eevee]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_retrieve_pokemon_1(self):
        """
        This is to test the retrieve_pokemon() method in the case that the team is empty.
        """
        t = PokeTeam("YEAH", [0, 0, 0, 0, 0], 1, PokeTeam.AI.RANDOM)
        p = t.retrieve_pokemon()
        self.assertEqual(p, None)

    def test_retrieve_pokemon_2(self):
        """
        This is to test the retrieve_pokemon() method for team in battle mode 1.
        """
        t = PokeTeam("YEAH", [0, 0, 1, 1, 1], 1, PokeTeam.AI.RANDOM)
        p = t.retrieve_pokemon()
        expected_pokemon = Squirtle
        self.assertIsInstance(p, expected_pokemon)

    def test_retrieve_pokemon_3(self):
        """
        This is to test the retrieve_pokemon() method for team in battle mode 2.
        """
        t = PokeTeam("YEAH", [1, 2, 1, 1, 1], 2, PokeTeam.AI.RANDOM, criterion=Criterion.LV)
        p = t.retrieve_pokemon()
        expected_pokemon = Charmander
        self.assertIsInstance(p, expected_pokemon)
    
    def test_regen_team(self):
        """
        This is to test the regenerate_team() method in the case that battle mode is 2 and the criterion for sorting is HP.
        """
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 2, team_size=4, criterion=Criterion.HP)
        # This should end, since all pokemon are fainted, slowly.
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(1)
            t.return_pokemon(p)
        t.regenerate_team()
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Bulbasaur, Eevee, Charmander, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_regen_team_1(self):
        """
        This is to test the regenerate_team() method in the case that battle mode is 0.
        """
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 0, team_size=4)
        # This should end, since all pokemon are fainted, slowly.
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(1)
            t.return_pokemon(p)
        t.regenerate_team()
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Charmander, Bulbasaur, Gastly, Eevee]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_regen_team_2(self):
        """
        This is to test the regenerate_team() method in the case that battle mode is 1.
        """
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 1, team_size=4)
        # This should end, since all pokemon are fainted, slowly.
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(1)
            t.return_pokemon(p)
        t.regenerate_team()
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Charmander, Bulbasaur, Gastly, Eevee]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_regen_team_3(self):
        """
        This is to test the regenerate_team() method in the case that battle mode is 2 and the criterion for sorting is level.
        """
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 2, team_size=4, criterion=Criterion.LV)
        # This should end, since all pokemon are fainted, slowly.
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(1)
            t.return_pokemon(p)
        t.regenerate_team()
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Charmander, Bulbasaur, Gastly, Eevee]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_battle_option_attack(self):
        """
        This is to test the choose_battle_option() method in the case ai mode = ALWAYS_ATTACK, always select attack.
        """
        t = PokeTeam("Wallace", [1, 0, 0, 0, 0], 1, PokeTeam.AI.ALWAYS_ATTACK)
        p = t.retrieve_pokemon()
        e = Eevee()
        self.assertEqual(t.choose_battle_option(p, e), Action.ATTACK)

    def test_special_mode_1(self):
        t = PokeTeam("Lance", [1, 1, 1, 1, 1], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # C B S G E

    def test_battle_option_attack_1(self):
        """
        This is to test the choose_battle_option() method in the case ai mode = SWAP_ON_SUPER_EFFECTIVE, the opposing pokemon's attacks are super-effective, always select swap.
        """
        t = PokeTeam("HI", [1, 0, 0, 0, 0], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        p = t.retrieve_pokemon()
        e = Squirtle()
        self.assertEqual(t.choose_battle_option(p, e), Action.SWAP)

    def test_battle_option_attack_2(self):
        """
        This is to test the choose_battle_option() method in the case ai mode = SWAP_ON_SUPER_EFFECTIVE, the opposing pokemon's attacks are NOT super-effective, always select attack.
        """
        t = PokeTeam("VICTORY", [0, 0, 1, 0, 0], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        p = t.retrieve_pokemon()
        e = Charmander()
        self.assertEqual(t.choose_battle_option(p, e), Action.ATTACK)

    def test_battle_option_attack_3(self):
        """
        This is to test the choose_battle_option() method if the ai mode of RANDOM can provide correct output when the team has 3 heals.
        """
        t = PokeTeam("YOLO", [1, 0, 0, 0, 0], 1, PokeTeam.AI.RANDOM)
        t.heal_count = 3
        p = t.retrieve_pokemon()
        e = Eevee()
        self.assertNotEqual(t.choose_battle_option(p, e), Action.HEAL, "Action.HEAL can't be selected by the random AI mode after 3 heals")

    def test_special_mode_0(self):
        """
        This is to test the special() method in the case that a team with battle mode 0.
        Battle mode 0 special swaps the first and last pokemon on the team.
        """
        t = PokeTeam("Winner", [1, 1, 1, 1, 1], 0, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # C B S G E
        t.special()
        # E B S G C
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Eevee, Bulbasaur, Squirtle, Gastly, Charmander]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_special_mode_1_mine(self):
        """
        This is to test the special() method in the case that a team with battle mode 1 that has even number of pokemons.
        Battle mode 1 special swaps the first and second halves of the team and reverses the order of the previously front half of the team.
        """
        t = PokeTeam("YEAH", [1, 2, 1, 1, 1], 1, PokeTeam.AI.RANDOM)
        # C B B S G E
        t.special()
        # S G E B B C
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Squirtle, Gastly, Eevee, Bulbasaur, Bulbasaur, Charmander]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_special_mode_2(self):
        """
        This is to test the special() method in the case that a team with battle mode 2.
        Battle Mode 2 special reverse the sorting order of the team.
        """
        t = PokeTeam("YOLO", [1, 1, 1, 1, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.HP)
        # B  S  E  C  G
        # 13 11 10 9  6
        t.special()
        # G  C  E  S  B
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Gastly, Charmander, Eevee, Squirtle, Bulbasaur]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_special_mode_1(self):
        """
        This is to test the special() method in the case that a team with battle mode 1 that has odd number of pokemons.
        Battle mode 1 special swaps the first and second halves of the team and reverses the order of the previously front half of the team.
        The second half includes the middle pokemon.
        """
        t = PokeTeam("Lance", [1, 1, 1, 1, 1], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # C B S G E
        t.special()
        # S G E B C
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Squirtle, Gastly, Eevee, Bulbasaur, Charmander]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_string(self):
        """
        This is to test the __str__ method if it is able to print the team for battle mode 2 (array sorted list).
        """
        t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, Criterion.DEF)
        self.assertEqual(str(t), "Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP]")

    def test_string_1(self):
        """
        This is to test the __str__ method if it is able to print the team for battle mode 2 (array sorted list).
        """
        t = PokeTeam("Victory", [1, 1, 1, 1, 1], 2, PokeTeam.AI.USER_INPUT, Criterion.SPD)
        self.assertEqual(str(t), "Victory (2): [LV. 1 Charmander: 9 HP, LV. 1 Eevee: 10 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP]")

    def test_string_2(self):
        """
        This is to test the __str__ method if it is able to print the team for battle mode 1 (circular queue).
        """
        t = PokeTeam("FIGHT", [1, 1, 1, 1, 1], 1, PokeTeam.AI.ALWAYS_ATTACK)
        self.assertEqual(str(t), "FIGHT (1): [LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")

    def test_string_3(self):
        """
        This is to test the __str__ method if it is able to print the team for battle mode 0 which the pokemons are push in the array stack in reverse order (array stack).
        """
        t = PokeTeam("YOU NEVER KNOW", [0, 1, 0, 0, 0], 0, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        self.assertEqual(str(t), "YOU NEVER KNOW (0): [LV. 1 Bulbasaur: 13 HP]")

    def test_is_empty_1(self):
        """
        This is to test the is_empty() method in the case that a team with pokemons (not empty).
        Should return False as the team is not empty.
        """
        t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, Criterion.DEF)
        e = t.team.is_empty()
        self.assertEqual(e, False)

    def test_is_empty_2(self):
        """
        This is to test the is_empty() method in the case that a team with 0 pokemon.
        Should return True as the team is empty.
        """
        t = PokeTeam("FIGHT", [0, 0, 0, 0, 0], 1, PokeTeam.AI.RANDOM)
        e = t.team.is_empty()
        self.assertEqual(e, True)
        
    def test_is_empty_3(self):
        """
        This is to test the is_empty() method in the case that a team's pokemons are all fainted and not returned back.
        Should return True as the team is empty.
        """
        t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, Criterion.HP)
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(1)
            t.return_pokemon(p)
        e = t.team.is_empty()
        self.assertEqual(e, True)

