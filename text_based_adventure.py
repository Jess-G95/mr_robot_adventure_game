'''
mr robot inspired adventure game (eXit)
'''

def play_again():
    answer = input("Do you want to play again? y/n: ").lower()

    if answer == 'y':
        start_game()
    else:
        print("Thanks for playing!")

def light_match():
    print("You light a match but it's still too dark to read the note. Do you continue or stay with your friend?")
    print("a. Continue through the tunnel")
    print("b. Stay with friend")
    answer = input("Choose 'a' or 'b': ").lower() 

    if answer == 'a':
        continue_through_tunnel()
    else:
        sit_next_to_friend()

def read_note_light():
    print("You read the note and is says 'Don't leave me here'. Do you go back to your friend or get on the boat?")
    print("a. Go back to your friend")
    print("b. Get on the boat")
    answer = input("Choose 'a' or 'b': ").lower() 

    if answer == 'a':
        stay_with_friend_end()
    else:
        rescue_boat_end()

def read_note_dark():
    print("You try to read the note but it's too dark. Do you light a match or conintue?")
    print("a. Continue through the tunnel")
    print("b. Light a match")
    answer = input("Choose 'a' or 'b': ").lower() 

    if answer == 'a':
        continue_through_tunnel()
    else:
        light_match()

def stay_with_friend_end():
    print("You decide to stay with your friend. You have just stopped a nuclear meltdown!")

    play_again()

def rescue_boat_end():
    print("You climb on board the rescue boat. You are free!")

    play_again()

def continue_through_tunnel():
    print("You continue through the tunnel. At the end of the tunnel is a beach where you see a rescue boat. It is light enough to read the note from your friend. Do you read the note or get on the rescue boat?")
    print("a. Read the note")
    print("b. Get on the rescue boat")
    answer = input("Choose 'a' or 'b': ").lower() 

    if answer == 'a':
        read_note_light()
    else:
        rescue_boat_end()

def enter_tunnel():
    print("You enter the tunnel. Your friend hands you a note. Do you try to read it or continue through the tunnel?")
    print("a. Continue through the tunnel")
    print("b. Read the note")
    answer = input("Choose 'a' or 'b': ").lower() 

    if answer == 'a':
        continue_through_tunnel()
    else:
        read_note_dark()

def move_barrel():
    print("You move the barrel and discover a tunnel behind it. Do you enter the tunnel?")
    print("a. Enter the tunnel")
    print("b. Stay with your friend")

    answer = input("Choose 'a' or 'b': ").lower() 

    if answer == 'a':
        enter_tunnel()
    else:
        stay_with_friend_end()

def read_note_dungeon():
    print("You read the note. It says 'Don't leave me here'. Do you stay with your friend or try to escape?")
    print("a. Stay with your friend")
    print("b. Try to escape")

    answer = input("Choose 'a' or 'b': ").lower()

    if answer == 'a':
        stay_with_friend_end()
    else:
        move_barrel()

def sit_next_to_friend():
    print("You sit next to your friend. They hand you a note. Do you read the note or try to escape?")
    print("a. Try to escape")
    print("b. Read the note")

    answer = input("Choose 'a' or 'b': ").lower()

    if answer == 'a':
        move_barrel()
    else:
        read_note_dungeon()

def start_game():
    print("You are trapped in a dungeon with a friend. You see a barrel. Do you move the barrel or sit next to your friend?")
    print("a. Move the barrel")
    print("b. Sit next to your friend")

    answer = input("Choose 'a' or 'b': ").lower()

    if answer == 'a':
        move_barrel()
    else:
        stay_with_friend_end()

start_game()