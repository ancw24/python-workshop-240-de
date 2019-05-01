# Übungsaufgabe 01

# Lösung 1

def kann_ich_ins_freibad_gehen(taschengeld, eintritt, freibad_geoeffnet=True):
    if taschengeld >= eintritt and freibad_geoeffnet is True:
        return True
    elif taschengeld < eintritt:
        return False
    else:
        return False

# Lösung 2

def kann_ich_ins_freibad_gehen(taschengeld, eintritt, freibad_geoeffnet=True):
    if taschengeld >= eintritt and freibad_geoeffnet is True:
        return True

    return False


# Wir haben weniger Taschengeld als der Eintritt kostet und das Freibad ist geöffnet
wenig_taschengeld = kann_ich_ins_freibad_gehen(1, 2)
print(wenig_taschengeld)

# Wir haben mehr Taschengeld als der Eintritt kostet und das Freibad ist geöffnet
viel_taschengeld = kann_ich_ins_freibad_gehen(10, 2)
print(viel_taschengeld)

# Wir haben mehr Taschengeld als der Eintritt kostet, aber das Freibad ist geschlossen
viel_taschengeld_freibad_zu = kann_ich_ins_freibad_gehen(10, 2, False)
print(viel_taschengeld_freibad_zu)