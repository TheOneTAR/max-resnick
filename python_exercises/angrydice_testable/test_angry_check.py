__author__ = 'Maxwell J. Resnick'

import unittest
from angry_dice import AngryDice
from unittest.mock import patch
from io import StringIO
import sys

class AngryCheckTest(unittest.TestCase):
    """Tests that AngryDie's angry check function works"""

    def setUp(self):
        self.new_game = AngryDice(False)
        print(self.shortDescription())

    def test_if_both_values_are_angry_we_get_true(self):
        """This checks if check_angry returns True if we are angry."""
        self.new_game.current_dice_a_value = "ANGRY"
        self.new_game.current_dice_b_value = "ANGRY"
        self.assertTrue(self.new_game.check_angry(),
                        "We're expecting to be returned true because both dice"
                        "values are set to ANGRY")

    def test_if_current_stage_is_set_to_1_if_angry(self):
        """This checks if the current stage is set to 1 if are `angry`"""
        self.new_game.current_dice_a_value = "ANGRY"
        self.new_game.current_dice_b_value = "ANGRY"
        self.new_game.check_angry()
        self.assertEqual(1, self.new_game.current_stage)

    @patch('sys.stdout', new_callable=StringIO)
    def test_if_print_works_for_angry(self, mock_stdout):
        """Checks print statement when player hits status of angry."""
        error_message = "The print statement doesn't match the requried"
        angry_text = "WOW, you're ANGRY!\n" + "Time to go back to Stage 1!\n"
        self.new_game.current_dice_a_value = "ANGRY"
        self.new_game.current_dice_b_value = "ANGRY"
        self.new_game.check_angry()
        self.assertEqual(mock_stdout.getvalue(), angry_text, error_message)

    # Greedy angry checks
    def test_that_angry_check_doesnt_cause_false_pos_for_one_angry_dice_a(self):
        """currently B dice values is angry, do we have a false positives"""
        self.new_game.current_dice_a_value = 1
        self.new_game.current_dice_b_value = "ANGRY"
        self.assertFalse(self.new_game.check_angry())

    def test_that_angry_check_doesnt_cause_false_pos_for_one_angry_dice_b(self):
        """currently A dice values is angry, do we have a false positives"""
        self.new_game.current_dice_a_value = "ANGRY"
        self.new_game.current_dice_b_value = 4
        self.assertFalse(self.new_game.check_angry())

    def test_that_angry_check_doesnt_cause_false_pos_for_either_angry_dice_b(self):
        """currently no dice values are angry, do we have a false positives"""
        self.new_game.current_dice_a_value = 1
        self.new_game.current_dice_b_value = 4
        self.assertFalse(self.new_game.check_angry())


if __name__ == '__main__':
    unittest.main()
