def encryptThis(message):
    words = message.split()  # Dividir a mensagem em palavras
    encrypted_words = []

    for word in words:
        if len(word) > 0:
            # Converter o primeiro caractere para seu código ASCII
            first_char_ascii = str(ord(word[0]))

            # Se a palavra tiver mais de um caractere, trocar o segundo com o último
            if len(word) > 1:
                second_char = word[1]
                last_char = word[-1]
                word = first_char_ascii + last_char + word[2:-1] + second_char
            else:
                word = first_char_ascii
            
            encrypted_words.append(word)

    # Reunir as palavras criptografadas em uma única string
    encrypted_message = ' '.join(encrypted_words)
    return encrypted_message
