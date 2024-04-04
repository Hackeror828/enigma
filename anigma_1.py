def shift_letters(letters, shift):
    shifted_list = []
    for letter in letters:
        if letter == ' ':
            # Keep spaces unchanged
            shifted_list.append(letter)
            continue
        # Convert letter to ASCII value
        ascii_value = ord(letter)
        # Apply the shift
        shifted_ascii = ascii_value + shift
        # Handle wraparound for lowercase letters
        if letter.islower():
            shifted_ascii = ((shifted_ascii - ord('a')) % 26) + ord('a')
        # Handle wraparound for uppercase letters
        elif letter.isupper():
            shifted_ascii = ((shifted_ascii - ord('A')) % 26) + ord('A')
        # Convert back to letter
        shifted_letter = chr(shifted_ascii)
        shifted_list.append(shifted_letter)
    return shifted_list

def convert_to_word(shifted_list):
    # Convert the list to a single word
    shifted_word = ''.join(shifted_list)
    return shifted_word

one = input("Enter a word: ")

lst = []
for letter in one:
    lst.append(letter)

shifts = []
for i in range(6):
    number = int(input(f"Enter shift {i+1} (0-26): "))
    while number < 0 or number > 26:
        print("Please enter a number between 0 and 26.")
        number = int(input(f"Enter shift {i+1} (0-26): "))
    shifts.append(number)

shifted_word = lst
for shift in shifts:
    shifted_word = shift_letters(shifted_word, shift)

print("Shifted Word:", convert_to_word(shifted_word))
# Inside anigma_1.py

def main():
    # Your main functionality here
    pass  # Placeholder for now
