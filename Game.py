from GameGameMaster import GameGameMaster
from GameTeam import GameTeam
import User
import Landmark
import ScavengerHunt



class Game(GameGameMaster, GameTeam):

	on = False
	myUserDisct = {}
	myLandmarkDict = {}
	myScavengerHunt = {}

	def start(self):
		pass

	def stop(self):
		pass
