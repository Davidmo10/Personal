# eScavenge
##### Software to enable virtual scavenger hunts

A traditional scavenger hunt game works as follows. Teams of players are all given a clue describing a particular location in the hunt area. After deciphering the clue they go the landmark described where they find a clue (a card or sign left by the game maker) to the next landmark. This repeats until the final landmark is discovered. First team to arrive at the final landmark wins. The Amazing Race is an example.

One difficulty in setting up such a game is that clues must be easily found when at the landmark, but they cannot be taken or dismantled by passers by. A second potential problem is that one team could destroy or alter a clue to confuse teams that arrive later to that landmark.

Our software, eScavenge, aims to address these difficulties. The game maker creates a clue for each landmark. By visiting the landmark the game maker finds a detail about the landmark one could only know by being there, and writes a confirmation question about this detail. Finally, the landmarks are ordered into a course. When teams play the game, after logging in they are given the clue to the first landmark. When they are ready they can ask for the confirmation question for that land mark. The game maker can set penalties on both the number of times a confirmation question is answered incorrectly and the amount of time that has passed between receiving the confirmation question and answering it correctly. Once the confirmation question is answered the team receives the clue for the next landmark. The team can always request the current clue without penalty.

Once a team has arrived at the final landmark and entered the final confirmation question it receives its score (based on its finishing rank and any penalties.) The game maker can check the status of all teams (current landmark, confirmation question timer (if any), current penalty, total score if complete). Teams can only know their own status.

The application will use a simple command line interface. Once a user (team or game maker) logs in, they issue commands. Teams need  to receive confirmation questions, enter confirmation answers, see the current clue, get status. They also need to edit their data (password, team name, etc.) Game makers need only get status while the game is running, but to set up they game the game maker needs to be able to create a landmark, enter the clue and confirmation question for that landmark, create a game (which is a total ordering of a subset of existing landmarks), start and end a game, and create/edit/delete teams' login credentials. The game maker's login will be set by the developers.

--------------------------
### Lab Descriptions
- [Lab 7](Labs/lab7.md)
- [Lab 8](Labs/lab8.md)
