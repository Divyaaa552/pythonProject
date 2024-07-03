import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Image Steganography")

#Image
frame1 = tk.Frame(root, bg="lightblue", padx=100, pady=100)
frame1.pack(side="left", padx=20, pady=20)

#Messagebox
frame2 = tk.Frame(root, bg="lightblue", padx=100, pady=100)
frame2.pack(side="left", padx=50, pady=60)

# Add widgets to the frame

label = tk.Label(frame1, text="Image", font=("Helvetica", 16))
label.pack()


label = tk.Label(frame2, text="Message", font=("Helvetica", 16))
label.pack()

#frame3
button_frame = tk.Frame(root, bg="lightblue", padx=250, pady=80)
button_frame.pack(side="left", padx=30, pady=30)

#button = tk.Button(frame3, text="Click Me!", command=root.quit)
#button.pack(side="left")

button1 = tk.Button(button_frame, text="Button 1")
button2 = tk.Button(button_frame, text="Button 2")
button3 = tk.Button(button_frame, text="Button 3")
button4 = tk.Button(button_frame, text="Button 4")

# Pack the buttons into the frame
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.LEFT)



# Run the main event loop
root.mainloop()
