logo = '''
 .d8888b.                                                    .d8888b.  d8b          888                       
d88P  Y88b                                                  d88P  Y88b Y8P          888                       
888    888                                                  888    888              888                       
888         8888b.   .d88b.  .d8888b   8888b.  888d888      888        888 88888b.  88888b.   .d88b.  888d888 
888            "88b d8P  Y8b 88K          "88b 888P"        888        888 888 "88b 888 "88b d8P  Y8b 888P"   
888    888 .d888888 88888888 "Y8888b. .d888888 888          888    888 888 888  888 888  888 88888888 888     
Y88b  d88P 888  888 Y8b.          X88 888  888 888          Y88b  d88P 888 888 d88P 888  888 Y8b.     888     
 "Y8888P"  "Y888888  "Y8888   88888P' "Y888888 888           "Y8888P"  888 88888P"  888  888  "Y8888  888     
                                                                           888                                
                                                                           888                                
                                                                           888                                

 '''


alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(logo)

play_again = True

while play_again:
    
    def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ""
        if encode_or_decode == "decode":
            shift_amount *= -1 # Multiply -1 reverses it from pos to neg (reverses if "decode")
        for letter in original_text:
            if letter not in alphabet:
                output_text += letter
            else:       
                shifted_index = alphabet.index(letter) + shift_amount
                shifted_index %= len(alphabet)
                output_text += alphabet[shifted_index]
        
            # shift_amount = abs(shift_amount)  # Added this to confirm shift_amount stays positive (to keep it from alternating +/- if decode)
        
        # Testing:  print(f"To test - printing the value of shift: {shift_amount}")
    
        print(f"Here is the {encode_or_decode}d result: {output_text}\n")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart = input(f"would you like to play again? (y/n)\n").lower()
        
    if restart == "n":
        play_again = False
        print("Game over.  Thanks for playing!")
    
# def encrypt(original_text, shift_amount):
# 	cipher_text = ""
# 	for letter in original_text:
# 		orig_index = alphabet.index(letter)
# 		shifted_index = orig_index + shift_amount
# 		shifted_index %= len(alphabet)  # applies mod 26 (length of alphabet) to limit shifted index to 26, or applies the remainder to wrap back around from the beginning
#             # example:  if orig_index = 25 'y', and shifted_index = 4, 29 % 25 = 4 'd'
# 		cipher_text += alphabet[shifted_index]
# 	print(f"Here is the encoded result: {cipher_text}")

# encrypt(original_text=text, shift_amount=shift)


# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         orig_index = alphabet.index(letter)
#         shifted_index = orig_index - shift_amount
#         shifted_index %= len(alphabet)
#         output_text += alphabet[shifted_index]
#     print(f"Here is the decoded result: {output_text}")

# decrypt(original_text=text, shift_amount=shift)



# decrypt(original_text=text, shift_amount=shift)


