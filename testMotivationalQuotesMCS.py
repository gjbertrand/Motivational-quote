import os.path
import time


def main():
    quote_folder = "Quote Folder"
    quote_path = os.path.join(quote_folder, 'quote.txt')
    response_path = os.path.join(quote_folder, 'response.txt')

    try:
        os.mkdir(quote_folder)
    except FileExistsError:
        pass

    print("=== Motivational Quote Microservice Test===")
    print("Type these in to test:")
    print("'random' to get a random quote")
    print("'all' to view all quotes")
    print("'add [quote] to add a new quote")
    print("'exit' to close the testing program")

    while True:
        request = input("Enter command: \n").strip()

        if request.lower() == 'exit':
            print("Thanks for using the tester! Closing now!")
            break

        with open(quote_path, 'w', encoding="utf-8") as file:
            file.write(request)

        print("Request has been sent. Awaiting response...\n")
        time.sleep(1)

        try:
            with open(response_path, 'r', encoding="utf-8") as file:
                response = file.read().strip()
                if response:
                    print("Response has been received:")
                    print(response)
                else:
                    print("No response as of yet")
        except FileNotFoundError:
            print("Response file does not exist")

        time.sleep(1)

if __name__ =="__main__":
    main()