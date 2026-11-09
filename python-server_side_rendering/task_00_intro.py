import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Invalid template input type.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Invalid attendees input type.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        content = template
        for ph in placeholders:
            val = attendee.get(ph)
            if val is None:
                val = "N/A"
            content = content.replace(f"{{{ph}}}", str(val))

        output_filename = f"output_{idx}.txt"
        with open(output_filename, 'w') as f:
            f.write(content)
