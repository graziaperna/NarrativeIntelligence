from event import Event
from ner_spacy import Ner

def start():
        
    model_params={
            "entity": True, 
            "event": False, 
            "model_entity": "medium",
            "model_event": "small"
        }

    input_file= "data/input/10502_due_sposi_in_viaggio_brat.txt"
    output_file_entity = "data/output/output_entity.json"
    output_file_event = "data/output/output_event.json"

    if model_params["entity"] and model_params["event"]==False:
        entity = Ner(model_params["model_entity"])
        entity.processing_entity(input_file,output_file_entity)
    elif model_params["event"] and model_params["entity"]==False:
        event = Event(model_params["model_event"])
        event.processing_event(input_file,output_file_event)
    elif model_params["entity"] and model_params["event"]:
        entity = Ner(model_params["model_entity"])
        entity.processing_entity(input_file,output_file_entity)
        event = Event(model_params["model_event"])
        event.processing_event(input_file,output_file_event)

if __name__ == "__main__":
    start()
