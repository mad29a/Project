"""
nepieciesams:
uzlabot kamera movement lai ar peli griežas objekts un peles kursors nerādās
"""
"""
ir pievienotas grīdas, kas paradas tikai noteiktajos scene, tas nozime, katram scene ir sava grīda

tacu sis grīdas bus velak jamaina jo nevar iazmantot vizshape, paslaik tie ir ka placeholders
"""

import viz
import vizinfo
import vizact
import vizshape
import vizmat #attaluma aprekinasa 

# Start the Vizard environment
viz.go()

# Create an info window for the main menu, positioned at the top of the screen
menu = vizinfo.InfoPanel('Time Travelers Academy: Final Exam', align=viz.ALIGN_CENTER_TOP, icon=False)
menu.setPosition([0.5, 0.8, 0])  # Adjust the Y position to move it towards the top
menu.visible(viz.ON)

# Create an info window for the exam hall, positioned at the top of the screen
hall = vizinfo.InfoPanel('Exam Hall', align=viz.ALIGN_CENTER_TOP, icon=False)
hall.setPosition([0.5, 0.8, 0])  # Adjust the Y position to move it towards the top
hall.visible(viz.OFF)

# Create an info window for the past, positioned at the top of the screen
past = vizinfo.InfoPanel('Current timeline: Past', align=viz.ALIGN_CENTER_TOP, icon=False)
past.setPosition([0.5, 0.8, 0])  # Adjust the Y position to move it towards the top
past.visible(viz.OFF)

# Create an info window for the future, positioned at the top of the screen
future = vizinfo.InfoPanel('Current timeline: Future', align=viz.ALIGN_CENTER_TOP, icon=False)
future.setPosition([0.5, 0.8, 0])  # Adjust the Y position to move it towards the top
future.visible(viz.OFF)

# Create an info window for rules, positioned at the top of the screen
rules = vizinfo.InfoPanel('Rules', align=viz.ALIGN_CENTER_TOP, icon=False)
rules.setPosition([0.5, 0.8, 0])  # Adjust the Y position to move it towards the top
rules.visible(viz.OFF)

# Create an info window for displaying the current number of attempts
attemptsDisplay = vizinfo.InfoPanel('Attempts: 0/10', align=viz.ALIGN_LEFT_TOP, icon=False)
attemptsDisplay.setPosition([0.05, 0.95, 0])  # Adjust position: [X, Y, Z]
attemptsDisplay.visible(viz.OFF)  # Make it visible initially


# Add start game button
startButton = viz.addButtonLabel('Start Game')
startButton.setPosition([0.5, 0.6, 0])

# Add rules button
rulesButton = viz.addButtonLabel('Rules')
rulesButton.setPosition([0.5, 0.5, 0])

# Add exit button
exitButton = viz.addButtonLabel('Exit')
exitButton.setPosition([0.5, 0.4, 0])

# Create the Quit button but hide it initially
quitButton = viz.addButtonLabel('Quit')
quitButton.setPosition([0.95, 0.05, 0])
quitButton.visible(viz.OFF)  # Make the Quit button invisible initially

# Create a "Back" button for the rules section, initially hidden
backButton = viz.addButtonLabel('Back')
backButton.setPosition([0.5, 0.1, 0])
backButton.visible(viz.OFF)

# Create a "Return" button for returning to the academy, initially hidden
returnButton = viz.addButtonLabel('Return')
returnButton.setPosition([0.1, 0.1, 0])
returnButton.visible(viz.OFF)

# Create the confirmation dialog for quitting
confirmQuitPanel = vizinfo.InfoPanel('Are you sure you want to quit? All progress will be lost.', align=viz.ALIGN_CENTER, icon=False)
confirmQuitPanel.setPosition(0, 0)  # Center the confirmation panel
confirmQuitPanel.visible(viz.OFF)  # Hide the panel initially

# Add OK and Cancel buttons to the confirmation dialog
okButton = viz.addButtonLabel('OK')
okButton.setPosition([0.4, 0.4, 0])
okButton.visible(viz.OFF)

cancelButton = viz.addButtonLabel('Cancel')
cancelButton.setPosition([0.6, 0.4, 0])
cancelButton.visible(viz.OFF)


# Global variable for the test object
test_object = None

def followTestObject():
    if test_object:
        # Define the offset position behind the object
        offset = [0, 6, -12]  # [X, Y, Z] - Adjust for height and distance
        # Get the object's current position
        object_position = test_object.getPosition()
        # Update the camera position to maintain the offset from the object
        viz.MainView.setPosition(
            object_position[0] + offset[0],
            object_position[1] + offset[1],
            object_position[2] + offset[2]
        )
        # Make the camera look at the object
        viz.MainView.lookAt(test_object.getPosition())
        # Adjust the camera to tilt upward
        viz.MainView.setEuler([0, 9, 0])  # Change the second value to adjust upward tilt angle


# Function to hide extra info panels
def hideInfoPanels():
    menu.visible(viz.OFF)
    hall.visible(viz.OFF)
    past.visible(viz.OFF)
    future.visible(viz.OFF)
    rules.visible(viz.OFF)
    

# Function to hide main menu buttons and show the Quit button
def hideMainMenu():
    menu.visible(viz.OFF)
    startButton.visible(viz.OFF)
    rulesButton.visible(viz.OFF)
    exitButton.visible(viz.OFF)
    quitButton.visible(viz.ON)

# Function to show main menu buttons and hide other buttons
def showMainMenu():
    global test_object  # Declare test_object as a global variable
    startButton.visible(viz.ON)
    rulesButton.visible(viz.ON)
    exitButton.visible(viz.ON)
    quitButton.visible(viz.OFF)
    backButton.visible(viz.OFF)
    returnButton.visible(viz.OFF)
    confirmQuitPanel.visible(viz.OFF)
    okButton.visible(viz.OFF)
    cancelButton.visible(viz.OFF)
    hideInfoPanels()  # Hide all info panels first
    menu.visible(viz.ON)  # Show the main menu last
    
    # Hide attempts display in the main menu
    attemptsDisplay.visible(viz.OFF)
    
    # Remove the existing test object if it exists
    if test_object:
        test_object.remove()
        test_object = None  # Reset the test_object variable


# Global variables for time travel attempts and tracking travel state
time_travel_attempts = 0
MAX_ATTEMPTS = 10
is_traveling = False  # Track if the player is currently in a time-travel phase

#global variable for floor
current_floor = None


# Global variable to store the collectible object
collectible_object = None


#function to remove the collectible obj
def removeCollectObject():
    global collectible_object
    
    if collectible_object:
        collectible_object.remove()
        collectible_object = None
    

#Function to remove the current floor if it exists
def removeCurrentFloor():
    global current_floor
    if current_floor:
        current_floor.remove()  # Remove the floor
        current_floor = None  # Reset the floor variable

# Function to show the rules and "Back" button
def showRules():
    print('Showing rules...')
    hideMainMenu()
    hideInfoPanels()  # Hide all info panels before showing rules
    quitButton.visible(viz.OFF)
    backButton.visible(viz.ON)
    rules.visible(viz.ON)  # Show the rules info panel

# Function to handle the Back button click (return to main menu from rules)
def backToMenu():
    print('Returning to main menu from rules...')
    hideInfoPanels()
    showMainMenu()

# Function to show the confirmation dialog when quitting
def showQuitConfirmation():
    confirmQuitPanel.visible(viz.ON)
    okButton.visible(viz.ON)
    cancelButton.visible(viz.ON)

# Function to handle the OK button click (confirm quit)
def confirmQuit():
    global current_floor
    
    removeCollectObject()
    removeCurrentFloor()
    print('Returning to main menu...')
    showMainMenu()
    

# Function to handle the Cancel button click (stay in the current scene)
def cancelQuit():
    confirmQuitPanel.visible(viz.OFF)
    okButton.visible(viz.OFF)
    cancelButton.visible(viz.OFF)
    print('Continue in the current scene.')

# Function to handle the Exit button click
def exitGame():
    viz.quit()

# Function to start the game
def startGame():
    global time_travel_attempts  # Declare time_travel_attempts as a global variable
    print('Starting game...')
    time_travel_attempts = 0  # Reset attempts to zero when starting the game
    hideMainMenu()
    hideInfoPanels()
    showAcademy()

    # Show attempts display when the game starts
    attemptsDisplay.visible(viz.ON)  # Show attempts display


# Function to show the academy scene
def showAcademy():
    global test_object  # Declare test_object as a global variable
    print('Showing the Academy scene...')
    viz.clearcolor(viz.SKYBLUE)  # Set a sky-blue background as a placeholder for the Academy
    returnButton.visible(viz.OFF)
    hideInfoPanels()
    hall.visible(viz.ON)  # Show the exam hall info panel

    # Remove the existing test object if it exists when returning to the academy
    if test_object:
        test_object.remove()
        test_object = None  # Reset the test_object variable


# Function to show the past scene
def showPastScene():
    removeCollectObject()
    global test_object, is_traveling, time_travel_attempts, current_floor, collectible_object
    
    # Remove existing floor when transitioning to a new scene
    removeCurrentFloor()
    
    # Create a floor under the player
    current_floor = vizshape.addPlane(size=(30, 30), axis=vizshape.AXIS_Y)
    current_floor.setPosition([0, 0, 0])  # Position the floor at the player's level
    current_floor.color(viz.GRAY)  # Set the floor color to gray

    if time_travel_attempts >= MAX_ATTEMPTS:
        print('You have reached the maximum number of time travel attempts. Game Over.')
        showGameOver()
        return
    
    print('Traveling to the past...')
    is_traveling = True
    viz.clearcolor([0.8, 0.5, 0.3])  # Set background color for the past
    returnButton.visible(viz.ON)
    hideInfoPanels()
    past.visible(viz.ON)
    
    # Remove existing test object if it exists
    if test_object:
        test_object.remove()
    
    # Add the test object and set its position
    test_object = viz.add('main_c_objc/test_objc.obj')
    test_object.setPosition([0, 0, 0])
    
    # Load and position the collectible object (ball) in the past
    collectible_object = viz.add('main_c_objc/BasicStarterObject.obj')
    collectible_object.setPosition([10, 0.8, 0])  # Adjust position as needed
    
    # Enable collision detection for the collectible object (ball)
    collectible_object.collideMesh()  # Ensures the object uses collision system
    collectible_object.disable(viz.DYNAMICS)  # Keep the object static, prevent movement

    # Start following the object with the camera
    vizact.ontimer(0, followTestObject)


# Function to handle object collection
def collectObject():
    global collectible_object, test_object

    if collectible_object and test_object:
        # Iegūst test_object pozīciju
        player_position = test_object.getPosition()  # Izmanto test_object pozīciju

        # Iegūst savācama objekta pozīciju
        object_position = collectible_object.getPosition()

        # Aprēķina attālumu starp test_object un savācamo objektu
        distance = vizmat.Distance(player_position, object_position)

        # Ja attālums ir mazāks par 2 vienībām, objekts tiek savākts
        if distance < 2.0:  # Ja attālums ir mazāks par 2 vienībām
            print('Object collected!')  # Izvada ziņojumu uz konsoles
            collectible_object.remove()  # Noņem objektu no scēnas
            collectible_object = None  # Notīra objektu no mainīgā
            showCollectedMessage()  # Parāda ziņojumu ekrānā

# Function to show a message that the object was collected
def showCollectedMessage():
    # Izveido info paneli ar savākšanas ziņojumu
    collectedMessage = vizinfo.InfoPanel('Object has been collected!', align=viz.ALIGN_CENTER, icon=False)
    #collectedMessage.setPosition([0, 0, 0])  # Novieto ziņojumu ekrāna augšējā daļā
    collectedMessage.visible(viz.ON)

    # Automātiski paslēpj ziņojumu pēc 2 sekundēm
    vizact.ontimer(3, collectedMessage.remove)

# Pievieno šo funkciju regulāram pārbaudījumam
vizact.ontimer(0.1, collectObject)  # Pārbauda ik pēc 0.1 sekundēm


# Function to show the future scene
def showFutureScene():
    removeCollectObject()
    global test_object, is_traveling, time_travel_attempts, current_floor, collectible_object
    
    # Remove the existing floor when transitioning to a new scene
    removeCurrentFloor()

    # Create a floor under the player
    current_floor = vizshape.addPlane(size=(30, 30), axis=vizshape.AXIS_Y)
    current_floor.setPosition([0, 0, 0])  # Position the floor at the player's level
    current_floor.color(viz.GREEN)  # Set the floor color to gray

    if time_travel_attempts >= MAX_ATTEMPTS:
        print('You have reached the maximum number of time travel attempts. Game Over.')
        showGameOver()
        return
    
    print('Traveling to the future...')
    is_traveling = True
    viz.clearcolor([0.3, 0.3, 0.3])  # Set background color for the future
    returnButton.visible(viz.ON)
    hideInfoPanels()
    future.visible(viz.ON)
    
    # Remove existing test object if it exists
    if test_object:
        test_object.remove()
    
    # Add the test object and set its position
    test_object = viz.add('main_c_objc/test_objc.obj')
    test_object.setPosition([0, 0, 0])

    # Ielādē un novieto savācamo objektu (bumbiņu) nākotnē
    collectible_object = viz.add('main_c_objc/BasicStarterObject.obj')
    collectible_object.setPosition([10, 0.8, 0])  # Pielāgo pozīciju pēc vajadzības
    
    # Aktivizē sadursmju noteikšanu savācamajam objektam (bumbiņai)
    collectible_object.collideMesh()  # Nodrošina, ka objekts izmanto sadursmju sistēmu
    collectible_object.disable(viz.DYNAMICS)  # Neļauj objektam kustēties, saglabā to statisku
    # Start following the object with the camera
    vizact.ontimer(0, followTestObject)



# Helper function for linear interpolation
def lerp(start, end, factor):
    return start + factor * (end - start)

# Example of smooth movement using interpolation
def moveTestObject():
    if test_object:
        # Movement speed factor
        speed = 1
        
        # Get current position of the object
        current_position = test_object.getPosition()

        # Define target position to move towards
        target_position = list(current_position)
        
        # Check keyboard input and update target position smoothly
        if viz.key.isDown('w'):  # Move forward (along the z-axis)
            target_position[2] += speed
        if viz.key.isDown('s'):  # Move backward
            target_position[2] -= speed
        if viz.key.isDown('a'):  # Move left
            target_position[0] -= speed
        if viz.key.isDown('d'):  # Move right
            target_position[0] += speed

        # Smoothly interpolate towards the target position
        new_position = [
            lerp(current_position[0], target_position[0], 0.05),  # X-axis interpolation
            current_position[1],  # Keep Y constant
            lerp(current_position[2], target_position[2], 0.05)   # Z-axis interpolation
        ]
        test_object.setPosition(new_position)



# Add an update event to call moveTestObject() regularly
vizact.ontimer(0.1, moveTestObject)  # Call every 0.1 seconds

# Setup key press event handlers for time travel
vizact.onkeydown('t', showPastScene)  # Press 't' to travel to the past
vizact.onkeydown('f', showFutureScene)  # Press 'f' to travel to the future


# Function to return to the academy from past/future
def returnToAcademy():
    removeCollectObject()
    global time_travel_attempts, is_traveling, current_floor
    print('Returning to the Academy...')
    
    # Remove the existing floor when transitioning to a new scene
    removeCurrentFloor()
    
    # Only increment attempts if the player was traveling
    if is_traveling:
        time_travel_attempts += 1  # Increment attempts on returning
        print(f'Attempt {time_travel_attempts}/{MAX_ATTEMPTS}')
        is_traveling = False  # Reset the traveling state when back at the academy
    
    # Hide past/future info panels and show the academy scene
    hideInfoPanels()
    showAcademy()

    # Update the attempts display
    attemptsDisplay.setText(f'Attempts: {time_travel_attempts}/{MAX_ATTEMPTS}')
    
    # Check if the attempts have reached the maximum limit after returning
    if time_travel_attempts >= MAX_ATTEMPTS:
        showGameOver()  # Show game over if the maximum attempts are reached

    # Stop following the object with the camera
    vizact.ontimer2(0, 0, followTestObject)  # Stop the follow action


# Function to handle game over scenario
def showGameOver():
    # Display a game-over message and reset the game or prevent further actions
    gameOverPanel = vizinfo.InfoPanel('Game Over: You have reached the maximum number of time travel attempts.', align=viz.ALIGN_CENTER, icon=False)
    gameOverPanel.setPosition(0, 0)  # Center the message panel
    gameOverPanel.visible(viz.ON)
    # Hide return button or other controls if needed
    returnButton.visible(viz.OFF)

    # Optionally, disable further time travel or restart the game
    vizact.onkeydown('t', lambda: print('No more time travel attempts allowed.'))
    vizact.onkeydown('f', lambda: print('No more time travel attempts allowed.'))

# Button event handlers
vizact.onbuttondown(startButton, startGame)
vizact.onbuttondown(rulesButton, showRules)
vizact.onbuttondown(exitButton, exitGame)
vizact.onbuttondown(backButton, backToMenu)
vizact.onbuttondown(quitButton, showQuitConfirmation)
vizact.onbuttondown(okButton, confirmQuit)
vizact.onbuttondown(cancelButton, cancelQuit)
vizact.onbuttondown(returnButton, returnToAcademy)
