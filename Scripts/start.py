from event import Event
from ner_spacy import spacyNer
from ner_IT5 import IT5Ner

def start():
        
    model_params={
            "model": "IT5", #accepted values are spacy, IT5 and MT5
            "entity": True, 
            "event": False, 
            "model_event": "small"
        }

    input_file= "data/input/10502_due_sposi_in_viaggio_brat.txt"
    output_file_entity = "data/output/output_entity.json"
    output_file_event = "data/output/output_event.json"

    if model_params["entity"] and model_params["event"]==False:
        
        if(model_params["model"] == "spacy"):
            entity = spacyNer()
            entity.processing_entity(input_file,output_file_entity)
        elif(model_params["model"] == "IT5"):
            entity = IT5Ner()
            entity.processing_entity(input_file,output_file_entity)

        print("Operation succeded.")
    
    elif model_params["event"] and model_params["entity"]==False:
        event = Event(model_params["model_event"])
        event.processing_event(input_file,output_file_event)
        print("Operation succeded.")
    
    elif model_params["entity"] and model_params["event"]:
        
        if(model_params["model"] == "spacy"):
            entity = spacyNer()
            entity.processing_entity(input_file,output_file_entity)
        elif(model_params["model"] == "IT5"):
            entity = IT5Ner()
            entity.processing_entity(input_file,output_file_entity)
        
        event = Event(model_params["model_event"])
        event.processing_event(input_file,output_file_event)
        print("Operation succeded.")

if __name__ == "__main__":
    start()
