import time
import os
import random
import elements_db
import greed_gauge
import art_assets
import msvcrt
### ENGLISH: Clears the terminal screen for smooth frame transitions.
### TAGALOG: Nililinis ng function na ito ang terminal screen para sa maayos na paglipat ng frame.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

### ENGLISH: Renders the static layout: Player (Left), Enemy (Right), and reserves the Bottom for UI.
### TAGALOG: Iginuguhit ang static na layout: Player (Kaliwa), Enemy (Kanan), at inilalaan ang Ibaba para sa UI.
### ENGLISH: Shreds the background string into an array of individual rows (Index 0 to 14).
### TAGALOG: Hinahati ang background string sa isang array ng mga indibidwal na hilera (Index 0 hanggang 14).
### ENGLISH: The Master Text Compositor. Layers characters over the background using true transparency.
### TAGALOG: Ang Master Text Compositor. Pinapatong ang mga karakter sa background gamit ang tunay na transparency.
### ENGLISH: The Master Text Compositor with Floating Name Tags.
### TAGALOG: Ang Master Text Compositor na may Floating Name Tags.
def build_combat_frame(player_element, enemy_element, player_hp, enemy_hp):
    
    bg_lines = art_assets.bg_lab.strip('\n').splitlines()
    char_lines = art_assets.combat_silhouettes.strip('\n').splitlines()
    
    # 1. Build the dynamic Name Tag strings
    op_tag = f"[ {player_element} : {player_hp} HP ]"
    an_tag = f"[ {enemy_element} : {enemy_hp} HP ]"
    
    # 2. X/Y Coordinates 
    start_y = 6
    start_x = 2
    tag_y = 4 # The Name Tags float on Row 4
    
    rendered_frame = ""
    current_row = 0
    total_rows = len(bg_lines)
    
    while current_row < total_rows:
        current_bg_line = bg_lines[current_row].ljust(180) 
        bg_width = 180
        
        # --- LAYER 4: FLOATING NAME TAGS ---
        if current_row == tag_y:
            # Math: Align the enemy tag perfectly to the right wall
            an_start_x = bg_width - len(an_tag) - 3 
            
            # Slice the background into 5 pieces and glue the tags inside
            p1 = current_bg_line[:start_x]                  # Left wall padding
            p2 = op_tag                                     # Operator Tag
            p3 = current_bg_line[start_x + len(op_tag) : an_start_x] # Middle empty wall
            p4 = an_tag                                     # Anomaly Tag
            p5 = current_bg_line[an_start_x + len(an_tag):] # Right wall padding
            
            final_line = p1 + p2 + p3 + p4 + p5
            
        # --- LAYER 2: CHARACTER SILHOUETTES ---
        elif start_y <= current_row < (start_y + len(char_lines)):
            char_index = current_row - start_y
            char_text = char_lines[char_index]
            
            final_line = ""
            pixel_x = 0
            
            while pixel_x < bg_width:
                if start_x <= pixel_x < (start_x + len(char_text)):
                    char_pixel = char_text[pixel_x - start_x]
                    if char_pixel == " ":
                        final_line += current_bg_line[pixel_x]
                    else:
                        final_line += char_pixel
                else:
                    final_line += current_bg_line[pixel_x]
                pixel_x += 1
                
        # --- LAYER 1: UNTOUCHED BACKGROUND ---
        else:
            final_line = current_bg_line
            
        rendered_frame += final_line + "\n"
        current_row += 1
        
    # --- LAYER 3: BOTTOM UI BORDER ---
    ui_layer = f"""==================================================================
 >> HOLD SPACEBAR TO FILL! LIFT TO STRIKE! <<
=================================================================="""
    
    # Notice we removed the duplicate HP stats from the UI since they are now floating in the map!
    rendered_frame += ui_layer
    
    return rendered_frame


def execute_typing_qte(target_word):
    time_limit = 2.0
    
    # 1. Giant Warning Overlay
    os.system('cls')
    print("=" * 180)
    print("\n" * 12)
    print("ULTIMATE TRIGGERED!".center(180))
    print(f"PREPARE TO TYPE: [ {target_word} ]".center(180))
    print("\n" * 12)
    print("=" * 180)
    time.sleep(2.0)
    
    # 2. Live Countdown & Input Engine
    start_time = time.time()
    typed_word = ""
    is_active = True
    
    while is_active:
        time_left = time_limit - (time.time() - start_time)
        if time_left <= 0:
            time_left = 0.0
            is_active = False
            
        if msvcrt.kbhit():
            # Use getwch() instead of getwche() to prevent console buffer glitches
            char = msvcrt.getwch() 
            if char == '\r':
                is_active = False
            elif char == '\b': # Backspace support
                typed_word = typed_word[:-1]
            elif char.isalnum():
                typed_word += char

        # 3. Render Live Clock Frame
        os.system('cls')
        print("=" * 180)
        print("\n" * 12)
        print(f"TARGET SYMBOL: [ {target_word} ]".center(180))
        print(f">> CLOCK: {time_left:.1f} SECONDS <<".center(180))
        print("\n")
        print(f"YOUR INPUT: {typed_word}".center(180))
        print("\n" * 12)
        print("=" * 180)
        
        time.sleep(0.05)

    # 4. Result
    if typed_word.strip().lower() == target_word.lower() and time_left > 0:
        return True
    else:
        return False
### ENGLISH: The main combat loop featuring map selection, atomic weight speed checks, and turn taking.
### TAGALOG: Ang pangunahing combat loop na may pagpili ng mapa, atomic weight speed checks, at palitan ng turn.
def start_gauntlet():
    available_elements = ["Na", "Cl", "Ar"]
    
    # 1. PRE-BATTLE MAP SELECTION[cite: 4]
    is_picking_map = True
    while is_picking_map:
        clear_screen()
        print(">> SELECT YOUR BATTLE MAP:")
        print("[1] The Abandoned Lab")
        print("[2] The Radioactive Wasteland")
        
        map_choice = input("> ")
        if map_choice == "1" or map_choice == "2":
            is_picking_map = False
        else:
            print(">> Invalid coordinates. Try again.")
            time.sleep(1)

    # 2. SETUP STATS (Random Pulls)
    player_hp = 100
    enemy_hp = 150
    player_active = random.choice(available_elements)
    enemy_active = random.choice(available_elements)
    
    # 3. TURN ORDER CALCULATION (Lowest Weight goes first)
    player_weight = elements_db.elements_database[player_active]["weight"]
    enemy_weight = elements_db.elements_database[enemy_active]["weight"]
    
    is_player_turn = False
    clear_screen()
    print(build_combat_frame(player_active, enemy_active, player_hp, enemy_hp))


    if player_weight <= enemy_weight:
        is_player_turn = True
        print(f">> Operator Weight [{player_weight}] <= Anomaly Weight [{enemy_weight}].")
        print(">> YOU TAKE THE FIRST TURN!")
    else:
        print(f">> Anomaly Weight [{enemy_weight}] < Operator Weight [{player_weight}].")
        print(">> ENEMY STRIKES FIRST!")
    time.sleep(3)

    # 4. THE TURN-BY-TURN LOOP
    is_battling = True
    while is_battling:
        # Standard Turn Rendering
        clear_screen()
        print(build_combat_frame(player_active, enemy_active, player_hp, enemy_hp))
        
        if is_player_turn:
            print(">> YOUR TURN! What will you do?")
            print("[A] Attack (Greed Gauge)")
            print("[Q] Quit & Flee to Hub")
            
            action = input("> ").lower()
            
            if action == 'q':
                print("\n>> RETREATING! Run aborted.")
                time.sleep(2)
                is_battling = False
                
            elif action == 'a':
                # Pass the new 'build' function so the gauge can grab the text string
                attack_result = greed_gauge.visual_greed_gauge(
                    lambda: build_combat_frame(player_active, enemy_active, player_hp, enemy_hp)
                )
                
                # Apply Damage
                if attack_result == "normal":
                    enemy_hp -= 20
                elif attack_result == "ultimate":
                    enemy_hp -= 40
                elif attack_result == "backfire":
                    player_hp -= 15
                elif attack_result == "meltdown":
                    player_hp -= 25
                
                is_player_turn = False # Pass turn to enemy
            else:
                print(">> Invalid input.")
                time.sleep(1)
                
        else:
            # 5. ENEMY TURN LOGIC
            print(f">> ANOMALY'S TURN! [{enemy_active}] is charging an attack...")
            time.sleep(2)
            
            enemy_damage = 15
            player_hp -= enemy_damage
            print(f">> Anomaly dealt {enemy_damage} damage!")
            time.sleep(2)
            
            is_player_turn = True # Pass turn back to player

       
        # 6. WIN/LOSS CONDITIONS
        if enemy_hp <= 0:
            clear_screen()
            print(build_combat_frame(player_active, enemy_active, player_hp, 0))
            print(">> ANOMALY DEFEATED! You survived.")
            is_battling = False
            time.sleep(3)
            
        elif player_hp <= 0:
            clear_screen()
            print(build_combat_frame(player_active, enemy_active, 0, enemy_hp))
            print(">> OPERATOR DEFEATED! Run Over.")
            is_battling = False
            time.sleep(3)