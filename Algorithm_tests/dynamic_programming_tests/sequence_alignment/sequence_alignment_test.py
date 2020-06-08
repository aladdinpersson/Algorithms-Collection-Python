import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append("Algorithms/dynamic_programming/")

# If run from local:
# sys.path.append('../../../Algorithms/dynamic_programming/')
from sequence_alignment import SequenceAlignment


class test_sequence_alignment(unittest.TestCase):
    def setUp(self):
        self.x1 = "ABC"
        self.y1 = "ADC"
        self.correct_editstep1 = 1

        self.x2 = "AB"
        self.y2 = "A"
        self.correct_editstep2 = 1

        self.x3 = "A"
        self.y3 = ""
        self.correct_editstep3 = 1

        self.x4 = "ABC"
        self.y4 = "ABCDE"
        self.correct_editstep4 = 2

        self.x5 = "ABCKL"
        self.y5 = "ADCE"
        self.correct_editstep5 = 3

        self.x6 = "A" * 10
        self.y6 = ""
        self.correct_editstep6 = 10

        self.x7 = ""
        self.y7 = "A" * 10
        self.correct_editstep7 = 10

        self.x8 = "TGACGTGC"
        self.y8 = "TCGACGTCA"
        self.correct_editstep8 = 3

        self.x9 = "XYZ"
        self.y9 = "XKZ"
        self.correct_solution9 = ["align_X", "align_K", "align_Z"]

        self.x10 = "XX"
        self.y10 = ""
        self.correct_solution10 = ["remove_X", "remove_X"]

        self.x11 = ""
        self.y11 = "XX"
        self.correct_solution11 = ["insert_X", "insert_X"]

    def test_simplecase(self):
        sequence_align = SequenceAlignment(self.x1, self.y1)
        editsteps, _ = sequence_align.alignment()
        self.assertEqual(self.correct_editstep1, editsteps)

    def test_remove(self):
        sequence_align = SequenceAlignment(self.x2, self.y2)
        editsteps, _ = sequence_align.alignment()
        self.assertEqual(self.correct_editstep2, editsteps)

    def test_remove_to_empty(self):
        sequence_align = SequenceAlignment(self.x3, self.y3)
        editsteps, _ = sequence_align.alignment()
        self.assertEqual(self.correct_editstep3, editsteps)

    def test_insert_elements(self):
        sequence_align = SequenceAlignment(self.x4, self.y4)
        editsteps, _ = sequence_align.alignment()
        self.assertEqual(self.correct_editstep4, editsteps)

    def test_remove_insert_align(self):
        sequence_align = SequenceAlignment(self.x5, self.y5)
        editsteps, _ = sequence_align.alignment()
        self.assertEqual(self.correct_editstep5, editsteps)

    def test_x_longer_than_y(self):
        sequence_align = SequenceAlignment(self.x6, self.y6)
        editsteps, _ = sequence_align.alignment()
        self.assertEqual(self.correct_editstep6, editsteps)

    def test_y_longer_than_x(self):
        sequence_align = SequenceAlignment(self.x7, self.y7)
        editsteps, _ = sequence_align.alignment()
        self.assertEqual(self.correct_editstep7, editsteps)

    def test_more_complicated_example(self):
        sequence_align = SequenceAlignment(self.x8, self.y8)
        editsteps, _ = sequence_align.alignment()
        self.assertEqual(self.correct_editstep8, editsteps)

    def test_findsolution_simplecase(self):
        sequence_align = SequenceAlignment(self.x9, self.y9)
        _, solution = sequence_align.alignment()
        self.assertEqual(self.correct_solution9, solution)

    def test_findsolution_empty_y(self):
        sequence_align = SequenceAlignment(self.x10, self.y10)
        _, solution = sequence_align.alignment()
        self.assertEqual(self.correct_solution10, solution)

    def test_findsolution_empty_x(self):
        sequence_align = SequenceAlignment(self.x11, self.y11)
        _, solution = sequence_align.alignment()
        self.assertEqual(self.correct_solution11, solution)


if __name__ == "__main__":
    print("Running Sequence Alignment tests:")
    unittest.main()
