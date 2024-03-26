# Creating a simple python based plaintext encryption/decryption program based on the Caesar Cipher. I am practicing importing libraries such as tkinter and creating a simple GUI for the user.

# Importing tkinter library
import tkinter as ttk

# Function to encrypt 
def encrypt():
  # Get the input (cleartext) from the entry widget
  cleartext = cleartext_entry.get()

  shift = 3  # Shifts the alphabet 3 characters to the right. (You can adjust this value)

  # Creating an string to store the encrypted text
  encrypted_text = ""

  # Putting each character in the plaintext through the shift.
  for char in cleartext:
      # Check if the character is an uppercase letter
      if char.isupper():
          # Encrypt uppercase letters
          encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
      # Check if the character is a lowercase letter
      elif char.islower():
          # Encrypt lowercase letters
          encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
      else:
          # If the character is not a letter, keep it unchanged
          encrypted_char = char
      # Append the encrypted character to the encrypted text
      encrypted_text += encrypted_char

  # Display the encrypted text in the output widget
  output_entry.delete(0, "end")  # Clear any previous text
  output_entry.insert(0, encrypted_text)

# Function to decrypt 
def decrypt():
  # Get the encrypted text from the entry widget
  encryptedtext = encryptedtext_entry.get()

  shift = 3  # Shifts the alphabet 3 characters to the left. (Same shift as encryption)

  # Initialize an empty string to store the decrypted text
  decrypted_text = ""

  # Iterate through each character in the encrypted text
  for char in encryptedtext:
      # Check if the character is an uppercase letter
      if char.isupper():
          decrypted_char = chr(((ord(char) - 65 - shift) % 26) + 65)
      # Check if the character is a lowercase letter
      elif char.islower():
          decrypted_char = chr(((ord(char) - 97 - shift) % 26) + 97)
      else:
          # If the character is not a letter, keep it unchanged
          decrypted_char = char
      # Append the decrypted character to the decrypted text
      decrypted_text += decrypted_char

  # Display the decrypted text in the output widget
  output_entry.delete(0, "end")  # Clear any previous text
  output_entry.insert(0, decrypted_text)

# Creating the application window
root = ttk.Tk()
root.title("Simple Plaintext Encryption and Decryption Program by xobash")

# Creating labels and buttons
cleartext_label = ttk.Label(root, text="Cleartext:")
cleartext_label.grid(row=0, column=0, padx=5, pady=5)

cleartext_entry = ttk.Entry(root)
cleartext_entry.grid(row=0, column=1, padx=5, pady=5)

encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=0, column=2, padx=5, pady=5)

encryptedtext_label = ttk.Label(root, text="Encrypted text:")
encryptedtext_label.grid(row=1, column=0, padx=5, pady=5)

encryptedtext_entry = ttk.Entry(root)
encryptedtext_entry.grid(row=1, column=1, padx=5, pady=5)

decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=1, column=2, padx=5, pady=5)

output_label = ttk.Label(root, text="Output:")
output_label.grid(row=2, column=0, padx=5, pady=5)

output_entry = ttk.Entry(root)
output_entry.grid(row=2, column=1, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
