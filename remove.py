import json

def remove_quotes(text):
    # Rimuove le virgolette solo dal valore associato a "text"
    return text.replace('"', '')

def process_json_line(line):
    try:
        # Carica la riga come oggetto JSON
        json_data = json.loads(line)
        
        # Rimuovi le virgolette solo dal valore associato a "text"
        json_data['text'] = remove_quotes(json_data['text'])
        
        # Ritorna l'oggetto JSON elaborato
        return json.dumps(json_data)
    except json.JSONDecodeError:
        # Gestisci eventuali errori di decodifica
        print(f"Errore di decodifica JSON nella riga: {line}")
        return None

# Leggi il tuo file JSON Lines
with open("data/annotations.jsonl", 'r') as file:
    # Leggi tutte le linee
    lines = file.readlines()

# Processa ogni riga del file
processed_lines = [process_json_line(line) for line in lines]

# Rimuovi eventuali righe None dovute a errori di decodifica
processed_lines = [line for line in processed_lines if line is not None]

# Sovrascrivi il file con le linee elaborate
with open("data/annotations.jsonl", 'w') as file:
    # Scrivi tutte le linee elaborate
    file.writelines('\n'.join(processed_lines))
