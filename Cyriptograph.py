import os

ascii_symbols = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "", "{", "|", "}", "~", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]

print("Welcome to Cryptograph, You might encrypt and decyrpt texts here \n by \"The Caesar Cipher\" algorithm.")
ask=''
while ask!='n' and ask!='N':
 operation=input("What do we do (encrypt/decrypt): ")
 os.system('cls' if os.name=='nt' else 'clear')
 if operation not in ["encrypt","enc","1","decrypt","dec","2"]:
 			ask=input("You've chosen wrong operation type.\nUse only 'enc' or 'encrypt' or '1' for encrypting, \n'dec' or 'decrypt' or '2' for decrypting. \n And try again! \n\nWould you like to work again? (y/n):  ")
 			os.system('cls' if os.name=='nt' else 'clear')
 			continue
 key=input("Ok, Enter a key word now: ")
 key_length_opposite=int("-"+str(len(key)-1))
 arrow_key_symbol_index=(len(key)-1)+key_length_opposite
 encrypted_text=""
 decrypted_text=""
 key_symbol=key[arrow_key_symbol_index]
 if key_symbol in ascii_symbols:
 	 key_symbol_index=ascii_symbols.index(key_symbol)
 else:
 	 ask=input(f"The key symbol \"{key_symbol}\" not found in ASSCI symbol list, Please try again using another symbols.\n Would you like to work again? (y/n): ")
 	 continue
 text=input("Amazing!, Enter text now: ")	 
 for symbol in text:
 	if arrow_key_symbol_index ==	(len(key)-1):
 		key_length_opposite=int("-"+str(len(key)-1))
 		arrow_key_symbol_index=(len(key)-1)+key_length_opposite
 	if symbol in ascii_symbols:
 	 symbol_index=ascii_symbols.index(symbol)
 	 if operation ==	"encrypt" or operation ==	"enc" or operation ==	"1":
 		 go_on = symbol_index+key_symbol_index
 		 if go_on  > len(ascii_symbols):
 			 go_on = go_on - (len(ascii_symbols)-1) 
 		 encrypted_text+=ascii_symbols[go_on]
 	 elif operation ==	"decrypt" or operation ==	"dec" or operation ==	"2":
 	  go_back = symbol_index-(key_symbol_index+1)
 	  encrypted_text+=ascii_symbols[go_back]
 	 key_length_opposite+=1
 	else:
 		encrypted_text+=symbol
 os.system('cls' if os.name=='nt' else 'clear')
 print("Result: " + encrypted_text)
 ask=input('\nWould you like to work again? (y/n): ')
os.system('cls' if os.name=='nt' else 'clear')
print("Code written by @steven_006")