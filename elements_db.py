### ENGLISH: The master dictionary holding all permanent element stats and synergy rules.
### TAGALOG: Ang pangunahing dictionary na naglalaman ng lahat ng permanenteng stats at synergy rules ng elemento.
### ENGLISH: The master dictionary holding all permanent element stats, now including atomic weight for turn order.
### TAGALOG: Ang pangunahing dictionary na naglalaman ng permanenteng stats, kabilang ang atomic weight para sa turn order.
elements_database = {
    "Na": {
        "name": "Sodium",
        "family": "Alkali Metals",
        "weight": 22.99, # <--- Added for speed calculation
        "advantage": "Halogens",
        "buff": "Pyrophoric Strike", 
        "is_unlocked": True
    },
    "Cl": {
        "name": "Chlorine",
        "family": "Halogens",
        "weight": 35.45, # <--- Added for speed calculation
        "advantage": "Alkali Metals",
        "buff": "Corrosive Gas", 
        "is_unlocked": False
    },
    "Ar": {
        "name": "Argon",
        "family": "Noble Gases",
        "weight": 39.95, # <--- Added for speed calculation
        "advantage": "None",
        "buff": "Inert Aura", 
        "is_unlocked": True
    }
}