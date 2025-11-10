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

1. Ensure the directory exists
  - os.makedirs(quote_folder)

 2. Write the request command to the quote file
  - request_command = "random" # For example, request a random quote
  - with open(quote_path, 'w', encoding="utf-8") as file:
  - file.write(request_command)
  - print(f"Request sent. Awaiting for response...")

# Programmatic Receive Example
- import os
- import time
- quote_folder = "Quote Folder"
 -response_path = os.path.join(quote_folder, 'response.txt')

1. Wait for a short time to allow the microservice to process the request
time.sleep(1) 

2. Read the response from the response file
- try:
    - with open(response_path, 'r', encoding="utf-8") as file:
    - response_data = file.read()
    
 3. Clear the response file after reading 
    - with open(response_path, 'w', encoding="utf-8") as file:
    - file.write("")

 4.  Response was written
     - with open(response_path, 'w', encoding="utf-8") as file:
     - file.write(response)
- print(f"Response was written :\n--- RESPONSE ---\n{response_data}\n----------------")

- except FileNotFoundError:
    print("Error: Response file does not exist.")

 # ULM Sequence Diagram
<img width="1002" height="1675" alt="Inspirational Quote UML-Final Version" src="https://github.com/user-attachments/assets/1bc72cb9-4dc1-4093-b907-c2526f9720e2" />


