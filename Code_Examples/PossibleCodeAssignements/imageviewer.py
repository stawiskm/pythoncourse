import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        self.image_label = tk.Label(root)
        self.image_label.pack(padx=10, pady=10)

        self.previous_button = tk.Button(root, text="Previous", command=self.show_previous_image)
        self.previous_button.pack(side="left", padx=5, pady=5)

        self.next_button = tk.Button(root, text="Next", command=self.show_next_image)
        self.next_button.pack(side="right", padx=5, pady=5)

        self.load_button = tk.Button(root, text="Load", command=self.load_image_directory)
        self.load_button.pack(padx=10, pady=5)

        self.status_label = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(fill=tk.X, padx=10, pady=5)

        self.current_directory = ""
        self.image_list = []
        self.current_image_index = 0

    def load_image_directory(self):
        self.current_directory  = filedialog.askdirectory()
        if self.current_directory:
            self.image_list = [f for f in os.listdir(self.current_directory) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]
            if self.image_list:
                self.current_image_index = 0
                self.load_and_display_current_image()

    def load_and_display_current_image(self):
        if self.image_list:
            image_path = os.path.join(self.current_directory, self.image_list[self.current_image_index])
            try:
                image = Image.open(image_path)
                image = image.resize((400, 400), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image=image)
                self.image_label.config(image=photo)
                self.image_label.image = photo

                self.update_status_label()
            except Exception as e:
                print("Error loading image:", e)


    def show_previous_image(self):
        if self.image_list:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_list)
            self.load_and_display_current_image()

    def show_next_image(self):
        if self.image_list:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_list)
            self.load_and_display_current_image()

    def update_status_label(self):
        if self.image_list:
            filename = self.image_list[self.current_image_index]
            self.status_label.config(text=f"Current Image: {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerApp(root)
    root.mainloop()
