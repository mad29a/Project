import viz
import vizinfo

viz.go(viz.FULLSCREEN)

#Speles nosaukums virs mainmenu screen
menu = vizinfo.InfoPanel('Time Travelers Academy', align=viz.ALIGN_CENTER_TOP, icon=False)


#POGU PIEVIENOSANA
startButton = viz.addButtonLabel('Start Game') #Start Game
startButton.setPosition([0.5, 0.6, 0])

optionsButton = viz.addButtonLabel('Rules') #Rules
optionsButton.setPosition([0.5, 0.5, 0])

exitButton = viz.addButtonLabel('Exit') #EXIT
exitButton.setPosition([0.5, 0.4, 0])

# funkcijas, kas tiek palaistas kad nospiez pogas
def startGame():
    print('Starting game...')
    showAcademy()

def openOptions():
    print('Options menu coming soon...')

def exitGame():
    viz.quit()

# Pievieno funkcijas pogām 
startButtonDown = vizact.onbuttondown(startButton, startGame)
optionsButtonDown = vizact.onbuttondown(optionsButton, openOptions)
exitButtonDown = vizact.onbuttondown(exitButton, exitGame)

# Define scenes as separate functions
def showAcademy():
    print('Showing the Academy scene...')
    viz.clearcolor(viz.SKYBLUE)  #placeholder for the Academy
