from booknlp.booknlp import BookNLP
import os
model_params={
		"pipeline":"entity,event", 
		"model":"small"
	}
	
booknlp=BookNLP("en", model_params)

print("Percorso",os.getcwd())
# Input file to process
input_file="data\english\\pride.short.txt"

# Output directory to store resulting files in
output_directory="output_dir\\result"

# File within this directory will be named ${book_id}.entities, ${book_id}.tokens, etc.
book_id="result"

booknlp.process(input_file, output_directory, book_id)