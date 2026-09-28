Here is the expanded, highly detailed version of your mechanics section, structured professionally so you can copy and paste it directly into your Game Design Document. The wording has been adapted to explicitly reflect your strictly terminal-based Python architecture without GUI libraries.

## II. COMBAT STAGING & ANIMATION (CLI ARCHITECTURE)

**4. The Combat Frame Layout: High-Contrast ASCII Staging**

* **Left Anchor:** The Resonance Operator silhouette (e.g., Urahara-inspired coat and Gauntlet) remains statically printed on the left side of the terminal.


* **Right Anchor:** The randomly spawned anomaly, grouped into 10 elemental families and distinguished by specific ASCII symbols and ANSI colors.


* **UI Overlay:** A floating bottom section containing the dynamic Typing Prompt and the Spacebar Greed Gauge.



**5. Visual Mutation System (The Transformation)**

* The Left Anchor begins as the Human Scientist.


* Upon drinking a vial (Turn 1), a simulated screen flash occurs using a rapid sequence of `os.system('cls')` and ANSI white background codes (`\033[47m`) with a 50ms `time.sleep()` to simulate a canvas flash in the terminal.


* When the flash clears, the human ASCII is replaced by the Elemental Monster ASCII, or it projects behind the human as a ghostly aura in the specific color of that elemental family.



**6. ASCII Animation "Juice"**

* Text art is stored as static variables in a separate file (e.g., `elements_db.py` or `art_assets.py`) to prevent formatting breakage.


* Impact animation avoids redrawing text line-by-line; instead, it relies on rapid 70ms terminal clear-and-reprint loops to simulate flashes and screen shakes.



---

## III. PROGRESSION & LOADOUT SYSTEM

**7. The 10-Stage Gauntlet**

* A linear survival run from Stage 1 to 10 where the base enemy HP continuously scales up, and the player faces a random element from the 10 groups.



**8. The "Party Draft" System**

* **Stage 1:** The player starts with 3 random elements chosen from their unlocked Periodic Index.


* **Stages 2 & 3:** A post-match draft occurs where the game offers 3 random elements from the Index. The player picks 1 to add to their party until hitting the max capacity of 3 elements.


* **Stages 4 to 10:** Upon winning, the player must choose to either **Replace** (swap a current element for the newly dropped one) or **Decline/Absorb** (reject the element for a permanent stat buff, such as +20 Max HP or +10 Base Damage).



**9. Victory & Element Extraction**

* Defeating an anomaly shatters it into base particles. The player then has a chance to extract its specific core, permanently unlocking that element in the Periodic Index for all future runs.



---

## IV. CHEMISTRY RPG DEPTH

**10. In-Combat Swapping**

* With 2 or 3 elements equipped, loadout slots are mapped to the 1, 2, and 3 keys.


* Pressing a key mid-battle instantly shifts the Operator's active element, updating the character color and the Ultimate typing requirement to adapt to enemy threats.



**11. Elemental Rock-Paper-Scissors**

* Real-world chemistry dictates the damage multipliers. The 10 Elemental Groups feature specific combat buffs triggered upon landing an Ultimate Attack, alongside clear strengths and weaknesses.



Which of the 10 elemental groups (like Alkali Metals or Halogens) should we map out the specific strengths, weaknesses, and Ultimate buffs for next to complete your documentation?


We can absolutely build this. The secret to rendering smooth, colored animations in a pure command prompt without GUI libraries like Tkinter or Pygame is the strict 3-pillar architecture we established. By separating your visual data from your game logic, we can create a high-performance digital flipbook using only `while` loops, basic arrays, and conditional statements.

Here is the blueprint for your super structure:

* **Pillar 1: The Art Vault (`art_assets.py`):** We will store every massive ASCII drawing, UI border, and animation frame as static string variables and simple arrays. This prevents your game loops from becoming unreadable walls of text and protects the formatting.


* **Pillar 2: The Projector (`ui_engine.py`):** This file contains the screen-clearing command (`os.system('cls')`) and handles the ANSI color codes. To simulate animations like the 50ms white screen flash, we will use a `while` loop with a counter variable to cycle through your art arrays alongside `time.sleep()`.


* **Pillar 3: The Director (`combat.py`, `shop_index.py`, `main.py`):** This handles the raw game math, such as the Spacebar Greed Gauge timing, the 10-Stage Gauntlet progression, and the elemental Rock-Paper-Scissors damage multipliers. It will never print graphics directly; it will only send commands to the Projector.



Every single line of code we write will strictly adhere to your master lab rules, including the mandatory bilingual Tagalog and English comments and the absolute ban on `for` loops.

Should we begin by writing the `ui_engine.py` file to establish your screen-clearing and animation loop, or do you want to build the `elements_db.py` dictionary first to lock in the elemental stats and Synergy combos?