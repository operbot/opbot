# This file is placed in the Public Domain.


"user"


import unittest


from opb.irc import User


class TestUser(unittest.TestCase):

    "test irc users."

    def test_user(self):
        "test construction."
        user = User()
        self.assertEqual(type(user), User)
