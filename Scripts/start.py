import spacy
import json
import os

def Ner(input_file, output_file):
    nlp = spacy.load("it_core_news_sm")
    
    with open(input_file, 'r', encoding='utf-8') as file:
        testo = file.read()
        
    doc = nlp(testo)
    
    risultati = []
    for token in doc:
        if token.ent_type_ != "" and token.ent_type_ != "MISC" :
            risultati.append({
                "testo": token.text,
                "entita": token.ent_type_
            })
        
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(risultati, json_file, ensure_ascii=False, indent=2)

def Event(input_file, output_file):
    nlp = spacy.load("Small_Model_Efficiency\output\model-best")
    
    with open(input_file, 'r', encoding='utf-8') as file:
        testo = file.read()

    doc = nlp(testo)
    risultati=[]
    for token in doc:
        if token.ent_type_ == "EVENT":
                risultati.append({
                    "testo": token.text,
                    "entita": token.ent_type_
                })
        
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(risultati, json_file, ensure_ascii=False, indent=2)

print(os.getcwd())

input_file_path = "data/input/10502_due_sposi_in_viaggio_brat.txt"
output_file_path = "data/output/output.json"
output_file_path1 = "data/output/output_event.json"

Ner(input_file_path, output_file_path)
Event(input_file_path,output_file_path1)
