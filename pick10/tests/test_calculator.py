from django.test import TestCase
from pick10.database import Database
from pick10.calculator import *
from pick10.models import *
from unit_test_database import *

# This class tests the calculator.py file load_week_data function
class CalculatorTests(TestCase):

    @classmethod
    def setUpClass(cls):
        test_db = UnitTestDatabase()
        test_db.load_historical_data_for_week(2013,1)
        test_db.load_historical_data_for_week(2013,2)

    def setUp(self):
        self.db = Database()
        self.week1 = self.db.load_week_data(2013,1)
        self.week2 = self.db.load_week_data(2013,2)
        self.calc = CalculateResults(data=self.week1)

    # function name decode:  
    # test_ : each function to test must start with test_ (unittest requirement)
    # _t<number>_ : unique identifier used to specify this test function
    # _<name> : this is the name of the function in calculator.py that is being tested
    def test_t1_get_team_player_picked_to_win(self):
        self.__t1_invalid_player()
        self.__t1_invalid_game()
        self.__t1_game_none()
        self.__t1_team1_winner()
        self.__t1_team2_winner()

    def test_t2_get_team_name_player_picked_to_win(self):
        self.__t2_invalid_player()
        self.__t2_invalid_game()
        self.__t2_game_none()
        self.__t2_team1_winner()
        self.__t2_team2_winner()
        self.__t2_winner_missing()

    def test_t3_is_team1_winning_pool(self):
        self.__t3_bad_game_favored_value()
        self.__t3_team1_ahead()
        self.__t3_team1_behind()
        self.__t3_team1_ahead_in_pool_behind_in_game()
        self.__t3_team1_behind_in_pool_ahead_in_game()
        self.__t3_team1_boundary_case1()
        self.__t3_team1_boundary_case2()
        self.__t3_team1_boundary_case3()
        self.__t3_team1_boundary_case4()

    def test_t4_is_team2_winning_pool(self):
        self.__t4_bad_game_favored_value()
        self.__t4_team2_ahead()
        self.__t4_team2_behind()
        self.__t4_team2_ahead_in_pool_behind_in_game()
        self.__t4_team2_behind_in_pool_ahead_in_game()
        self.__t4_team2_boundary_case1()
        self.__t4_team2_boundary_case2()
        self.__t4_team2_boundary_case3()
        self.__t4_team2_boundary_case4()

    def test_t5_get_pool_game_winner(self):
        self.__t5_game_none()
        self.__t5_game_in_progress()
        self.__t5_game_not_started()
        self.__t5_team1_won()
        self.__t5_team2_won()

    def test_t6_get_pool_game_winner_team_name(self):
        self.__t6_game_none()
        self.__t6_game_in_progress()
        self.__t6_game_not_started()
        self.__t6_team1_won()
        self.__t6_team2_won()

    def test_t7_get_game_winner(self):
        self.__t7_game_none()
        self.__t7_game_in_progress()
        self.__t7_game_not_started()
        self.__t7_same_score()
        self.__t7_team1_won()
        self.__t7_team2_won()
        self.__t7_team1_won_but_not_favored()
        self.__t7_team2_won_but_not_favored()

    def test_t8_get_game_winner_team_name(self):
        self.__t8_game_none()
        self.__t8_game_in_progress()
        self.__t8_game_not_started()
        self.__t8_same_score()
        self.__t8_team1_won()
        self.__t8_team2_won()

    def test_t9_get_team_winning_pool_game(self):
        self.__t9_game_none()
        self.__t9_game_final()
        self.__t9_game_not_started()
        self.__t9_same_score()
        self.__t9_team1_ahead()
        self.__t9_team2_ahead()

    def test_t10_get_team_name_winning_pool_game(self):
        self.__t10_game_none()
        self.__t10_game_final()
        self.__t10_game_not_started()
        self.__t10_same_score()
        self.__t10_team1_ahead()
        self.__t10_team2_ahead()

    def test_t11_get_team_winning_game(self):
        self.__t11_game_none()
        self.__t11_game_final()
        self.__t11_game_not_started()
        self.__t11_same_score()
        self.__t11_team1_ahead()
        self.__t11_team2_ahead()

    def test_t12_get_team_name_winning_game(self):
        self.__t12_game_none()
        self.__t12_game_final()
        self.__t12_game_not_started()
        self.__t12_same_score()
        self.__t12_team1_ahead()
        self.__t12_team2_ahead()

    # t13 tests are broken up into multiple functions
    # to allow setUp() to run again and restore data
    def test_t13_player_did_not_pick(self):
        self.__t13_game_none()
        self.__t13_game_invalid()
        self.__t13_invalid_player()

    def test_t13_1_player_did_not_pick(self):
        self.__t13_player_missing_all_week_picks()

    def test_t13_2_player_did_not_pick(self):
        self.__t13_player_missing_pick_for_game()

    def test_t13_3_player_did_not_pick(self):
        self.__t13_player_missing_pick_winner()

    def test_t13_4_player_did_not_pick(self):
        self.__t13_player_made_pick()

    def test_t14_did_player_win_game(self):
        self.__t14_game_none()
        self.__t14_invalid_player()
        self.__t14_player_won_game()
        self.__t14_player_lost_game()

    def test_t14_1_did_player_win_game(self):
        self.__t14_player_missing_pick()

    def test_t14_2_did_player_win_game(self):
        self.__t14_game_in_progress()

    def test_t14_3_did_player_win_game(self):
        self.__t14_game_not_started()

    def test_t15_did_player_lose_game(self):
        self.__t15_game_none()
        self.__t15_invalid_player()
        self.__t15_player_won_game()
        self.__t15_player_lost_game()

    def test_t15_1_did_player_lose_game(self):
        self.__t15_player_missing_pick()

    def test_t15_2_did_player_lose_game(self):
        self.__t15_game_in_progress()

    def test_t15_3_did_player_lose_game(self):
        self.__t15_game_not_started()

    def test_t16_get_number_of_wins(self):
        #self.__t16_invalid_player()
        #self.__t16_no_games_started()
        #self.__t16_some_games_in_progress()
        #self.__t16_mixed_game_states()
        #self.__t16_all_games_final()
        #self.__t16_player_with_no_picks()
        #self.__t16_player_0_wins()
        #self.__t16_player_10_wins()
        pass

    def test_t17_get_number_of_losses(self):
        #self.__t17_invalid_player()
        #self.__t17_no_games_started()
        #self.__t17_some_games_in_progress()
        #self.__t17_mixed_game_states()
        #self.__t17_all_games_final()
        #self.__t17_player_with_no_picks()
        #self.__t17_player_0_losses()
        #self.__t17_player_10_losses()
        pass

    def test_t18_is_player_winning_game(self):
        #self.__t18_game_none()
        #self.__t18_invalid_player()
        #self.__t18_player_pick_missing_game_not_started()
        #self.__t18_player_pick_missing_game_in_progress()
        #self.__t18_player_pick_missing_game_final()
        #self.__t18_game_not_started()
        #self.__t18_game_final()
        #self.__t18_player_ahead_in_game_and_pool()
        #self.__t18_player_behind_in_game_and_pool()
        #self.__t18_player_ahead_in_game_and_behind_in_pool()
        #self.__t18_player_behind_in_game_and_ahead_in_pool()
        pass

    def test_t19_is_player_losing_game(self):
        #self.__t19_game_none()
        #self.__t19_invalid_player()
        #self.__t19_player_pick_missing_game_not_started()
        #self.__t19_player_pick_missing_game_in_progress()
        #self.__t19_player_pick_missing_game_final()
        #self.__t19_game_not_started()
        #self.__t19_game_final()
        #self.__t19_player_ahead_in_game_and_pool()
        #self.__t19_player_behind_in_game_and_pool()
        #self.__t19_player_ahead_in_game_and_behind_in_pool()
        #self.__t19_player_behind_in_game_and_ahead_in_pool()
        pass

    def test_t20_is_player_projected_to_win_game(self):
        #self.__t20_game_none()
        #self.__t20_invalid_player()
        #self.__t20_player_pick_missing()
        #self.__t20_game_final_player_ahead_in_game_and_pool()
        #self.__t20_game_final_player_behind_in_game_and_pool()
        #self.__t20_game_final_player_ahead_in_game_and_behind_in_pool()
        #self.__t20_game_final_player_behind_in_game_and_ahead_in_pool()
        #self.__t20_game_in_progress_player_ahead_in_game_and_pool()
        #self.__t20_game_in_progress_player_behind_in_game_and_pool()
        #self.__t20_game_in_progress_player_ahead_in_game_and_behind_in_pool()
        #self.__t20_game_in_progress_player_behind_in_game_and_ahead_in_pool()
        #self.__t20_game_not_started_player_ahead_in_game_and_pool()
        #self.__t20_game_not_started_player_behind_in_game_and_pool()
        #self.__t20_game_not_started_player_ahead_in_game_and_behind_in_pool()
        #self.__t20_game_not_started_player_behind_in_game_and_ahead_in_pool()
        pass


    def __t1_invalid_player(self):
        bad_player = Player()
        bad_player.id = -1
        game = self.__get_a_valid_game()
        with self.assertRaises(KeyError):
            self.calc.get_team_player_picked_to_win(bad_player,game)

    def __t1_invalid_game(self):
        invalid_game = self.__get_a_valid_game2()
        valid_player = self.week1.get_player("holden_brent")
        with self.assertRaises(AssertionError):
            self.calc.get_team_player_picked_to_win(valid_player,invalid_game)

    def __t1_game_none(self):
        valid_player = self.week1.get_player("holden_brent")
        with self.assertRaises(AssertionError):
            self.calc.get_team_player_picked_to_win(valid_player,None)

    def __t1_team2_winner(self):
        game = self.__find_game("North Carolina","South Carolina")
        brent = self.week1.get_player("holden_brent")
        team = self.calc.get_team_player_picked_to_win(brent,game)
        self.assertEqual(team,TEAM2)

    def __t1_team1_winner(self):
        game = self.__find_game("LSU","TCU")
        brent = self.week1.get_player("holden_brent")
        team = self.calc.get_team_player_picked_to_win(brent,game)
        self.assertEqual(team,TEAM1)

    def __t2_invalid_player(self):
        bad_player = Player()
        bad_player.id = -1
        game = self.__get_a_valid_game()
        with self.assertRaises(KeyError):
            self.calc.get_team_name_player_picked_to_win(bad_player,game)

    def __t2_invalid_game(self):
        invalid_game = self.__get_a_valid_game2()
        valid_player = self.week1.get_player("holden_brent")
        with self.assertRaises(AssertionError):
            self.calc.get_team_name_player_picked_to_win(valid_player,invalid_game)

    def __t2_game_none(self):
        valid_player = self.week1.get_player("holden_brent")
        with self.assertRaises(AssertionError):
            self.calc.get_team_name_player_picked_to_win(valid_player,None)

    def __t2_team2_winner(self):
        game = self.__find_game("North Carolina","South Carolina")
        brent = self.week1.get_player("holden_brent")
        team = self.calc.get_team_name_player_picked_to_win(brent,game)
        self.assertEqual(team,"South Carolina")

    def __t2_team1_winner(self):
        game = self.__find_game("LSU","TCU")
        brent = self.week1.get_player("holden_brent")
        team = self.calc.get_team_name_player_picked_to_win(brent,game)
        self.assertEqual(team,"LSU")

    def __t2_winner_missing(self):
        player = self.week1.get_player("holden_brent")
        game = self.__get_a_valid_game()

        self.__make_winner_missing(player,game)
        team = self.calc.get_team_name_player_picked_to_win(player,game)
        self.assertEqual(team,"")

    def __t3_bad_game_favored_value(self):
        g = Game()
        g.team1_actual_points = 0
        g.team2_actual_points = 0
        g.favored = 0
        g.spread = 0.5
        with self.assertRaises(AssertionError):
            self.calc.is_team1_winning_pool(g)

    def __t3_team1_ahead(self):
        g = Game()
        g.team1_actual_points = 20 
        g.team2_actual_points = 10 
        g.favored = TEAM1
        g.spread = 5.5 
        self.assertTrue(self.calc.is_team1_winning_pool(g))

    def __t3_team1_behind(self):
        g = Game()
        g.team1_actual_points = 10 
        g.team2_actual_points = 20 
        g.favored = TEAM1
        g.spread = 5.5 
        self.assertFalse(self.calc.is_team1_winning_pool(g))

    def __t3_team1_ahead_in_pool_behind_in_game(self):
        g = Game()
        g.team1_actual_points = 14 
        g.team2_actual_points = 17 
        g.favored = TEAM2
        g.spread = 3.5 
        self.assertTrue(self.calc.is_team1_winning_pool(g))

    def __t3_team1_behind_in_pool_ahead_in_game(self):
        g = Game()
        g.team1_actual_points = 21 
        g.team2_actual_points = 17 
        g.favored = TEAM1
        g.spread = 4.5 
        self.assertFalse(self.calc.is_team1_winning_pool(g))

    def __t3_team1_boundary_case1(self):
        g = Game()
        g.team1_actual_points = 17 
        g.team2_actual_points = 16 
        g.favored = TEAM1
        g.spread = 0.5 
        self.assertTrue(self.calc.is_team1_winning_pool(g))

    def __t3_team1_boundary_case2(self):
        g = Game()
        g.team1_actual_points = 16 
        g.team2_actual_points = 17 
        g.favored = TEAM1
        g.spread = 0.5 
        self.assertFalse(self.calc.is_team1_winning_pool(g))

    def __t3_team1_boundary_case3(self):
        g = Game()
        g.team1_actual_points = 17 
        g.team2_actual_points = 16 
        g.favored = TEAM2
        g.spread = 0.5 
        self.assertTrue(self.calc.is_team1_winning_pool(g))

    def __t3_team1_boundary_case4(self):
        g = Game()
        g.team1_actual_points = 16 
        g.team2_actual_points = 17 
        g.favored = TEAM2
        g.spread = 0.5 
        self.assertFalse(self.calc.is_team1_winning_pool(g))

    def __t4_bad_game_favored_value(self):
        g = Game()
        g.team1_actual_points = 0
        g.team2_actual_points = 0
        g.favored = 0
        g.spread = 0.5
        with self.assertRaises(AssertionError):
            self.calc.is_team2_winning_pool(g)

    def __t4_team2_ahead(self):
        g = Game()
        g.team1_actual_points = 10 
        g.team2_actual_points = 20 
        g.favored = TEAM2
        g.spread = 5.5 
        self.assertTrue(self.calc.is_team2_winning_pool(g))

    def __t4_team2_behind(self):
        g = Game()
        g.team1_actual_points = 20 
        g.team2_actual_points = 10 
        g.favored = TEAM2
        g.spread = 5.5 
        self.assertFalse(self.calc.is_team2_winning_pool(g))

    def __t4_team2_ahead_in_pool_behind_in_game(self):
        g = Game()
        g.team1_actual_points = 17 
        g.team2_actual_points = 14 
        g.favored = TEAM1
        g.spread = 3.5 
        self.assertTrue(self.calc.is_team2_winning_pool(g))

    def __t4_team2_behind_in_pool_ahead_in_game(self):
        g = Game()
        g.team1_actual_points = 17
        g.team2_actual_points = 21
        g.favored = TEAM2
        g.spread = 4.5 
        self.assertFalse(self.calc.is_team2_winning_pool(g))

    def __t4_team2_boundary_case1(self):
        g = Game()
        g.team1_actual_points = 16 
        g.team2_actual_points = 17 
        g.favored = TEAM2
        g.spread = 0.5 
        self.assertTrue(self.calc.is_team2_winning_pool(g))

    def __t4_team2_boundary_case2(self):
        g = Game()
        g.team1_actual_points = 17 
        g.team2_actual_points = 16 
        g.favored = TEAM2
        g.spread = 0.5 
        self.assertFalse(self.calc.is_team2_winning_pool(g))

    def __t4_team2_boundary_case3(self):
        g = Game()
        g.team1_actual_points = 16 
        g.team2_actual_points = 17 
        g.favored = TEAM1
        g.spread = 0.5 
        self.assertTrue(self.calc.is_team2_winning_pool(g))

    def __t4_team2_boundary_case4(self):
        g = Game()
        g.team1_actual_points = 17 
        g.team2_actual_points = 16 
        g.favored = TEAM1
        g.spread = 0.5 
        self.assertFalse(self.calc.is_team2_winning_pool(g))

    def __t5_game_none(self):
        with self.assertRaises(Exception):
            self.calc.get_pool_game_winner(None)

    def __t5_game_in_progress(self):
        g = Game()
        g.game_state = IN_PROGRESS
        self.assertIsNone(self.calc.get_pool_game_winner(g))

    def __t5_game_not_started(self):
        g = Game()
        g.game_state = NOT_STARTED
        self.assertIsNone(self.calc.get_pool_game_winner(g))

    def __t5_team1_won(self):
        g = Game()
        g.team1_actual_points = 30 
        g.team2_actual_points = 10 
        g.favored = TEAM1
        g.spread = 10.5
        g.game_state = FINAL
        self.assertEqual(self.calc.get_pool_game_winner(g),TEAM1)

    def __t5_team2_won(self):
        g = Game()
        g.team1_actual_points = 30 
        g.team2_actual_points = 25 
        g.favored = TEAM1
        g.spread = 10.5
        g.game_state = FINAL
        self.assertEqual(self.calc.get_pool_game_winner(g),TEAM2)

    def __t6_game_none(self):
        with self.assertRaises(Exception):
            self.calc.get_pool_game_winner_team_name(None)

    def __t6_game_in_progress(self):
        g = Game()
        g.game_state = IN_PROGRESS
        self.assertIsNone(self.calc.get_pool_game_winner_team_name(g))

    def __t6_game_not_started(self):
        g = Game()
        g.game_state = NOT_STARTED
        self.assertIsNone(self.calc.get_pool_game_winner_team_name(g))

    def __t6_team1_won(self):
        game = self.__find_game("LSU","TCU")
        self.assertEqual(self.calc.get_pool_game_winner_team_name(game),"LSU")

    def __t6_team2_won(self):
        game = self.__find_game("Boise State","Washington")
        self.assertEqual(self.calc.get_pool_game_winner_team_name(game),"Washington")

    def __t7_game_none(self):
        with self.assertRaises(Exception):
            self.calc.get_game_winner(None)

    def __t7_game_in_progress(self):
        g = Game()
        g.game_state = IN_PROGRESS
        self.assertIsNone(self.calc.get_game_winner(g))

    def __t7_game_not_started(self):
        g = Game()
        g.game_state = NOT_STARTED
        self.assertIsNone(self.calc.get_game_winner(g))

    def __t7_same_score(self):
        g = Game()
        g.team1_actual_points = 21
        g.team2_actual_points = 21
        g.favored = TEAM1
        g.spread = 10.5
        g.game_state = FINAL
        with self.assertRaises(AssertionError):
            self.calc.get_game_winner(g)

    def __t7_team1_won(self):
        g = Game()
        g.team1_actual_points = 31
        g.team2_actual_points = 21
        g.favored = TEAM1
        g.spread = 10.5
        g.game_state = FINAL
        self.assertEqual(self.calc.get_game_winner(g),TEAM1)

    def __t7_team2_won(self):
        g = Game()
        g.team1_actual_points = 10 
        g.team2_actual_points = 24 
        g.favored = TEAM2
        g.spread = 14.5
        g.game_state = FINAL
        self.assertEqual(self.calc.get_game_winner(g),TEAM2)

    def __t7_team1_won_but_not_favored(self):
        g = Game()
        g.team1_actual_points = 24
        g.team2_actual_points = 21
        g.favored = TEAM2
        g.spread = 5.5
        g.game_state = FINAL
        self.assertEqual(self.calc.get_game_winner(g),TEAM1)

    def __t7_team2_won_but_not_favored(self):
        g = Game()
        g.team1_actual_points = 41
        g.team2_actual_points = 48
        g.favored = TEAM1
        g.spread = 7.5
        g.game_state = FINAL
        self.assertEqual(self.calc.get_game_winner(g),TEAM2)

    def __t8_game_none(self):
        with self.assertRaises(Exception):
            self.calc.get_game_winner_team_name(None)

    def __t8_game_in_progress(self):
        g = Game()
        g.game_state = IN_PROGRESS
        self.assertIsNone(self.calc.get_game_winner_team_name(g))

    def __t8_game_not_started(self):
        g = Game()
        g.game_state = NOT_STARTED
        self.assertIsNone(self.calc.get_game_winner_team_name(g))

    def __t8_same_score(self):
        g = Game()
        g.team1_actual_points = 21
        g.team2_actual_points = 21
        g.favored = TEAM1
        g.spread = 10.5
        g.game_state = FINAL
        with self.assertRaises(AssertionError):
            self.calc.get_game_winner_team_name(g)

    def __t8_team1_won(self):
        game = self.__find_game("Penn State","Syracuse")
        self.assertEqual(self.calc.get_game_winner_team_name(game),"Penn State")

    def __t8_team2_won(self):
        game = self.__find_game("Georgia","Clemson")
        self.assertEqual(self.calc.get_game_winner_team_name(game),"Clemson")

    def __t9_game_none(self):
        with self.assertRaises(Exception):
            self.calc.get_team_winning_pool_game(None)

    def __t9_game_final(self):
        g = Game()
        g.game_state = FINAL
        self.assertIsNone(self.calc.get_team_winning_pool_game(g))

    def __t9_game_not_started(self):
        g = Game()
        g.game_state = NOT_STARTED
        self.assertIsNone(self.calc.get_team_winning_pool_game(g))

    def __t9_same_score(self):
        g = Game()
        g.team1_actual_points = 35
        g.team2_actual_points = 35
        g.favored = TEAM1
        g.spread = 0.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_winning_pool_game(g),TEAM2)

    def __t9_team1_ahead(self):
        g = Game()
        g.team1_actual_points = 44
        g.team2_actual_points = 48
        g.favored = TEAM2
        g.spread = 4.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_winning_pool_game(g),TEAM1)

    def __t9_team2_ahead(self):
        g = Game()
        g.team1_actual_points = 21
        g.team2_actual_points = 18
        g.favored = TEAM1
        g.spread = 3.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_winning_pool_game(g),TEAM2)

    def __t10_game_none(self):
        with self.assertRaises(Exception):
            self.calc.get_team_name_winning_pool_game(None)

    def __t10_game_final(self):
        g = Game()
        g.game_state = FINAL
        self.assertIsNone(self.calc.get_team_name_winning_pool_game(g))

    def __t10_game_not_started(self):
        g = Game()
        g.game_state = NOT_STARTED
        self.assertIsNone(self.calc.get_team_name_winning_pool_game(g))

    def __t10_same_score(self):
        g = Game()
        g.team1 = self.__find_team("Georgia Tech")
        g.team2 = self.__find_team("Clemson")
        g.team1_actual_points = 35
        g.team2_actual_points = 35
        g.favored = TEAM1
        g.spread = 0.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_name_winning_pool_game(g),"Clemson")

    def __t10_team1_ahead(self):
        g = Game()
        g.team1 = self.__find_team("Georgia Tech")
        g.team2 = self.__find_team("Clemson")
        g.team1_actual_points = 44
        g.team2_actual_points = 48
        g.favored = TEAM2
        g.spread = 4.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_name_winning_pool_game(g),"Georgia Tech")

    def __t10_team2_ahead(self):
        g = Game()
        g.team1 = self.__find_team("Georgia Tech")
        g.team2 = self.__find_team("Clemson")
        g.team1_actual_points = 21
        g.team2_actual_points = 18
        g.favored = TEAM1
        g.spread = 3.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_name_winning_pool_game(g),"Clemson")

    def __t11_game_none(self):
        with self.assertRaises(Exception):
            self.calc.get_team_winning_game(None)

    def __t11_game_final(self):
        g = Game()
        g.game_state = FINAL
        self.assertIsNone(self.calc.get_team_winning_game(g))

    def __t11_game_not_started(self):
        g = Game()
        g.game_state = NOT_STARTED
        self.assertIsNone(self.calc.get_team_winning_game(g))

    def __t11_same_score(self):
        g = Game()
        g.team1 = self.__find_team("Georgia Tech")
        g.team2 = self.__find_team("Clemson")
        g.team1_actual_points = 35
        g.team2_actual_points = 35
        g.favored = TEAM1
        g.spread = 0.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_winning_game(g),TIED)

    def __t11_team1_ahead(self):
        g = Game()
        g.team1 = self.__find_team("Georgia Tech")
        g.team2 = self.__find_team("Clemson")
        g.team1_actual_points = 31
        g.team2_actual_points = 24
        g.favored = TEAM2
        g.spread = 4.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_winning_game(g),TEAM1)

    def __t11_team2_ahead(self):
        g = Game()
        g.team1 = self.__find_team("Georgia Tech")
        g.team2 = self.__find_team("Clemson")
        g.team1_actual_points = 17
        g.team2_actual_points = 31
        g.favored = TEAM1
        g.spread = 3.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_winning_game(g),TEAM2)

    def __t12_game_none(self):
        with self.assertRaises(Exception):
            self.calc.get_team_name_winning_game(None)

    def __t12_game_final(self):
        g = Game()
        g.game_state = FINAL
        self.assertIsNone(self.calc.get_team_name_winning_game(g))

    def __t12_game_not_started(self):
        g = Game()
        g.game_state = NOT_STARTED
        self.assertIsNone(self.calc.get_team_name_winning_game(g))

    def __t12_same_score(self):
        g = Game()
        g.team1 = self.__find_team("Georgia Tech")
        g.team2 = self.__find_team("Clemson")
        g.team1_actual_points = 35
        g.team2_actual_points = 35
        g.favored = TEAM1
        g.spread = 0.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_name_winning_game(g),"tied")

    def __t12_team1_ahead(self):
        g = Game()
        g.team1 = self.__find_team("Georgia Tech")
        g.team2 = self.__find_team("Clemson")
        g.team1_actual_points = 31
        g.team2_actual_points = 24
        g.favored = TEAM2
        g.spread = 4.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_name_winning_game(g),"Georgia Tech")

    def __t12_team2_ahead(self):
        g = Game()
        g.team1 = self.__find_team("Georgia Tech")
        g.team2 = self.__find_team("Clemson")
        g.team1_actual_points = 17
        g.team2_actual_points = 31
        g.favored = TEAM1
        g.spread = 3.5
        g.game_state = IN_PROGRESS
        self.assertEqual(self.calc.get_team_name_winning_game(g),"Clemson")

    def __t13_game_none(self):
        valid_player = self.week1.get_player("holden_brent")
        with self.assertRaises(Exception):
            self.calc.player_did_not_pick(valid_player,None)

    def __t13_game_invalid(self):
        valid_player = self.week1.get_player("holden_brent")
        invalid_game = self.__get_a_valid_game2()
        with self.assertRaises(Exception):
            self.calc.player_did_not_pick(valid_player,invalid_game)

    def __t13_invalid_player(self):
        bad_player = Player()
        bad_player.id = -1
        game = self.__get_a_valid_game()
        with self.assertRaises(Exception):
            self.calc.player_did_not_pick(bad_player,game)

    def __t13_player_missing_all_week_picks(self):
        player = self.week1.get_player("holden_brent")
        game = self.__get_a_valid_game()
        self.__make_all_picks_missing(player)
        self.assertTrue(self.calc.player_did_not_pick(player,game))

    def __t13_player_missing_pick_for_game(self):
        player = self.week1.get_player("holden_brent")
        game = self.__get_a_valid_game()
        self.__remove_game_from_picks(player,game)
        self.assertTrue(self.calc.player_did_not_pick(player,game))

    def __t13_player_missing_pick_winner(self):
        player = self.week1.get_player("holden_brent")
        game = self.__get_a_valid_game()
        self.__make_winner_missing(player,game)
        self.assertTrue(self.calc.player_did_not_pick(player,game))

    def __t13_player_made_pick(self):
        player = self.week1.get_player("holden_brent")
        game = self.__get_a_valid_game()
        self.assertFalse(self.calc.player_did_not_pick(player,game))

    def __t14_game_none(self):
        player = self.week1.get_player("holden_brent")
        with self.assertRaises(Exception):
            self.calc.did_player_win_game(player,None)

    def __t14_invalid_player(self):
        bad_player = Player()
        bad_player.id = -1
        game = self.__get_a_valid_game()
        with self.assertRaises(Exception):
            self.calc.did_player_win_game(bad_player,game)

    def __t14_player_missing_pick(self):
        player = self.week1.get_player("holden_brent")
        game = self.__get_a_valid_game()

        self.__remove_game_from_picks(player,game)
        self.assertFalse(self.calc.did_player_win_game(player,game))

    def __t14_game_in_progress(self):
        player = self.week1.get_player("holden_brent")
        game = self.__get_a_valid_game()
        game.game_state = IN_PROGRESS
        self.assertFalse(self.calc.did_player_win_game(player,game))

    def __t14_game_not_started(self):
        player = self.week1.get_player("holden_brent")
        game = self.__get_a_valid_game()
        game.game_state = NOT_STARTED
        self.assertFalse(self.calc.did_player_win_game(player,game))

    def __t14_player_won_game(self):
        player = self.week1.get_player("holden_brent")
        game = self.__find_game("North Carolina","South Carolina")
        self.assertTrue(self.calc.did_player_win_game(player,game))

    def __t14_player_lost_game(self):
        player = self.week1.get_player("holden_brent")
        game = self.__find_game("Penn State","Syracuse")
        self.assertFalse(self.calc.did_player_win_game(player,game))

    def __t15_game_none(self):
        player = self.week1.get_player("holden_brent")
        with self.assertRaises(Exception):
            self.calc.did_player_lose_game(player,None)

    def __t15_invalid_player(self):
        bad_player = Player()
        bad_player.id = -1
        game = self.__get_a_valid_game()
        with self.assertRaises(Exception):
            self.calc.did_player_lose_game(bad_player,game)

    def __t15_player_missing_pick(self):
        player = self.week1.get_player("holden_brent")
        game = self.__get_a_valid_game()
        self.__remove_game_from_picks(player,game)
        self.assertTrue(self.calc.did_player_lose_game(player,game))

    def __t15_game_in_progress(self):
        player = self.week1.get_player("holden_brent")
        game = self.__get_a_valid_game()
        game.game_state = IN_PROGRESS
        self.assertFalse(self.calc.did_player_lose_game(player,game))

    def __t15_game_not_started(self):
        player = self.week1.get_player("holden_brent")
        game = self.__get_a_valid_game()
        game.game_state = NOT_STARTED
        self.assertFalse(self.calc.did_player_lose_game(player,game))

    def __t15_player_won_game(self):
        player = self.week1.get_player("holden_brent")
        game = self.__find_game("North Carolina","South Carolina")
        self.assertFalse(self.calc.did_player_lose_game(player,game))

    def __t15_player_lost_game(self):
        player = self.week1.get_player("holden_brent")
        game = self.__find_game("Penn State","Syracuse")
        self.assertTrue(self.calc.did_player_lose_game(player,game))

    def __t16_invalid_player(self):
        with self.assertRaises(Exception):
            self.calc.get_number_of_wins("bad key")

    def __t16_no_games_started(self):
        player_key = self.week1.get_player_key("Brent H.")
        self.__modify_game_states(['not_started']*10)
        self.assertEqual(self.calc.get_number_of_wins(player_key),0)
        self.__restore_games()

    def __t16_some_games_in_progress(self):
        player_key = self.week1.get_player_key("Brent H.")
        states = ['not_started']*3 + ['in_progress']*7
        self.__modify_game_states(states)
        self.assertEqual(self.calc.get_number_of_wins(player_key),0)
        self.__restore_games()

    def __t16_mixed_game_states(self):
        player_key = self.week1.get_player_key("Brent H.")
        num_wins_in_first_3_games_2013_week_1 = 2

        states = ['final']*3 + ['not_started']*3 + ['in_progress']*4
        self.__modify_game_states(states)
        self.assertEqual(self.calc.get_number_of_wins(player_key),num_wins_in_first_3_games_2013_week_1)
        self.__restore_games()

    def __t16_all_games_final(self):
        player_key = self.week1.get_player_key("Brent H.")
        num_wins_2013_week_1 = 5
        self.assertEqual(self.calc.get_number_of_wins(player_key),num_wins_2013_week_1)

    def __t16_player_with_no_picks(self):
        player_key = self.week1.get_player_key("Brent H.")
        self.__make_all_player_picks_not_entered(player_key)
        self.assertEqual(self.calc.get_number_of_wins(player_key),0)
        self.__restore_picks(player_key)

    def __t16_player_0_wins(self):
        player_key = self.week1.get_player_key("Dale R.")
        self.__make_dale_0_wins()
        self.assertEqual(self.calc.get_number_of_wins(player_key),0)
        self.__restore_picks(player_key)

    def __t16_player_10_wins(self):
        player_key = self.week1.get_player_key("William M.")
        self.__make_william_10_wins()
        self.assertEqual(self.calc.get_number_of_wins(player_key),10)
        self.__restore_picks(player_key)

    def __t17_invalid_player(self):
        with self.assertRaises(Exception):
            self.calc.get_number_of_losses("bad key")

    def __t17_no_games_started(self):
        player_key = self.week1.get_player_key("Brent H.")
        self.__modify_game_states(['not_started']*10)
        self.assertEqual(self.calc.get_number_of_losses(player_key),0)
        self.__restore_games()

    def __t17_some_games_in_progress(self):
        player_key = self.week1.get_player_key("Brent H.")
        states = ['not_started']*3 + ['in_progress']*7
        self.__modify_game_states(states)
        self.assertEqual(self.calc.get_number_of_losses(player_key),0)
        self.__restore_games()

    def __t17_mixed_game_states(self):
        player_key = self.week1.get_player_key("Brent H.")
        num_losses_in_first_3_games_2013_week_1 = 1

        states = ['final']*3 + ['not_started']*3 + ['in_progress']*4
        self.__modify_game_states(states)
        self.assertEqual(self.calc.get_number_of_losses(player_key),num_losses_in_first_3_games_2013_week_1)
        self.__restore_games()

    def __t17_all_games_final(self):
        player_key = self.week1.get_player_key("Byron R.")
        num_losses_2013_week_1 = 4
        self.assertEqual(self.calc.get_number_of_losses(player_key),num_losses_2013_week_1)

    def __t17_player_with_no_picks(self):
        player_key = self.week1.get_player_key("Brent H.")
        self.__make_all_player_picks_not_entered(player_key)
        self.assertEqual(self.calc.get_number_of_losses(player_key),10)
        self.__restore_picks(player_key)

    def __t17_player_0_losses(self):
        player_key = self.week1.get_player_key("William M.")
        self.__make_william_10_wins()
        self.assertEqual(self.calc.get_number_of_losses(player_key),0)
        self.__restore_picks(player_key)

    def __t17_player_10_losses(self):
        player_key = self.week1.get_player_key("Dale R.")
        self.__make_dale_0_wins()
        self.assertEqual(self.calc.get_number_of_losses(player_key),10)
        self.__restore_picks(player_key)

    def __t18_game_none(self):
        player_key = self.__get_a_valid_player_key()
        with self.assertRaises(Exception):
            self.calc.is_player_winning_game(player_key,None)

    def __t18_invalid_player(self):
        game_key = self.__get_a_valid_game_key()
        with self.assertRaises(Exception):
            self.calc.is_player_winning_game("bad key",game_key)

    def __t18_player_pick_missing_game_not_started(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 25
        game.team2_score = 10
        game.state = "not_started"

        game_key = self.__edit_existing_game(game)
        self.__make_winner_missing(player_key,game_key)

        self.assertFalse(self.calc.is_player_winning_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t18_player_pick_missing_game_in_progress(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 25
        game.team2_score = 10
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__make_winner_missing(player_key,game_key)

        self.assertFalse(self.calc.is_player_winning_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t18_player_pick_missing_game_final(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 25
        game.team2_score = 10
        game.state = "final"

        game_key = self.__edit_existing_game(game)
        self.__make_winner_missing(player_key,game_key)

        self.assertFalse(self.calc.is_player_winning_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t18_player_ahead_in_game_and_pool(self):
        player_key = self.week1.get_player_key("Brent H.")
        self.__save_picks(self.week1.player_picks[player_key])

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 25
        game.team2_score = 10
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertTrue(self.calc.is_player_winning_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t18_player_behind_in_game_and_pool(self):
        player_key = self.week1.get_player_key("Brent H.")
        self.__save_picks(self.week1.player_picks[player_key])

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 10
        game.team2_score = 30
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertFalse(self.calc.is_player_winning_game(player_key,game_key))

    def __t18_player_ahead_in_game_and_behind_in_pool(self):
        player_key = self.week1.get_player_key("Brent H.")
        self.__save_picks(self.week1.player_picks[player_key])

        game = Game()
        game.favored = "team2"
        game.spread = 5.5
        game.team1_score = 20 
        game.team2_score = 25
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team2")

        self.assertFalse(self.calc.is_player_winning_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t18_player_behind_in_game_and_ahead_in_pool(self):
        player_key = self.week1.get_player_key("Brent H.")
        self.__save_picks(self.week1.player_picks[player_key])

        game = Game()
        game.favored = "team2"
        game.spread = 1.5
        game.team1_score = 20 
        game.team2_score = 21
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertTrue(self.calc.is_player_winning_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t18_game_not_started(self):
        player_key = self.week1.get_player_key("Brent H.")
        self.__save_picks(self.week1.player_picks[player_key])

        game = Game()
        game.favored = "team2"
        game.spread = 1.5
        game.team1_score = 20 
        game.team2_score = 21
        game.state = "not_started"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertFalse(self.calc.is_player_winning_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t18_game_final(self):
        player_key = self.week1.get_player_key("Brent H.")
        self.__save_picks(self.week1.player_picks[player_key])

        game = Game()
        game.favored = "team2"
        game.spread = 1.5
        game.team1_score = 20 
        game.team2_score = 21
        game.state = "final"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertFalse(self.calc.is_player_winning_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t19_game_none(self):
        player_key = self.__get_a_valid_player_key()
        with self.assertRaises(Exception):
            self.calc.is_player_losing_game(player_key,None)

    def __t19_invalid_player(self):
        game_key = self.__get_a_valid_game_key()
        with self.assertRaises(Exception):
            self.calc.is_player_losing_game("bad key",game_key)

    def __t19_game_not_started(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team2"
        game.spread = 1.5
        game.team1_score = 20 
        game.team2_score = 21
        game.state = "not_started"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertFalse(self.calc.is_player_losing_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t19_game_final(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team2"
        game.spread = 1.5
        game.team1_score = 20 
        game.team2_score = 21
        game.state = "final"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertFalse(self.calc.is_player_losing_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t19_player_pick_missing_game_not_started(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 25
        game.team2_score = 10
        game.state = "not_started"

        game_key = self.__edit_existing_game(game)
        self.__make_winner_missing(player_key,game_key)

        self.assertTrue(self.calc.is_player_losing_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t19_player_pick_missing_game_in_progress(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 25
        game.team2_score = 10
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__make_winner_missing(player_key,game_key)

        self.assertTrue(self.calc.is_player_losing_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t19_player_pick_missing_game_final(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 10
        game.team2_score = 25
        game.state = "final"

        game_key = self.__edit_existing_game(game)
        self.__make_winner_missing(player_key,game_key)

        self.assertFalse(self.calc.is_player_losing_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t19_player_ahead_in_game_and_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 25
        game.team2_score = 10
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertFalse(self.calc.is_player_losing_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t19_player_behind_in_game_and_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 10
        game.team2_score = 30
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertTrue(self.calc.is_player_losing_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t19_player_ahead_in_game_and_behind_in_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team2"
        game.spread = 5.5
        game.team1_score = 20 
        game.team2_score = 25
        game.state = "in_progress"
        
        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team2")

        self.assertTrue(self.calc.is_player_losing_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t19_player_behind_in_game_and_ahead_in_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team2"
        game.spread = 1.5
        game.team1_score = 20 
        game.team2_score = 21
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertFalse(self.calc.is_player_losing_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t20_game_none(self):
        player_key = self.__get_a_valid_player_key()
        with self.assertRaises(Exception):
            self.calc.is_player_projected_to_win_game(player_key,None)

    def __t20_invalid_player(self):
        game_key = self.__get_a_valid_game_key()
        with self.assertRaises(Exception):
            self.calc.is_player_projected_to_win_game("bad key",game_key)

    def __t20_player_pick_missing(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 10
        game.team2_score = 25
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__make_winner_missing(player_key,game_key)

        self.assertFalse(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)


    def __t20_game_final_player_ahead_in_game_and_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 25
        game.team2_score = 10
        game.state = "final"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertTrue(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)


    def __t20_game_final_player_behind_in_game_and_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 10
        game.team2_score = 30
        game.state = "final"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertFalse(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)


    def __t20_game_final_player_ahead_in_game_and_behind_in_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team2"
        game.spread = 5.5
        game.team1_score = 20 
        game.team2_score = 25
        game.state = "final"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team2")

        self.assertFalse(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)



    def __t20_game_final_player_behind_in_game_and_ahead_in_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team2"
        game.spread = 1.5
        game.team1_score = 20 
        game.team2_score = 21
        game.state = "final"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertTrue(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t20_game_in_progress_player_ahead_in_game_and_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 25
        game.team2_score = 10
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertTrue(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)



    def __t20_game_in_progress_player_behind_in_game_and_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 10
        game.team2_score = 30
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertFalse(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t20_game_in_progress_player_ahead_in_game_and_behind_in_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team2"
        game.spread = 5.5
        game.team1_score = 20 
        game.team2_score = 25
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team2")

        self.assertFalse(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)


    def __t20_game_in_progress_player_behind_in_game_and_ahead_in_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team2"
        game.spread = 1.5
        game.team1_score = 20 
        game.team2_score = 21
        game.state = "in_progress"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertTrue(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)


    def __t20_game_not_started_player_ahead_in_game_and_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 25
        game.team2_score = 10
        game.state = "not_started"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertTrue(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)

    def __t20_game_not_started_player_behind_in_game_and_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team1"
        game.spread = 5.5
        game.team1_score = 10
        game.team2_score = 30
        game.state = "not_started"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertTrue(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)


    def __t20_game_not_started_player_ahead_in_game_and_behind_in_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team2"
        game.spread = 5.5
        game.team1_score = 20 
        game.team2_score = 25
        game.state = "not_started"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team2")

        self.assertTrue(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)


    def __t20_game_not_started_player_behind_in_game_and_ahead_in_pool(self):
        player_key = self.week1.get_player_key("Brent H.")

        game = Game()
        game.favored = "team2"
        game.spread = 1.5
        game.team1_score = 20 
        game.team2_score = 21
        game.state = "not_started"

        game_key = self.__edit_existing_game(game)
        self.__change_player_pick(player_key,game_key,"team1")

        self.assertTrue(self.calc.is_player_projected_to_win_game(player_key,game_key))

        self.__restore_picks(player_key)
        self.__restore_game(game_key)


    def __get_a_valid_game(self):
        return self.week1.games[1]

    def __get_a_valid_game2(self):
        return self.week2.games[1]

    def __find_game(self,team1,team2):
        for game in self.week1.games.values():
            same_teams = team1 == game.team1.team_name and team2 == game.team2.team_name
            if same_teams:
                return game
        raise AssertionError, "Could not find game"

    def __find_team(self,name):
        if name not in self.week1.teams:
            raise AssertionError,"Could not find team %s" % (name)
        return self.week1.teams[name]

    def __make_winner_missing(self,player,game):
        for i,pick in enumerate(self.week1.player_picks[player.id]):
            if pick.game == game:
                self.week1.player_picks[player.id][i].winner = 0
                return
        raise AssertionError,"could not find game in picks"

    def __make_all_picks_missing(self,player):
        self.week1.player_picks[player.id] = []

    def __remove_game_from_picks(self,player,game):
        new_picks = []
        for pick in self.week1.player_picks[player.id]:
            if pick.game != game:
                new_picks.append(pick)
        self.week1.player_picks[player.id] = new_picks
