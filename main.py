import os
import time
import combat
import elements_db
# Expanded to 174 columns wide to safely fit two 80-character sprites side-by-side
if os.name == 'nt':
    os.system('mode con: cols=180 lines=45')
# NOTE: These imports will connect your existing files once they are fully built.
# import elements_db
# import combat
# import shop_index
# import ui_engine

### ENGLISH: Clears the terminal screen for smooth frame transitions.
### TAGALOG: Nililinis ng function na ito ang terminal screen para sa maayos na paglipat ng frame.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

### ENGLISH: The main game loop that acts as the Hub Menu connecting all game features.
### TAGALOG: Ang pangunahing game loop na nagsisilbing Hub Menu na nagkokonekta sa lahat ng feature ng laro.
def main_menu():
    is_running = True
    
    while is_running:
        clear_screen()
        print("==================================================")
        print("           PERIODIC MUTATION 118")
        print("==================================================")
        print("[1] Play Combat (10-Stage Gauntlet)")
        print("[2] Side Quests")
        print("[3] Practice")
        print("[4] Shop (Black Market)")
        print("[5] Periodic Index")
        print("[6] Exit Game")
        print("==================================================")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            print("\n>> LOADING COMBAT GAUNTLET...")
            time.sleep(1)
            combat.start_gauntlet()
            # combat.start_gauntlet() # Uncomment this to trigger your combat.py loop
        elif choice == '2':
            print("\n>> ACCESSING SIDE QUESTS...")
            time.sleep(1)
        elif choice == '3':
            print("\n>> LOADING PRACTICE SIMULATION...")
            time.sleep(1)
        elif choice == '4':
            print("\n>> ENTERING THE BLACK MARKET...")
            time.sleep(1)
            # shop_index.open_shop() 
        elif choice == '5':
            print("\n>> OPENING PERIODIC INDEX...")
            time.sleep(1)
            # shop_index.open_index() 
        elif choice == '6':
            print("\n>> SHUTTING DOWN TERMINAL...")
            time.sleep(1)
            is_running = False
        else:
            print("\n>> INVALID INPUT. Please enter a number from 1 to 6.")
            time.sleep(1)

### ENGLISH: Starts the game by executing the main menu function.
### TAGALOG: Sinisimulan ang laro sa pamamagitan ng pagtawag sa main menu function.
if __name__ == "__main__":
    main_menu()