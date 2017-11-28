import unittest

from Game import Game
from Team import Team
from GameMaker import GameMaker

class TestEditTeam(unittest.TestCase):

    def setUp(self):
        self.game = Game()#Initialize game
        self.gameMaker = GameMaker(self.game)#Initialize gamemaker with new game

        team1 = Team("Team1","Password1", self.game)#Initialize Teams
        team2 = Team("Team2","Password2", self.game)
        team3 = Team("Team3","Password3", self.game)

        self.game.teamList.append(team1)#Add teams to Game's teamlist
        self.game.teamList.append(team2)
        self.game.teamList.append(team3)

    def test_edit_existing_team(self):
        self.gameMaker.edit_team("Team2","NewTeam2","NewPassword2")
        self.assertEqual(self.game.teamList[1].name, "NewTeam2", "Team name was not changed correctly")
        self.assertEqual(self.game.teamList[1].password, "NewPassword2", "Team password was not changed correctly")

    def test_edit_nonexisting_team(self):
        self.assertFalse(self.gameMaker.edit_team("NonExistingTeam", "NewTeam2", "NewPassword2"), "A non existing team was edited successfully")


if __name__ == "__main__":
    unittest.main()




