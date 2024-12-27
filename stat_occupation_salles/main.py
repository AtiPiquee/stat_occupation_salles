

import module_stat_occupation_salles
from datetime import datetime

# Utilisation des fonctions du module pour extraire les données
file_paths = ["data/BUT1.ics", "data/BUT2.ics", "data/BUT3.ics"]
data = []

for file_path in file_paths:
    try:
        room_hours, total_hours = module_stat_occupation_salles.calculate_room_occupancy(file_path)
        for room, hours in room_hours.items():
            avg_per_week = hours / 52  # Moyenne par semaine
            avg_per_day = hours / 365  # Moyenne par jour
            occupancy_rate = (hours / total_hours) * 100 if total_hours > 0 else 0
            data.append({
                "Salle": room,
                "Heures": round(hours, 2),
                "Heures_semaine": round(avg_per_week, 2),
                "Heures_jour": round(avg_per_day, 2),
                "Taux_occupation": round(occupancy_rate, 2),
            })
    except Exception as e:
        print(f"Erreur lors du traitement du fichier {file_path}: {e}")

# Générer une page HTML
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Occupation des salles</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f4f4f4;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Occupation des salles</h1>
    <table>
        <thead>
            <tr>
                <th>Salle</th>
                <th>Heures d’utilisation</th>
                <th>Heures d’utilisation moyen/semaine</th>
                <th>Heures d’utilisation moyen/jour</th>
                <th>Taux d’occupation (%)</th>
            </tr>
        </thead>
        <tbody>
"""

for row in data:
    html_content += f"""            <tr>
                <td>{row['Salle']}</td>
                <td>{row['Heures']}</td>
                <td>{row['Heures_semaine']}</td>
                <td>{row['Heures_jour']}</td>
                <td>{row['Taux_occupation']}</td>
            </tr>
"""

html_content += """        </tbody>
    </table>
</body>
</html>
"""

# Écrire le HTML dans un fichier
with open("occupation_salles.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("La page HTML a été générée avec succès : occupation_salles.html")
