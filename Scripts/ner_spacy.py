import spacy
import json
import os
from os.path import join
from pathlib import Path

class spacyNer:
    def __init__(self):

        self.model_path = "../models_spacy_pretrained/model-best"

    def processing_entity(self,input_file, output_file):
        nlp = spacy.load(self.model_path)
        
        with open(input_file, 'r', encoding='utf-8') as file:
            testo = file.read()
            
        doc = nlp(testo)
        
        risultati = []
        for token in doc:
            if token.ent_type != "" and token.ent_type != "MISC" :
                risultati.append({
                    "testo": token.text,
                    "entita": token.ent_type_
                })
            
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(risultati, json_file, ensure_ascii=False, indent=2)