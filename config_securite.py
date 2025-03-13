# config_securite.py

# Liste des sites et applications autorisés sans confirmation
SITES_AUTORISES = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://openai.com"
]

# Fonction de vérification avant d'exécuter une action
def verifier_securite(action, cible):
    if cible in SITES_AUTORISES:
        return True  # Autorisé sans confirmation
    else:
        confirmation = input(f"Voulez-vous vraiment accéder à {cible} ? (oui/non) : ")
        return confirmation.lower() == "oui"