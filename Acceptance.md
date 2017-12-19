# All Acceptance tests:

## User Story #1 & #3
#### As a user I can log in / log out

(Assuming server is started and web page is loaded to default)
1. On the page, enter username "maker1" and password "maker1pwd"
2. Press submit
    
    -[X] Should display a dashboard
3. Find and click a button or link labeled "Logout"
    
    -[X] Should return to log in page
4. Enter "team1" and password "team1pwd"
5. Press submit
    
    -[X] Should display a dashboard
6. Find and click a button or link labeled "Logout"
    
    -[X] Should return to log in page

## User Story #2
#### As a game maker, I can edit a landmark's details

(Assuming server is started and web page is loaded to default)

1. Enter "maker1" and "maker1pwd", then press submit
2. Find and click the title of Landmark 1
    
    -[X] Should display form
3. Change the values to "a", "b", "c", "d", and "e"
4. Press "Edit Landmark" button below form
    
    -[ ] Should return to main dashboard, with the first landmark titled "a"
5. Again, click the title of the first landmark
    
    -[ ] Fields should display as "a", "b", "c", "d", and "e" as you entered them

## User Story #5
#### As a game maker, I can add a landmark to a scavenger hunt

(Assuming server is started and web page is loaded to default)

1. Enter "maker1" and "maker1pwd", then press submit
2. Click "Add Landmark"

    -[X] Should display landmark addition form
3. Fill in form with "Name", "desc", "a lm", "where", and "here"
4. Click "Add Landmark"

    -[X] Should show a landmark called "Name" at bottom of landmark list

## User Story #12
#### As a game maker, I can edit team credentials

(Assuming server is started and web page is loaded to default)

1. Enter "maker1" and "maker1pwd", then press submit
2. From the left-hand side, click "team1"
3. Type "t", "maker1pwd", and "t" into the three fields
4. Click "Edit Credentials"
    
    -[X] Should change name of team to "t"
5. Log out by clicking the "Logout" button
6. Enter "t" and "t", then press submit
    
    -[X] Should go to team dashboard with "Welcome back t!" at the top

## User Story #13
#### As a game maker, I can delete a team

(Assuming server is started and web page is loaded to default)

1. Enter "maker1" and "maker1pwd", then press submit
2. Click "Delete Team" in the team1 card
    
    -[X] Card should disappear
3. Log out by clicking the "Logout" button
4. Enter "team1" and "team1pwd", then press submit
    
    -[X] Should display a login error

## User Story #17
#### As a team member, I can edit team data

(Assuming server is started and web page is loaded to default)

1. Enter "team1" and "team1pwd", then press submit
2. Click the "Edit Credentials" link
3. Fill in "t", "team1pwd", and "t"
4. Click "Change Credentials"
    
    -[X] Should display "Welcome back t!" at top
5. Log out by clicking the "Logout" button
6. Enter "t" and "t", then press submit

    -[X] Should display team dashboard with "Welcome back t!" at top
    
## User Story #19
#### As a game maker, I can edit a scavenger hunt's details

(Assuming server is started and web page is loaded to default)

1. Enter "maker1" and "maker1pwd", then press submit
2. Find and click the link labelled "Edit Game Details"
    
    -[X] Should display form
3. Change the values to "foo" and "bar"
4. Press "Edit Game Details" button below form
    
    -[X] Should return to main dashboard, with name as "foo"
    -[X] Should display description as "bar"
5. Find landmarks 1-4 to the right
6. Find and click the "Reorder" link below
7. Change the numbers in the upper left to 4, 3, 2, 1 for landmarks 1, 2, 3, and 4
8. Click "Submit Reorder"
    
    -[X] Should now display landmarks in order 4, 3, 2, 1
    -[X] Numbers in the corner of the Landmarks should correspond to their order    
    
## User Story #15
#### As a team member, I can request a confirmation question

(Assuming server is started and web page is loaded to default)

1. Enter "maker1" and "maker1pwd", then press submit
2. Click "Start Game"
3. Log out by clicking "Logout"
4. Enter "team1" and "team1pwd", then press submit
    
    -[X] Should display a "Request Question" link
5. Click "Request Question"
    
    -[X] Should display a question, time data, and a form to answer

## User Story #21
#### As a game maker, I can set a scoring scheme

(Assuming server is started and web page is loaded to default)

1. Enter "maker1" and "maker1pwd", then press submit
2. Click "Start Game"
3. Log out by clicking the "Logout" button
4. Enter "team1" and "team1pwd", then press submit
5. Request question, then submit answer "Answer 1"
    
    -[X] Should display score at top of screen
6. Request question, then submit answer "Answer 2"
    
    -[X] Should update score at top of screen
7. Log out by clicking the "Logout" button
8. Enter "maker1" and "maker1pwd", then press submit
9. Make a note of the score of team1
10. Click the "edit" link underneath the score scheme
11. Change the value of name to "test", wrong to 0, right to 10, and game per sec to -2
12. Click "Submit Edit"
    
    -[X] Should change score of team1 accordingly
    -[X] Should change score display along the top to reflect changes    

## User Story #23
#### As a game maker, I can start the game

(Assuming server is started and web page is loaded to default)

1. Enter "maker1" and "maker1pwd", then press submit
    
    -[X] Should display "Start Game" link
2. Click "Start Game"

    -[X] Should display page saying game started and the time at which it started
