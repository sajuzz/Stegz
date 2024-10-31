import tkinter as tk
from tkinter import filedialog
from PIL import Image

def hide_text_in_image(image_path, text):
    img = Image.open(image_path)
    pixels = img.load()

    index = 0
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b = pixels[x, y]

            # Convert text to binary
            binary_text = ''.join(format(ord(char), '08b') for char in text)

            # Hide 3 bits of each pixel
            if index < len(binary_text):
                r = (r & 252) | int(binary_text[index])
                index += 1
            if index < len(binary_text):
                g = (g & 252) | int(binary_text[index])
                index += 1
            if index < len(binary_text):
                b = (b & 252) | int(binary_text[index])
                index += 1

            pixels[x, y] = (r, g, b)

    img.save("stego_image.png")

def select_image():
    file_path = filedialog.askopenfilename(title="Select Image")
    image_entry.delete(0, tk.END)
    image_entry.insert(0, file_path)

def select_text_or_audio():
    file_path = filedialog.askopenfilename(title="Select Text or Audio File")
    text_audio_entry.delete(0, tk.END)
    text_audio_entry.insert(0, file_path)

# Create the main window
root = tk.Tk()
root.title("Steganography Tool")

# Create labels and entry fields
image_label = tk.Label(root, text="Image File:")
image_label.pack()
image_entry = tk.Entry(root, width=50)
image_entry.pack()
image_button = tk.Button(root, text="Select Image", command=select_image)
image_button.pack()

text_audio_label = tk.Label(root, text="Text or Audio File:")
text_audio_label.pack()
text_audio_entry = tk.Entry(root, width=50)
text_audio_entry.pack()
text_audio_button = tk.Button(root, text="Select File", command=select_text_or_audio)
text_audio_button.pack()

# Add buttons for hiding and extracting
hide_button = tk.Button(root, text="Hide", command=lambda: hide_text_in_image(image_entry.get(), text_audio_entry.get()))
hide_button.pack()
# ... other buttons for different operations ...

root.mainloop()