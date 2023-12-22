import re
import hashlib
import json

def mdp(mot_de_passe):
    if len(mot_de_passe) < 8:
        return False
        
    
    if not re.search(r'\d', mot_de_passe):
        return False
    
    if not re.search(r'[A-Z]', mot_de_passe):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>-]', mot_de_passe):
        return False
    
    return True

def demander_mdp():
    while True:
    
        mot_de_passe = input("Entrez un mot de passe de au moins 8 caractères  : ")
            
        if mdp(mot_de_passe):
            print("Mot de passe fort. Merci!")
            mot_de_passe_crypte = crypte(mot_de_passe)
            print("Mot de passe crypté :", crypte(mot_de_passe))
            return mot_de_passe
        else:
            print("Mot de passe invalide veuillez entrez un mot de passe d'au moins 8 caractères avec Majuscule,caractères spéciaux et chiffres.")
        
def crypte(mot_de_passe):
    hachage = hashlib.sha256()
    mot_de_passe_bytes = mot_de_passe.encode('utf-8')
    hachage.update(mot_de_passe_bytes)
    mot_de_passe_hashe = hachage.hexdigest()
    
    return mot_de_passe_hashe
    

mot_de_passe = demander_mdp()


def enregistrer_mdp(mdp, cryp_mdp):
    mdp_list = [mdp, cryp_mdp]
    try:
        with open("mdp.json", "r") as gest:
            try:
                data = json.load(gest)
            except json.decoder.JSONDecodeError:
                data = []
    except FileNotFoundError:
        data = []

    with open("mdp.json", "w") as gest:
        data.append(cryp_mdp)
        json.dump(data, gest)
        print("ok")  
        



