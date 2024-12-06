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



def calculate_hours_per_week(file_path):
    events = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        if line.startswith("DTSTART:"):
            start_time = line.replace("DTSTART:", "").strip()
        elif line.startswith("DTEND:"):
            end_time = line.replace("DTEND:", "").strip()
            # Convertir en objets datetime
            start_dt = datetime.strptime(start_time, "%Y%m%dT%H%M%SZ")
            end_dt = datetime.strptime(end_time, "%Y%m%dT%H%M%SZ")
            events.append((start_dt, end_dt))
    
    # Calculer la durée totale en heures et les semaines couvertes
    total_hours = 0
    weeks = set()
    for start, end in events:
        duration = (end - start).total_seconds() / 3600
        total_hours += duration
        weeks.add(start.strftime("%Y-W%U"))  # Ajouter la semaine au format "Année-Semaine"
    
    # Calculer les heures moyennes par semaine
    total_weeks = len(weeks)
    average_hours_per_week = total_hours / total_weeks if total_weeks > 0 else 0

    return total_hours, total_weeks, average_hours_per_week

# Chemins vers les fichiers
file_paths = ["data/BUT1.ics", "data/BUT2.ics", "data/BUT3.ics"]

# Calcul pour tous les fichiers
total_hours_all_files = 0
total_weeks_all_files = set()
for file_path in file_paths:
    try:
        total_hours, total_weeks, avg_hours = calculate_hours_per_week(file_path)
        print(f"Fichier : {file_path}")
        print(f"  Total heures : {total_hours:.2f}")
        print(f"  Total semaines : {total_weeks}")
        print(f"  Moyenne par semaine : {avg_hours:.2f} heures")
        total_hours_all_files += total_hours
        total_weeks_all_files.update([week for week in range(total_weeks)])  # Ajouter les semaines uniques
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
    except Exception as e:
        print(f"Erreur lors du traitement de {file_path}: {e}")

# Moyenne générale
total_weeks_unique = len(total_weeks_all_files)
average_hours_all_files = total_hours_all_files / total_weeks_unique if total_weeks_unique > 0 else 0
print(f"\nMoyenne générale d'heures par semaine : {average_hours_all_files:.2f} heures")

from datetime import datetime

def calculate_hours_per_day(file_path):
    events = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        if line.startswith("DTSTART:"):
            start_time = line.replace("DTSTART:", "").strip()
        elif line.startswith("DTEND:"):
            end_time = line.replace("DTEND:", "").strip()
            # Convertir en objets datetime
            start_dt = datetime.strptime(start_time, "%Y%m%dT%H%M%SZ")
            end_dt = datetime.strptime(end_time, "%Y%m%dT%H%M%SZ")
            events.append((start_dt, end_dt))
    
    # Calculer la durée totale en heures et les jours couverts
    total_hours = 0
    days = set()
    for start, end in events:
        duration = (end - start).total_seconds() / 3600
        total_hours += duration
        days.add(start.strftime("%Y-%m-%d"))  # Ajouter la date au format "AAAA-MM-JJ"
    
    # Calculer les heures moyennes par jour
    total_days = len(days)
    average_hours_per_day = total_hours / total_days if total_days > 0 else 0

    return total_hours, total_days, average_hours_per_day

# Chemins vers les fichiers
file_paths = ["data/BUT1.ics", "data/BUT2.ics", "data/BUT3.ics"]

# Calcul pour tous les fichiers
total_hours_all_files = 0
total_days_all_files = set()
for file_path in file_paths:
    try:
        total_hours, total_days, avg_hours = calculate_hours_per_day(file_path)
        print(f"Fichier : {file_path}")
        print(f"  Total heures : {total_hours:.2f}")
        print(f"  Total jours : {total_days}")
        print(f"  Moyenne par jour : {avg_hours:.2f} heures")
        total_hours_all_files += total_hours
        total_days_all_files.update([day for day in range(total_days)])  # Ajouter les jours uniques
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
    except Exception as e:
        print(f"Erreur lors du traitement de {file_path}: {e}")

# Moyenne générale
total_days_unique = len(total_days_all_files)
average_hours_all_files = total_hours_all_files / total_days_unique if total_days_unique > 0 else 0
print(f"\nMoyenne générale d'heures par jour : {average_hours_all_files:.2f} heures")
from datetime import datetime
from collections import defaultdict

def calculate_room_occupancy(file_path):
    room_hours = defaultdict(float)  # Stocke les heures totales par salle
    total_hours = 0  # Total des heures pour toutes les salles

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("DTSTART:"):
            start_time = line.replace("DTSTART:", "").strip()
        elif line.startswith("DTEND:"):
            end_time = line.replace("DTEND:", "").strip()
        elif line.startswith("LOCATION:"):
            room = line.replace("LOCATION:", "").strip()
            # Convertir les dates en objets datetime
            start_dt = datetime.strptime(start_time, "%Y%m%dT%H%M%SZ")
            end_dt = datetime.strptime(end_time, "%Y%m%dT%H%M%SZ")
            # Calculer la durée en heures
            duration = (end_dt - start_dt).total_seconds() / 3600
            room_hours[room] += duration
            total_hours += duration

    return room_hours, total_hours

# Chemins vers les fichiers
file_paths = ["data/BUT1.ics", "data/BUT2.ics", "data/BUT3.ics"]

# Calculer les heures d'occupation
total_department_hours = 0
all_room_hours = defaultdict(float)

for file_path in file_paths:
    try:
        room_hours, file_total_hours = calculate_room_occupancy(file_path)
        for room, hours in room_hours.items():
            all_room_hours[room] += hours
        total_department_hours += file_total_hours
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
    except Exception as e:
        print(f"Erreur lors du traitement de {file_path}: {e}")

# Calculer et afficher les taux d'occupation
print("\nTaux d'occupation des salles :")
for room, hours in all_room_hours.items():
    occupancy_rate = (hours / total_department_hours) * 100 if total_department_hours > 0 else 0
    print(f"Salle {room} : {occupancy_rate:.2f}%")

print(f"\nTotal des heures pour le département : {total_department_hours:.2f} heures")
