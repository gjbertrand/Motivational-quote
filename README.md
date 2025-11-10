# Motivational-quote
A microservice that generates motivational quotes

# Communication Contract
All communication happens via two text files in the Quote Folder directory:
-	Request file: Quote Folder/quote.txt
-	Response file: Quote Folder/response.txt
Both files are plain UTF-8 text.

Valid Commands (Requests)
Write exactly one of these commands into quote.txt:
1.	random
-	Returns a single random motivational quote.
2.	all
-	Returns all currently known quotes, separated by newline characters.
3.	add <your quote text>
-	Example:
add What we do in life echoes in eternity.
-	If the quote text after add is non-empty:
	The quote is appended to the in-memory quote_list.
	Response: Quote has been added successfully!
-	If the quote text is empty:
	Response: Error! No quote was provided!
4.	Any other text:
	Response: Invalid Command

After handling any request, the microservice(Response):
-	Writes the response to response.txt.
-	Clears quote.txt (sets it to an empty string).

# Programmatic Request Example
- import os
- quote_folder = "Quote Folder"
- quote_path = os.path.join(quote_folder, 'quote.txt')

# 1. Ensure the directory exists
- os.makedirs(quote_folder)

# 2. Write the request command to the quote file
- request_command = "random" # For example, request a random quote
- with open(quote_path, 'w', encoding="utf-8") as file:
  - file.write(request_command)
- print(f"Request sent. Awaiting for response...")

