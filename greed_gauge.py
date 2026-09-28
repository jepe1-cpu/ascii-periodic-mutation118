import os
import time
import random

if os.name == 'nt':
    os.system('')    # Enables colors and flicker-free drawing on Windows
    import msvcrt    # Enables reading the spacebar in real-time

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

### ENGLISH: Clears the terminal screen for smooth frame transitions.
### TAGALOG: Nililinis ng function na ito ang terminal screen para sa maayos na paglipat ng frame.
def clear_screen():
    # \033[H moves the cursor Home (top-left) without deleting the background buffer
    print("\033[H", end="", flush=True)
### ENGLISH: Allows the player to fill the gauge by pressing spacebar, firing when they stop.
### TAGALOG: Pinapayagan ang manlalaro na punuin ang gauge gamit ang spacebar, at aatake kapag tumigil sila.
def visual_greed_gauge(draw_top_screen):
    print(f"\n{CYAN}>> GET READY!{RESET}")
    print(">> HOLD or MASH the SPACEBAR to fill the gauge.")
    print(">> STOP pressing to lock in your attack!")
    time.sleep(2.5)

    # Clear accidental early presses
    if os.name == 'nt':
        while msvcrt.kbhit():
            msvcrt.getch()

    percent = 0.0
    is_charging = True
    last_press_time = time.time()
    bar_width = 40

    # Strict rule applied: Using while loop instead of for loop
    while is_charging:
        current_time = time.time()
        
        # Check for spacebar input
        if os.name == 'nt' and msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b' ':
                # Random Speedup Mechanic: Adds a random amount of progress per tick
                percent += random.uniform(1.0, 5.0)
                last_press_time = time.time() # Reset the stop timer

        # The "Release" Trigger: If you haven't pressed space in 0.6 seconds, it fires!
        if percent > 0 and (current_time - last_press_time > 0.5):
            is_charging = False

        if percent >= 100:
            percent = 100
            is_charging = False

        # Determine colors and active zones based on percentage
        if percent < 20:
            bar_color = RED
            zone_text = "MISFIRE (0-19%)"
        elif percent < 80:
            bar_color = GREEN
            zone_text = "NORMAL ATTACK (20-79%)"
        elif percent < 90:
            bar_color = RED
            zone_text = "BACKFIRE (80-89%)"
        elif percent <= 95:
            bar_color = YELLOW
            zone_text = "ULTIMATE SWEET SPOT (90-95%)"
        else:
            bar_color = RED
            zone_text = "MELTDOWN (96-100%)"

        # Calculate filled vs empty blocks without using for loops
       # Calculate filled vs empty blocks
        filled_blocks = int((percent / 100) * bar_width)
        bar_fill = "█" * filled_blocks
        bar_empty = "-" * (bar_width - filled_blocks)

        # 1. Grab the top map and characters from combat.py
        top_half = draw_top_screen() 
        
        # 2. Build the moving gauge as a text block
        bottom_half = f"""
{CYAN}================ GREED GAUGE ================{RESET}
ZONE: {bar_color}{zone_text}{RESET}
[{bar_color}{bar_fill}{bar_empty}{RESET}] {percent:.1f}%
{CYAN}============================================={RESET}
{YELLOW}>> HOLD SPACEBAR TO FILL! LIFT TO STRIKE! <<{RESET}
"""
        
        # 3. ONE ATOMIC PRINT: Teleports cursor (\033[H) and pastes the entire combined screen instantly
        print(f"\033[H{top_half}{bottom_half}", end="", flush=True)

        time.sleep(0.05) 

    # Final Resolution Logic
    clear_screen()
    draw_top_screen()
    print(f"\n{CYAN}>> You locked in at {percent:.1f}%!{RESET}")
    time.sleep(1.5)
    
    if percent < 20:
        return "misfire"
    elif percent < 80:
        return "normal"
    elif percent < 90:
        return "backfire"
    elif percent <= 95:
        return "ultimate"
    else:
        return "meltdown"