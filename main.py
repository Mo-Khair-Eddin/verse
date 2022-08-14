def get_user_input():
    print("Verse: ")
    user_input = []
    while True:
        line = input()
        if line == "end()":
            break
        else:
            user_input.append(line)
    return '\n'.join(user_input)


def format_output(user_request):
    if number_of_As_len == 1:
        user_request = user_request.upper()
    elif number_of_As_len > 1:
        user_request = user_request.capitalize()
    for no_input in user_request:
        if num == 1:
            print('There is {} "'.format(num) + user_request + '" in the verse.')
        elif num > 1:
            print('There are {} "'.format(num) + user_request + '"s in the verse.')
        elif num == 0:
            print('In the verse, there are no matching characters/words with your enquiry.')
        break
    if length_of_verse == 1:
        print("Length: your verse is {} character long".format(length_of_verse))
    elif length_of_verse > 1:
        print("Length: your verse is {} characters long".format(length_of_verse))
    elif length_of_verse == 0:
        print("You've input nothing.")



verse = get_user_input()
#the_verse = input().splitlines()
#verse = ''.join(input().splitlines())
#verse = sys.stdin.read()
number_of_As = input('In your verse, you\'d like to know the count of the letter/word:\n')
#verse_file = open("Big Verse.txt", 'w+')

#verse_file = verse_file.write(verse)
#verse_file.close("Big Verse.txt")
#verse_file = open("Big Verse.txt", 'r')
#print(verse_file.read())

#small_letter_count = (verse.count(number_of_As.lower()))
#big_letter_count = (verse.count(number_of_As.upper()))
#num = small_letter_count + big_letter_count
num = verse.lower().count(number_of_As.lower())
length_of_verse = len(verse)
num_of_words = verse.split()
length_of_words = len(num_of_words)
no_input = ""
number_of_As_len = len(number_of_As)

format_output(number_of_As)

print(length_of_words)
