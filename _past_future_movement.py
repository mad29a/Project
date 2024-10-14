import viz
import vizinfo
import vizact

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
    
    # Remove the existing test object if it exists
    if test_object:
        test_object.remove()
        test_object = None  # Reset the test_object variable

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
    print('Starting game...')
    hideMainMenu()
    hideInfoPanels()
    showAcademy()

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
    global test_object
    print('Traveling to the past...')
    viz.clearcolor([0.8, 0.5, 0.3])  # Set a color for the past scene
    returnButton.visible(viz.ON)
    hideInfoPanels()
    past.visible(viz.ON)  # Show the past info panel
    
    # Remove the existing test object if it exists
    if test_object:
        test_object.remove()

    # Load and position the test object in the past
    test_object = viz.add('main_c_objc/test_objc.obj')
    test_object.setPosition([0, 0, 0])  # Adjust position as needed

# Function to show the future scene
def showFutureScene():
    global test_object
    print('Traveling to the future...')
    viz.clearcolor([0.3, 0.3, 0.3])  # Set a color for the future scene
    returnButton.visible(viz.ON)  # Show the return button in the future scene
    hideInfoPanels()
    future.visible(viz.ON)  # Show the future info panel

    # Remove the existing test object if it exists
    if test_object:
        test_object.remove()

    # Load and position the test object in the future
    test_object = viz.add('main_c_objc/test_objc.obj')
    test_object.setPosition([0, 0, 0])  # Adjust position as needed


# Function to move the test object
def moveTestObject():
    if test_object:
        # Example movement speed
        speed = 0.1
        # Get the current position of the object
        current_position = test_object.getPosition()
        
        # Check keyboard input to determine direction
        if viz.key.isDown('w'):  # Move forward (along the z-axis)
            test_object.setPosition(current_position[0], current_position[1], current_position[2] + speed)
        if viz.key.isDown('s'):  # Move backward
            test_object.setPosition(current_position[0], current_position[1], current_position[2] - speed)
        if viz.key.isDown('a'):  # Move left
            test_object.setPosition(current_position[0] - speed, current_position[1], current_position[2])
        if viz.key.isDown('d'):  # Move right
            test_object.setPosition(current_position[0] + speed, current_position[1], current_position[2])



# Add an update event to call moveTestObject() regularly
vizact.ontimer(0.1, moveTestObject)  # Call every 0.1 seconds

# Setup key press event handlers for time travel
vizact.onkeydown('t', showPastScene)  # Press 't' to travel to the past
vizact.onkeydown('f', showFutureScene)  # Press 'f' to travel to the future

# Function to return to the academy from past/future
def returnToAcademy():
    print('Returning to the Academy...')
    # Hide past/future info panels and show the academy scene
    hideInfoPanels()
    showAcademy()

# Button event handlers
vizact.onbuttondown(startButton, startGame)
vizact.onbuttondown(rulesButton, showRules)
vizact.onbuttondown(exitButton, exitGame)
vizact.onbuttondown(backButton, backToMenu)
vizact.onbuttondown(quitButton, showQuitConfirmation)
vizact.onbuttondown(okButton, confirmQuit)
vizact.onbuttondown(cancelButton, cancelQuit)
vizact.onbuttondown(returnButton, returnToAcademy)