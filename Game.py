from GameGameMaker import GameGameMaker
from GameTeam import GameTeam
import User
import Landmark
import ScavengerHunt



class Game(GameGameMaker, GameTeam):

	on = False
	myUserDisct = {}
	myLandmarkDict = {}
	myScavengerHunt = {}

	def start(self):
		pass

	def stop(self):
		pass
