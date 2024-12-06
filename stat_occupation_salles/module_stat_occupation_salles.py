from datetime import datetime

def extract_ics_data_and_calculate_hours(file_path):
    total_hours = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        if line.startswith("DTSTART:"):
            start_time = line.replace("DTSTART:", "").strip()
        elif line.startswith("DTEND:"):
            end_time = line.replace("DTEND:", "").strip()
            # Convertir les dates et heures en objets datetime
            start_dt = datetime.strptime(start_time, "%Y%m%dT%H%M%SZ")
            end_dt = datetime.strptime(end_time, "%Y%m%dT%H%M%SZ")
            # Calculer la durée en heures
            duration = (end_dt - start_dt).total_seconds() / 3600
            total_hours += duration
    
    return total_hours

# Chemins vers les fichiers
file_paths = ["data/BUT1.ics", "data/BUT2.ics", "data/BUT3.ics"]

# Calcul total des heures
total_hours_all_files = 0
for file_path in file_paths:
    try:
        total_hours = extract_ics_data_and_calculate_hours(file_path)
        print(f"Total d'heures pour {file_path}: {total_hours:.2f} heures")
        total_hours_all_files += total_hours
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
    except Exception as e:
        print(f"Erreur lors du traitement de {file_path}: {e}")

print(f"Total général d'heures d'utilisation : {total_hours_all_files:.2f} heures")

