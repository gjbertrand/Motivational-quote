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

# REQUESTING A QUOTE FROM THE MICROSERVICE
The requesting program must write a command into the file named quote.txt.
This file is located inside a folder named:
Quote Folder
The string written to quote.txt must not include newline characters.
The requesting program writes one of the following commands:
________________________________________
# Valid Commands
Command	Behavior
1. random	
2. all	
3. add Your new quote here	Adds a new quote to the internal list.

________________________________________
# How to Make a Request
1.	Open quote.txt with UTF-8 encoding.
2.	Write one of the supported commands.
3.	Close the file to allow the microservice to process the request.
The Quote Folder directory and both text files will be created automatically by the microservice if they do not already exist.
Any existing text in quote.txt is overwritten at startup by the microservice.
# EXAMPLE REQUEST WITH PYTHON
# Recommended imports
import os  # required unless the file path is hardcoded

# get file path to quote.txt
folder_path = os.path.join(os.getcwd(), "Quote Folder")
file_path = os.path.join(folder_path, "quote.txt")

# command to write (example: get a random quote)
command = "random"

# “call” to the Microservice (write the command to quote.txt)
with open(file_path, "w", encoding="utf-8") as file:
    file.write(command)
________________________________________

# RECEIVING THE RESPONSE FROM THE MICROSERVICE
The requesting program should wait at least 1 second after writing the request before reading the response.
The microservice writes its response into:
Quote Folder/response.txt
After processing the request, the microservice:
•	Writes the response to response.txt
•	Clears quote.txt (sets it to an empty string)

# EXAMPLE  RECEIVE CALL WITH PYTHON
# imports required for this microservice call
import time
import os  # required unless path is hardcoded

# wait at least 1 second
time.sleep(1)

# get file path to response.txt
folder_path = os.path.join(os.getcwd(), "Quote Folder")
file_path = os.path.join(folder_path, "response.txt")

# variable to save the response
response = ""

# receive response from Microservice (read from response.txt)
with open(file_path, "r", encoding="utf-8") as file:
    response = file.read()

print(response)
________________________________________
# REAL WORLD EXAMPLE CALL AND RETURN VALUE
Suppose a user wants to request all quotes from the microservice.
They would use the following code to:
1.	Make the request
2.	Wait for the microservice to process it
3.	Read the response
Example Code:
import os
import time

# get file paths
folder_path = os.path.join(os.getcwd(), "Quote Folder")
request_path = os.path.join(folder_path, "quote.txt")
response_path = os.path.join(folder_path, "response.txt")

# command to write
command = "all"

# Write command to microservice (Request)
with open(request_path, "w", encoding="utf-8") as file:
    file.write(command)

# wait for the microservice to process
time.sleep(1)

# Read the response
with open(response_path, "r", encoding="utf-8") as file:
    quotes = file.read()

print(quotes)
________________________________________
# Example Call Made (quote.txt contents):

<img width="602" height="294" alt="image" src="https://github.com/user-attachments/assets/c340977a-bced-40e0-b376-df4304b2f8e7" />

 
# Example Response Written to response.txt:
<img width="975" height="326" alt="image" src="https://github.com/user-attachments/assets/7caee13a-0134-4a74-9d13-9a719ccaf96f" />

 

# Example Console Output:

<img width="950" height="270" alt="image" src="https://github.com/user-attachments/assets/c592d8b5-5ed7-41c4-98ef-70481dc919e7" />





 # ULM Sequence Diagram
<img width="1002" height="1646" alt="Inspirational Quote UML-Final Version-Revised" src="https://github.com/user-attachments/assets/1817b14f-2a3c-45ed-883e-786cb51277ae" />



