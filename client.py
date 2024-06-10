import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "localhost"
PORT = 9090
client.connect((HOST, PORT))

# Receiving initial message from the server
msg_from_server = client.recv(1024).decode('utf-8')

user_name = input(msg_from_server)
client.send(user_name.encode('utf-8'))

# Receiving welcome message with the user's name
msg_from_server = client.recv(1024).decode('utf-8')
print(msg_from_server)  # "Hello There {user_name}"

# Receiving the rules of the game
game_rules = client.recv(1024).decode('utf-8')
print(game_rules)

acknowledgement_message = "Rules Fully Understood"
client.send(acknowledgement_message.encode("utf-8"))

# Receiving the prompt to enter the range
msg_from = client.recv(1024).decode('utf-8')

user_guess_range = input(msg_from)
client.send(user_guess_range.encode('utf-8'))

# Receiving the confirmation of the range
msg_from_server = client.recv(1024).decode('utf-8')
print(msg_from_server)  # "You'd Be Guessing Between 1 and {msg}"

# Starting the guessing game
for _ in range(10):
    guess = input("Your Guess: ")
    client.send(guess.encode('utf-8'))
    feedback = client.recv(1024).decode('utf-8')
    print(feedback)
    if "Correct" in feedback:
        break

client.close()
