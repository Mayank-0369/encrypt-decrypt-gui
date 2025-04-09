from tkinter import *
from tkinter import messagebox
import base64

# Correct password (could be stored securely in a more complex app)
correct_password = "01"

# Decrypt function
def decrypt():
    password = code.get()
    if password == correct_password:  # Correct password check
        screen2 = Toplevel(screen)  # Open a new window for decryption
        screen2.title("Decryption")
        screen2.geometry("400x300")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END).strip()  # Get and strip any trailing spaces

        if not message:
            messagebox.showerror("Decryption", "No message to decrypt")
            return

        try:
            # Decode the base64 message
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypted_message = base64_bytes.decode("ascii")

            # Show the decrypted message in the new window
            label1 = Label(screen2, text="DECRYPTED MESSAGE", font=("Arial", 14), fg="white", bg="#00bd56")
            label1.place(x=10, y=0)

            text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, decrypted_message)  # Insert decrypted message

        except Exception as e:
            messagebox.showerror("Decryption Error", f"Error during decryption: {e}")
    elif password == "":
        messagebox.showerror("Decryption", "Please input a password")
    else:
        messagebox.showerror("Decryption", "Invalid password")


# Encrypt function
def encrypt():
    password = code.get()

    if password == correct_password:  # Correct password check
        screen2 = Toplevel(screen)  # Open a new window for encryption
        screen2.title("Encryption")
        screen2.geometry("400x300")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END).strip()  # Get and strip any trailing spaces

        if not message:
            messagebox.showerror("Encryption", "No message to encrypt")
            return

        try:
            # Encrypt the message using base64
            message_bytes = message.encode("ascii")
            base64_bytes = base64.b64encode(message_bytes)
            encrypted_message = base64_bytes.decode("ascii")

            # Show the encrypted message in the new window
            label1 = Label(screen2, text="ENCRYPTED MESSAGE", font=("Arial", 14), fg="white", bg="#00bd56")
            label1.place(x=10, y=0)

            text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, encrypted_message)  # Insert encrypted message

        except Exception as e:
            messagebox.showerror("Encryption Error", f"Error during encryption: {e}")
    elif password == "":
        messagebox.showerror("Encryption", "Please input a password")
    else:
        messagebox.showerror("Encryption", "Invalid password")


# Reset function
def reset():
    code.set("")  # Clear the password entry field
    text1.delete(1.0, END)  # Clear the message text area


# Main screen function
def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("400x450")
    screen.title("Encryption & Decryption Tool")

    # Set up the background image (ensure the image path is correct)
    try:
        bg_image = PhotoImage(file="background.png")  # Replace with your image file
        bg_label = Label(screen, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)  # Make the background cover the whole window
    except Exception as e:
        print(f"Error loading background image: {e}")

    # Set up the icon for the window (if you have an image named keys.png)
    try:
        image_icon = PhotoImage(file="keys.png")
        screen.iconphoto(False, image_icon)
    except Exception as e:
        print(f"Error loading icon: {e}")

    # Add labels and widgets to the screen
    Label(text="Enter text for encryption and decryption", fg="white", font=("Calibri", 14), bg="#00bd56").place(x=10, y=10)

    text1 = Text(screen, font="Roboto 16", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=380, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="white", font=("Calibri", 14), bg="#00bd56").place(x=10, y=160)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show="*").place(x=10, y=200)

    # Stylish buttons
    Button(text="ENCRYPT", height=2, width=23, bg="#ed3833", fg="white", bd=0, font=("Arial", 12, "bold"), relief=SOLID, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height=2, width=23, bg="#00bd56", fg="white", bd=0, font=("Arial", 12, "bold"), relief=SOLID, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height=2, width=50, bg="#1089ff", fg="white", bd=0, font=("Arial", 12, "bold"), relief=SOLID, command=reset).place(x=10, y=300)

    screen.mainloop()

# Run the main screen
main_screen()
