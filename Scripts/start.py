from event import Event

def start():
        
    model_params={
            "entity": False, 
            "event": True, 
            "model_entity": "small",
            "model_event": "small"
        }

    input_file= "data/input/10502_due_sposi_in_viaggio_brat.txt"
    output_file_entity = "data/output/output.json"
    output_file_event = "data/output/output_event.json"

    if model_params["entity"] :
        #Ner(input_file, output_file_entity, model_params["model_entity"])
         print("ciao")
    else :
        event = Event(input_file,output_file_event, model_params["model_event"])

if __name__ == "__main__":
	start()
