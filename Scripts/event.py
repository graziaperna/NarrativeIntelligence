import spacy
import json
import os
from os.path import join
from pathlib import Path
from pyxtension.streams import stream

class Event:
    def Event(self, input_file, output_file, model): 
        models={
            "big": "models_event\Large_Model_Efficiency\output\model-best",
            "small": "models_event\Small_Model_Efficiency\output\model-best"
        }
        model_path = stream(models.keys()).filter(lambda key : key==model).flatMap(lambda key : model_path==models[key])
        #for key in models.keys() :
        #    if model==key:
        #        model_path = models[key]
        home = str(Path.home())
        model_path=os.path.join(home, model_path)
        nlp = spacy.load(model_path)

        with open(input_file, 'r', encoding='utf-8') as file:
            testo = file.read()

        doc = nlp(testo)
        risultati=[]
        for token in doc:
            if token.ent_type_ == "Event":
                    risultati.append({
                        "testo": token.text,
                        "entita": token.ent_type_
                    })
            
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(risultati, json_file, ensure_ascii=False, indent=2)


