from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from stegano import lsb

# Function to open the image file
def open_image():
  global img_path
  img_path = filedialog.askopenfilename(title="Open Image", filetypes=[("Image Files", "*.png *.jpg")])
  if img_path:
    global img_display
    img = Image.open(img_path)
    img_display = ImageTk.PhotoImage(img)
    image_label.config(image=img_display)

# Function to encode message in image
def encode_image():
  global img_path
  if not img_path:
    return

  # Get message from text box
  message = message_entry.get()

  # Open image and convert to RGB
  img = Image.open(img_path).convert("RGB")

  # Encode message using LSB
  secret = lsb.hide(img, message)

  # Save encoded image
  new_path = "stego_image.png"
  secret.save(new_path)

  # Display message
  message_label.config(text="Message encoded successfully! Saved as: " + new_path)

# Function to decode message from image
def decode_image():
  global img_path
  if not img_path:
    return

  # Open image
  img = Image.open(img_path)

  # Decode message using LSB
  revealed_message = lsb.reveal(img)

  # Display decoded message
  message_label.config(text="Decoded message: " + revealed_message)

# Function to clear all fields
def clear_all():
  global img_path
  img_path = None
  image_label.config(image="")
  message_entry.delete(0, END)
  message_label.config(text="")

# Initialize main window
root = Tk()
root.title("Image Steganography")

# Create two frames
image_frame = Frame(root)
message_frame = Frame(root)
image_frame.pack(padx=10, pady=10)
message_frame.pack(padx=10, pady=10)

# Image label
image_label = Label(image_frame, image="")
image_label.grid(row=0, columnspan=2)

# Button to open image
open_button = Button(image_frame, text="Open Image", command=open_image)
open_button.grid(row=1, column=0, pady=5)

# Message entry
message_entry = Entry(message_frame, width=50)
message_entry.grid(row=0, column=0, pady=5)

# Button to encode message
encode_button = Button(message_frame, text="Encode Message", command=encode_image)
encode_button.grid(row=1, column=0, pady=5)

# Button to decode message
decode_button = Button(message_frame, text="Decode Message", command=decode_image)
decode_button.grid(row=2, column=0, pady=5)

# Button to clear all fields
clear_button = Button(message_frame, text="Clear All", command=clear_all)
clear_button.grid(row=3, column=0, pady=5)

# Label to display messages
message_label = Label(message_frame, text="")
message_label.grid(row=4, columnspan=2)

# Run the main loop
root.mainloop()
