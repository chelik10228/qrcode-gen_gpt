import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL or Text.")
        return

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,  # Adjusted box size for a smaller QR code
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to a format suitable for Tkinter
    img.save("qrcode.png")  # Save the QR code as an image
    img_tk = ImageTk.PhotoImage(img)

    # Display the QR code in the label
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # Keep a reference to avoid garbage collection

def save_qr_code():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL or Text.")
        return

    filename = "qrcode.png"
    qr = qrcode.make(url)
    qr.save(filename)
    messagebox.showinfo("Success", f"QR code saved as {filename}")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place the URL entry
url_label = tk.Label(root, text="Enter URL or Text:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)

# Create and place the Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

# Create a label to display the QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Create and place the Save button below the QR code
save_button = tk.Button(root, text="Save QR Code", command=save_qr_code)
save_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
