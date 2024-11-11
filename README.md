# Project
Funkijas

Time Travelers Academy: Final Exam 

*main concept* 

Overview: You are a student at the Time Travelers Academy, and your final exam will determine whether you graduate or get expelled. The exam is simple but challenging: retrieve two artifacts—one from the past and one from the future—within 10 attempts. Success means you graduate as a time traveler; failure means game over. 

Core Mechanics 
The 10-Try Rule: 
You have 10 chances (attempts) to complete the exam. Each attempt counts when you travel to a time period to search for an artifact. 
If you successfully retrieve both artifacts in 10 tries or less, you graduate. If you use up all 10 attempts without success, you fail and are expelled. 
Artifacts & Time Travel: 
Past Artifact: You must retrieve this one first. It’s hidden in a historical era, like ancient Egypt or medieval Europe. 
Future Artifact: Unlocked only after retrieving the past artifact. It’s hidden in a future timeline, such as a cyberpunk city or a dystopian world. 
After collecting both, you must safely return to the Academy to complete the exam. 

Fitting In (Disguise System): 
Before entering a time period, you choose a disguise that helps you blend in. 
Wearing the right disguise keeps you from being spotted by locals, making it easier to search for the artifact. 
If you’re not dressed appropriately or act suspiciously, locals or guards will become suspicious and make it harder for you to complete your mission. 
Simplified Gameplay Flow 
Start at the Academy: 
Get your mission briefing and the rules for your exam. 
Choose your disguise and prepare for the time jump. 

Travel to the Past: 
Search for clues to find the location of the past artifact. 
Solve a few basic puzzles (e.g., figuring out a hidden compartment in a temple). 
Avoid suspicion by acting like a local. 
Return to the Academy with the Past Artifact: 
If successful, unlock the ability to travel to the future. 

Travel to the Future: 
Use similar mechanics to find the future artifact, with different challenges and obstacles. 
Technology or advanced puzzles will replace ancient traps, but the core idea of fitting in remains. 
Return to the Academy with Both Artifacts: 
Graduation if successful, game over if you exceed 10 attempts. 



Building stages:  
Game logic devided into smaller pieces of functions and main objectives ( to work on step by step )  whole game gets divided into 5 phases, that are after made into even smaler parts, to be able to retrive funcitons if something goes wrong 

Phase 1: Core Structure & Basic game logic 
 1. 1 Main menu -  
 Simple starting screen with options like "Start Game" , "Exit", "Rules"  
 1.2. Scene managment System  
 Set up function to change between scenes/ times, example "Main menu" to "exam hall" 
 Izveidot simple enviroments for each time ( placeholder scenes) 
 1.3 Basic player Movement : 
 Create a simple 3d object for main character 
 Make navigation system for it soo it can move at the past and future time	 

Phase 2: Time travel and missions 
  2.1 Time travel funcionality  
  create a simple way to trigger time travel – for example trigger with letter "t" so it stands for travel  
  implement 10-try rule – function that counts tries and after 10 does not let continue or says game over 
  2.2 timeline missions  
  make a concept for each time like collect staff or motherboerd 
  make a understanding concept for detecting if player is in disguises 
  2.3 return Mechanics:  
  create a function for returning to academy after finding the past artifact 
  if successful unlock the future timeline 

Phase 3:  Game mechanics 
  3.1 Disguise system: 
  implement a simple system where the player can choose a disguise before starting the mission 
  detetion system, if the player chooses the wrong disguises he has less time to collect the artifact and a waring shows on the screen 
  3.2 artifact collection system :  
  create a way to track if the player has retrives the artifact ( give it a index or somethin like that)  
  include visual indicators, for example, if collected there shows option to return to academy. Or create a UI that shows artifact at the screen 

Phase 4:  Polishing & Extra Features 
 4.1  Game over and Succed Conditions 
 add a game over screen  
 create a simple "Congrulations" screen for successfully retrivieng both artifacts 

Phase 5:  Visuals and final touches 
 5.1. Art & Graphich 
 replace placeholders with better graphics 
 create animations if possible 
 5.2 Sounds & Music  
 add a background music for different scenes ( academy, past and future) 
 sound effects for collecting items and alerts or try usage 
 5.3. Testing  
 test the whole game, make the fixes if neded.  


Main character: Student for time travel academy  



 

 

