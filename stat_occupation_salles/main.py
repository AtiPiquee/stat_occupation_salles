"""
Module pour analyser et générer une page HTML sur l'occupation des salles.

Ce script utilise un module externe `module_stat_occupation_salles` pour extraire des données d'occupation à partir de fichiers ICS.
Ensuite, il génère un fichier HTML contenant un tableau des statistiques d'occupation.

Auteurs: PIHI Belvina
Date: 2025-01-07
"""

import module_stat_occupation_salles
from datetime import datetime

def process_file(file_paths):
    """
    Traite une liste de fichiers ICS et extrait les données d'occupation.

    Pour chaque fichier ICS, cette fonction calcule les heures d'occupation par salle,
    la moyenne hebdomadaire et journalière, ainsi que le taux d'occupation.

    :param file_paths: Liste des chemins vers les fichiers ICS.
    :type file_paths: list[str]
    :return: Liste de dictionnaires contenant les statistiques d'occupation par salle.
    :rtype: list[dict]
    """
    data = []
    for file_path in file_paths:
        try:
            # Appel au module externe pour calculer l'occupation des salles
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
    return data

def generate_html(data, output_file="occupation_salles.html"):
    """
    Génère une page HTML pour afficher les statistiques d'occupation des salles.

    :param data: Liste de dictionnaires contenant les données d'occupation par salle.
    :type data: list[dict]
    :param output_file: Chemin vers le fichier de sortie HTML.
    :type output_file: str
    """
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Occupation des salles</title>
    <link rel="stylesheet" href="html/css/style.css">
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
    # Écrire dans le fichier HTML
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"La page HTML a été générée avec succès : {output_file}")


if __name__ == "__main__":
    # Liste des fichiers ICS
    file_paths = ["data/BUT1.ics", "data/BUT2.ics", "data/BUT3.ics"]
    
    # Traiter les fichiers et extraire les données
    data = process_file(file_paths)
    
    # Générer la page HTML
    generate_html(data)
