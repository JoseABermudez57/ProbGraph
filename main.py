from tkinter import Tk, Button, Label, filedialog
import pandas as pd

def open_files():
    root = Tk()
    root.withdraw()

    file = filedialog.askopenfile(filetypes=[('CSV Files', '*.csv')])  # Open the dialog box
    if file:
        # Open file process
        content = pd.read_csv(file, delimiter=';')
        attributes = content.columns[0].replace('"', '').split(';')
        print(content)
        file.close()

# Create the main window
window = Tk()
window.geometry("400x200")
window.title("ProbGraph")
window.eval('tk::PlaceWindow . center')  # Center the program

# Create the "Open file" section
text = Label(window, text="Seleccione el archivo '.csv' que desee analizar")
text.pack(anchor="center", expand="true")
open_button = Button(window, text="Abrir archivo", command=open_files)
open_button.pack(anchor="center", expand="true")

# Initiate the event loop for the graphical interface
window.mainloop()
