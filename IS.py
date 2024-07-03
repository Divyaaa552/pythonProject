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
frame1 = Frame(root)
frame2 = Frame(root)
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

# Image label
image_label = Label(frame1, image="")
image_label.pack()

# Button to open image
open_button = Button(frame1, text="Open Image", command=open_image)
open_button.pack(pady=5)

# Message entry
message_entry = Entry(frame2, width=50)
message_entry.pack(pady=5)

# Button to encode message
encode_button = Button(frame2, text="Encode Message", command=encode_image)
encode_button.pack(pady=5)

# Button to decode message
decode_button = Button(frame2, text="Decode Message", command=decode_image)
decode_button.pack(pady=5)

# Button to clear all fields
clear_button = Button(frame2, text="Clear All", command=clear_all)
clear_button.pack(pady=5)

# Label to display messages
message_label = Label(frame2, text="")
message_label.pack()

# Run the main loop
root.mainloop()
