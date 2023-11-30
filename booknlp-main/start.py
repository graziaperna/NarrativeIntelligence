from booknlp.booknlp import BookNLP

model_params={
		"pipeline":"entity,event", 
		"model":"small"
	}
	
booknlp=BookNLP("en", model_params)

# Input file to process
input_file="booknlp-main\\booknlp\\data\english\\pride_and_prejudice.txt"

# Output directory to store resulting files in
output_directory="booknlp-main\\output_dir\\result"

# File within this directory will be named ${book_id}.entities, ${book_id}.tokens, etc.
book_id="result"

booknlp.process(input_file, output_directory, book_id)