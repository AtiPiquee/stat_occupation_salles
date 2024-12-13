#!/bin/python3

import re
from datetime import datetime
import path

def read_ics_file(file):
    """Lit le fichier ICS et extrait les blocs VEVENT."""
    print(file)
    with open(file, 'r', encoding='utf-8') as file:
        data = file.read()
    events = re.findall(r"BEGIN:VEVENT(.*?)END:VEVENT", data, re.DOTALL)
    return events

def parse_event(event):
    """Extrait les informations pertinentes d'un événement."""
    def extract_field(field_name, event_block):
        pattern = rf"{field_name}:(.*)"
        match = re.search(pattern, event_block)
        return match.group(1).strip() if match else None

    start_time = extract_field("DTSTART", event)
    end_time = extract_field("DTEND", event)
    location = extract_field("LOCATION", event)
    return {
        "start_time": datetime.strptime(start_time, "%Y%m%dT%H%M%SZ"),
        "end_time": datetime.strptime(end_time, "%Y%m%dT%H%M%SZ"),
        "location": location or "Unknown"
    }
def calculate_total_hours(events):
    """Calcule le total d'heures d'occupation par salle."""
    hours_per_room = {}
    for event in events:
        location = event['location']
        duration = (event['end_time'] - event['start_time']).total_seconds() / 3600
        if location not in hours_per_room:
            hours_per_room[location] = 0
        hours_per_room[location] += duration
    return hours_per_room

def calculate_average_hours(hours_per_room, weeks=52, days_per_week=5):
    """Calcule les moyennes hebdomadaires et journalières."""
    averages = {}
    for room, total_hours in hours_per_room.items():
        weekly_avg = total_hours / weeks
        daily_avg = total_hours / (weeks * days_per_week)
        averages[room] = {
            "weekly_avg": weekly_avg,
            "daily_avg": daily_avg
        }
    return averages
def calculate_occupancy_rate(hours_per_room):
    """Calcule le taux d'occupation par rapport à l'occupation totale."""
    total_hours = sum(hours_per_room.values())
    occupancy_rate = {
        room: (hours / total_hours) * 100
        for room, hours in hours_per_room.items()
    }
    return occupancy_rate

def main():
    file_path = "../data/"
    files = path.elements(file_path)
    
    for i in range(len(files)):
        file = str(path) + files[i]
        print(file)
        events_raw = read_ics_file(file)
        events = [parse_event(event) for event in events_raw]

        # Calculs
        total_hours = calculate_total_hours(events)
        averages = calculate_average_hours(total_hours)
        occupancy_rate = calculate_occupancy_rate(total_hours)

        # Résultats
        print("Nombre total d'heures par salle:")
        for room, hours in total_hours.items():
            print(f"{room}: {hours:.2f} heures")

        print("\nMoyenne hebdomadaire et journalière:")
        for room, stats in averages.items():
            print(f"{room} - Hebdo: {stats['weekly_avg']:.2f}h, Journée: {stats['daily_avg']:.2f}h")

        print("\nTaux d'occupation:")
        for room, rate in occupancy_rate.items():
            print(f"{room}: {rate:.2f}%")

# Exécution
if __name__ == "__main__":
    main()


