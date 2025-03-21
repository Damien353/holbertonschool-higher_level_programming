import os

def generate_invitations(template, attendees):
    # Vérification des types d'entrée
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Gestion des entrées vides
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Traitement des données et écriture des fichiers
    for idx, attendee in enumerate(attendees, start=1):
        invitation_content = template
        # Remplacement des placeholders
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A") or "N/A"
            invitation_content = invitation_content.replace(f"{{{key}}}", value)

        # Écriture dans un fichier
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation_content)
            print(f"Generated {output_filename}")
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
