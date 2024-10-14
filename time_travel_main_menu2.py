import viz
import vizinfo
import vizact

viz.go()
# Create an info window for the main menu, positioned at the top of the screen
menu = vizinfo.InfoPanel('Time Travelers Academy', align=viz.ALIGN_CENTER_TOP, icon=False)
menu.setPosition([0.5, 0.8, 0])  # Adjust the Y position to move it towards the top
menu.visible(viz.ON)

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

# Function to hide main menu buttons and show the Quit button
def hideMainMenu():
    menu.visible(viz.OFF)
    startButton.visible(viz.OFF)
    rulesButton.visible(viz.OFF)
    exitButton.visible(viz.OFF)
    quitButton.visible(viz.ON)

# Function to show main menu buttons and hide other buttons
def showMainMenu():
    menu.visible(viz.ON)
    startButton.visible(viz.ON)
    rulesButton.visible(viz.ON)
    exitButton.visible(viz.ON)
    quitButton.visible(viz.OFF)
    backButton.visible(viz.OFF)
    confirmQuitPanel.visible(viz.OFF)
    okButton.visible(viz.OFF)
    cancelButton.visible(viz.OFF)

# Function to show the rules and "Back" button
def showRules():
    print('Showing rules...')
    hideMainMenu()
    quitButton.visible(viz.OFF)
    backButton.visible(viz.ON)
    # Display rules or any other content here

# Function to handle the Back button click (return to main menu from rules)
def backToMenu():
    print('Returning to main menu from rules...')
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
    showAcademy()

# Define scenes as separate functions
def showAcademy():
    print('Showing the Academy scene...')
    viz.clearcolor(viz.SKYBLUE)  # Set a sky-blue background as a placeholder for the Academy

# Assign the button actions
vizact.onbuttondown(startButton, startGame)
vizact.onbuttondown(rulesButton, showRules)
vizact.onbuttondown(exitButton, exitGame)
vizact.onbuttondown(quitButton, showQuitConfirmation)
vizact.onbuttondown(okButton, confirmQuit)
vizact.onbuttondown(cancelButton, cancelQuit)
vizact.onbuttondown(backButton, backToMenu)
