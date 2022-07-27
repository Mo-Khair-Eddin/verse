verse = input("Your verse: ")
verse = verse.lower()
number_of_As = input('In your verse, you\'d like to know the count of the letter/word:\n')

small_letter_count = (verse.count(number_of_As.lower()))
big_letter_count = (verse.count(number_of_As.upper()))
num = small_letter_count + big_letter_count
length_of_verse = len(verse)
no_input = ""
number_of_As_len = len(number_of_As)

if number_of_As_len == 1:
    number_of_As = number_of_As.upper()
elif number_of_As_len > 1:
    number_of_As = number_of_As.capitalize()

for no_input in number_of_As:

    if num == 1:
        print('There is {} "'.format(num) + number_of_As + '" in the verse.')
    elif num > 1:
        print('There are {} "'.format(num) + number_of_As + '"s in the verse.')
    elif num == 0:
        print('There are no "' + number_of_As + '"s in the verse.')
    break
if length_of_verse == 1:
    print("Length: your verse is {} character long".format(length_of_verse))
elif length_of_verse > 1:
    print("Length: your verse is {} characters long".format(length_of_verse))
elif length_of_verse == 0:
    print("You've input nothing.")