# Scavenger Hunt ERD Explained #

## Entities ##
* CLUE - holds the clue
* QUESTION - holds a question prompt and a question answer
* LANDMARK - holds a name and a description
* TASK - has an order
* GAME - has a master, a name, a description, a start timestamp and an end timestamp
* EVENT - has a timestamp and a boolean is answer (otherwise is prompt)
* ANSWER - has a boolean is correct
* USER - has a name, a password, and a boolean is master
* TEAM - has a score and a boolean is done


## Relationships ##
* A clue is associated with exactly 1 landmark
* A question is associated with exactly one landmark
* A landmark can have many or no clues
* A landmark can have many or no questions
* A landmark is linked with many or no tasks
* A team competes in at least one game
* A team is linked with exactly one user
* A game is played by many or no teams
* A game is composed of many or no tasks
* A game is masterd by exactly one user
* A user plays in one or zero teams
* A user masters one or zero games
* A user may complete zero or many events
* A task is linked to exactly one landmark
* A task is part of exactly one game
* A task may generates many or zero events
* An event is associated with exactly one task
* An event (question) can link with zero or one answer
* An event is completed by exactly one user
* An answer is corresponds to exaclty one event
