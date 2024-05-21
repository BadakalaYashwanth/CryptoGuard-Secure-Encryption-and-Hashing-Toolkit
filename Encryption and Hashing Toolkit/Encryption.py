from tkinter import messagebox, simpledialog, Tk

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message, task):
    if not is_even(len(message)):
        message = message + 'x'  # Padding for odd-length messages
    letter_list = list(message)
    mid = len(message) // 2
    even_letters = letter_list[:mid]
    odd_letters = letter_list[mid:]
    
    if task == 'encrypt':
        letter_list = [val for pair in zip(odd_letters, even_letters) for val in pair]
    elif task == 'decrypt':
        letter_list = [val for pair in zip(even_letters, odd_letters) for val in pair]
    
    new_message = ''.join(letter_list)
    return new_message

def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return  task.lower()  # Convert to lowercase to standardize the task input


def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

root = Tk()
root.withdraw() #hide the main window

while True:
    task = get_task()
    if task in ['encrypt', 'decrypt']:
       message = get_message()
       processed_message = swap_letters(message, task)
    if task == 'encrypt':
         messagebox.showinfo('Ciphertext of the secret message is:', processed_message)
    elif task == 'decrypt':
            messagebox.showinfo('Plaintext of the secret message is:', processed_message)
    else:
        break


root.mainloop()