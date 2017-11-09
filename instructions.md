# Commands

!! Quoted strings are parsed as one argument !!

### All Users
- `login <username> <password>` - logs you in to your account
- `logout` - once you've logged in

### Teams

- `getclue` - gets clue of the team's current landmarks
- `getquestion` - gets question of team's current landmark
- `answer <answer>` - allows team to answer question of current landmark
- `forfeit` - forfeit, so users can no longer update their state

### Gamemaker
- `createlandmark <name>` - Adds a landmark to the game with specified name
- `createteam <name> <password>` - Adds a team to the game with specified name and password
- `landmarkclue <name> <clue>` - Adds a clue to landmark with specified name
- `landmarkquestion <name> <question> <answer>` - Adds a question to the specified landmark with specified answer
- `endgame` - ends the game
- `startgame` - starts game, allowing teams to begin playing
- `listlandmarks` - lists all landmarks with their clues


