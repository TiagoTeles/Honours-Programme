# ============================================================
# Name: Tiago Teles
# License: GNU GPL 3.0
# Version: 0.0.1
# Email: T.MoreiraDaFonteFonsecaTeles@student.tudelft.nl
# ============================================================

# Imports
import unittest
from src import main

# Main Program
class TestMain(unittest.TestCase):

    def test_hello_world(self):
        main.hello_world()
