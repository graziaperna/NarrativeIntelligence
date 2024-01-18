import spacy
import json

class Ner:
    def Ner(input_file, output_file,model):
        models={
            "big": "it_core_news_lg",
            "medium":"it_core_news_md",
            "small": "it_core_news_sm"
        }

        for key in models.keys() :
            if model==key:
                model_path = models[key]

        nlp = spacy.load(model_path)
        
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
