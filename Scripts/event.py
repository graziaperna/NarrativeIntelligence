import spacy
import json
import os
from os.path import join
from pathlib import Path

class Event:
    def __init__(self,model): 
        models={
            "big": "models_event\Large_Model_Efficiency\output\model-best",
            "small": "models_event\Small_Model_Efficiency\output\model-best"
        }
        self.model_path = models[model]
        
    def processing_event(self,input_file, output_file):
        home = str(Path.home())
        self.model_path=os.path.join(home, self.model_path)
        nlp = spacy.load(self.model_path)

        with open(input_file, 'r', encoding='utf-8') as file:
            testo = file.read()

        doc = nlp(testo)
        risultati=[]
        for token in doc:
            if token.ent_type_ == "Event":
                    risultati.append({
                        "testo": token.text,
                        "evento": token.ent_type_
                    })
            
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(risultati, json_file, ensure_ascii=False, indent=2)