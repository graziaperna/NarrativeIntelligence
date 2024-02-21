import spacy
import json
import os
from os.path import join
from pathlib import Path
from transformers import AutoModelForSequenceClassification, AutoTokenizer

dataset_path = os.path.join(os.getcwd(), "../modello_semantics/model_ner_small")

class Ner:
    def __init__(self,model):
        models={
            "big": "data/output/model-best",
            "medium":"it_core_news_md",
            "small": dataset_path
        }

        self.model_path = models[model]

    def processing_entity(self,input_file, output_file):
        #nlp = spacy.load(self.model_path)
        
        tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        model = AutoModelForSequenceClassification.from_pretrained(self.model_path)

        with open(input_file, 'r', encoding='utf-8') as file:
            testo = file.read()
            
        #doc = nlp(testo)
        doc = model(testo)
        
        risultati = []
        #for token in doc:
         #   if token.ent_type_ != "" and token.ent_type_ != "MISC" :
          #      risultati.append({
           #         "testo": token.text,
            #        "entita": token.ent_type_
             #   })
            
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(doc, json_file, ensure_ascii=False, indent=2)
