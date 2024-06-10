


import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "localhost"
PORT = 9090
server.bind((HOST, PORT))
server.listen(5)

while True:
    connection, address = server.accept()
    print(f"Connection Established With {address}")

    # Send initial greeting
    connection.send("Hello, What Would You Like To Be Called? ".encode("utf-8"))
    user_name = connection.recv(1024).decode("utf-8")

    # Send greeting with user name
    connection.send(f"Hello There {user_name}".encode("utf-8"))

   

    game_rules = f"Rules:\n 1 Enter The Range You Want To Guess\n 2 You Have 10 Tries to guess correctly\nGood Luck {user_name}"

    connection.sendall(game_rules.encode("utf-8"))


    message_from_client = connection.recv(1024).decode("utf-8")
    print(message_from_client)

    # Prompt for guessing range
    msg = "Enter The Range You Want To Guess: "
    connection.send(msg.encode("utf-8"))
    msg = connection.recv(1024).decode("utf-8")
    msg = int(msg)
    msg_to_client = f"You'd Be Guessing Between 1 and {msg}"
    connection.send(msg_to_client.encode("utf-8"))

    random_number = random.randint(1, msg)

    for attempt in range(10):
        guess = int(connection.recv(1024).decode("utf-8"))
        if guess < random_number:
            connection.send(f"Too Low, Try Again {9 - attempt} tries left ".encode("utf-8"))
        elif guess > random_number:
            connection.send(f"Too High. Try again {9 - attempt} tries left".encode("utf-8"))
        else:
            win_message =  f"Correct! Well Done {user_name} You Guessed Correctly In {attempt} tries"
            connection.send(win_message.encode("utf-8"))
            break
    else:
        connection.send(f"Out Of Attempts! The random_number was {random_number}".encode("utf-8"))

    connection.close()