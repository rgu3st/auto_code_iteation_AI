from tkinter import Tk, PhotoImage, Label

def main():
    # Create root window
    root = Tk()

    # Set window title and size
    root.title("Display Image")
    root.geometry("300x200")  # Set window width (300 pixels) and height (200 pixels)

    # Load image using PhotoImage
    image = PhotoImage(file="./CheetahBaby.jpg", imgtype="jpg")

    # Create label and add image to it
    label = Label(root, image=image)

    # Pack label to fill the window
    label.pack(pady=10, padx=10, fill="both", expand="yes")

    # Start Tkinter mainloop
    root.mainloop()

if __name__ == "__main__":
    main()