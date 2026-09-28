# ascii-periodic-mutation118
A 10-Stage Survival Gauntlet RPG based on the Periodic Table of Elements.

PERIODIC MUTATION 118 Project Lead & Main Engine Architect: Salvador John Patrick Collaborators: [Your Teammate's Name Here]

Project Overview "PERIODIC MUTATION 118" is a 10-Stage Survival Gauntlet RPG based on the Periodic Table of Elements. The game features a turn-based combat system where the player equips up to 3 elements to battle anomalies, utilizing simulated QTE timing and Elemental Type advantages.

Technical Architecture & Strict Lab Constraints This project operates entirely within the standard Command Prompt/Terminal using a strict State Machine loop, requiring zero external libraries to be installed. As the Lead Developer, I engineered the core loop to adhere to two strict master lab rules:

No GUI Libraries: The game runs 100% in the terminal using standard print() and input() functions. Libraries like tkinter, PyQt, or Pygame are strictly forbidden.

No 'For' Loops: All iterations, animations, and game loops are simulated entirely using while loops and counters.

CLI Scene Manager: Navigating between screens relies on clearing the terminal (os.system('cls')) and re-printing the new state. This "flipbook" method prevents text overlap and protects the complex ASCII art formatting.

Core Systems The Hub: A clean, text-based vertical main menu to access Combat, Side Quests, the Black Market Shop, and the Index.

Combat (Spacebar Greed Gauge): A high-risk timing system where players hold the spacebar and must release it in specific sweet spots, combined with a 2.0-second typing QTE for Ultimate attacks.

The Index: A master dictionary database holding all 118 elements, tracking their is_unlocked status, 2x damage advantages, and specific Ultimate buffs.

How to Run the Game Crucial: Do not run this game inside a basic IDE output window (like PyCharm or VSCode's default run panel), as they fail to process terminal clear commands or ANSI text color codes. Open your standard Command Prompt (Windows) or Terminal (Mac/Linux). Navigate to the folder where you saved the game files using the cd command. Type python main.py and press Enter.
