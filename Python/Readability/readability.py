def main():
    # Main text input
    text = input("Text: ")

    # Fucntion calls
    sentence = count_sentences(text)
    words = count_words(text)
    letters = count_letters(text)

    # Coleman-Liau index
    index = (0.0588 * (100 * float(letters) / float(words))) - (0.296 * (100 * float(sentence) / float(words))) - 15.8

    if index < 16 and index >= 0:
        print("Grade", round(index))
    elif index >= 16:
        print("Grade 16+")
    else:
        print("Before Grade 1")


# Counting number of sentences
def count_sentences(t):
    sent = 0
    for i in range(0, len(t)):
        if t[i] == '.' or t[i] == '!' or t[i] == '?':
            sent += 1
    return sent


# Counting number of words
def count_words(t):
    words = 1
    for i in range(0, len(t)):
        if t[i] == ' ':
            words += 1
    return words


# Counting number of letters
def count_letters(t):
    letters = 0
    for i in range(0, len(t)):
        if t[i].isupper() or t[i].islower():
            letters += 1
    return letters


main()