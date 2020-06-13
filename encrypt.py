def rotate(text):
    for i in range(int(len(text)/2)):
        if i % 2 == 0:
            text[i] , text[len(text)-i-1] = text[len(text)-i-1] , text[i]
    return text

input_text = input('Enter the text to encrypt:')
text_to_encrypt = input_text.split(' ')
encrypted_text = []
for word in text_to_encrypt:
    encrypted_text.append(''.join(rotate(list(word))))
encrypted_text = ' '.join(rotate(encrypted_text))
print(encrypted_text)