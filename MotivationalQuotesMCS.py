import os
import random
import time

def main():
    quote_folder = "Quote Folder"
    quote_path = os.path.join(quote_folder, 'quote.txt')
    response_path = os.path.join(quote_folder, 'response.txt')

    try:
        os.mkdir(quote_folder)
    except FileExistsError:
        pass

    quote_list = ["Don't dream of winning, train for it!",
                  "Keep trying! Rome wasn't built in a day!",
                  "If things get tough, take a break, you earned it!",
                  "You're doing a great job! Keep this up and you'll reach your dreams",
                  "A fancy sports car is earned through hard work. You got this!"]

    print("Motivational Quote Microservice is running...")

    while True:
        try:
            with open(quote_path, 'r', encoding="utf-8") as file:
                request = file.read().strip()
        except FileNotFoundError:
            request = ""

        if request:
            print(f"Request received: {request}")

            if request.lower() == "random":
                 response = random.choice(quote_list)

            elif request.lower() == "all":
                response = "\n".join(quote_list)

            elif request.lower().startswith("add "):
                add_quote = request[4:].strip()
                if add_quote:
                    quote_list.append(add_quote)
                    response = 'Quote has been added successfully!'
                else:
                    response = "Error! No quote was provided!"
            else:
                response = "Invalid Command"

            with open(response_path, 'w', encoding="utf-8") as file:
                file.write(response)

            print(f"Response was written: {response}\n")

            with open(quote_path, 'w', encoding="utf-8") as file:
                file.write("")
        time.sleep(1)

if __name__ == "__main__":
    main()
