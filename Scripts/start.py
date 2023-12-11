import spacy
import json
import os

def Ner(input_file, output_file):
    nlp = spacy.load("it_core_news_sm")
    
    # Leggi il testo dal file
    with open(input_file, 'r', encoding='utf-8') as file:
        testo = file.read()
        
    doc = nlp(testo)
    
    # Prepara i risultati per il salvataggio in JSON
    risultati = []
    for token in doc:
        if token.ent_type_ != "":
            risultati.append({
                "testo": token.text,
                "entita": token.ent_type_
            })
        
    # Salva i risultati in un file JSON
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(risultati, json_file, ensure_ascii=False, indent=2)

print(os.getcwd())

# Specifica i percorsi del file di input e del file di output JSON
input_file_path = "data/input/10502_due_sposi_in_viaggio_brat.txt"
output_file_path = "data/output/output.json"

# Esegui la funzione con i percorsi specificati
Ner(input_file_path, output_file_path)
