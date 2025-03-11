import json
from tqdm import tqdm
import os
from os.path import join
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from torch import torch
from transformers import pipeline


class IT5Ner:
    
    def __init__(self):

        self.model_path = "../modello_semantics_it5/model_ner_small"

    def processing_entity(self,input_file, output_file):
        
        with open(input_file, 'r', encoding='utf-8') as file:
            testo = file.read()
            print(testo)


        # e.g. to load IT5 Small trained on formal-to-informal style 
        # transfer, use `it5/it5-small-formal-to-informal`
        f2i = pipeline("text-classi", model= self.model_path)
        results = f2i("la penna sul tavolo")

        print(results)

            
        # tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        # model = AutoModelForSeq2SeqLM.from_pretrained(self.model_path)

        # input_ids = tokenizer(testo, return_tensors="pt").input_ids
        # outputs = model.generate(input_ids)
        # for output in outputs:
        #     print(tokenizer.decode(output, skip_special_tokens=True))
        # for token in doc:
        #     if token.ent_type != "" and token.ent_type != "MISC" :
        #         risultati.append({
        #             "testo": token.text,
        #             "entita": token.ent_type_
        #         })
            
        # with open(output_file, 'w', encoding='utf-8') as json_file:
        #      json.dump(outputs, json_file, ensure_ascii=False, indent=2)