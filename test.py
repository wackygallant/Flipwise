import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")

# 1. Configure the grid system of the main window
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

# 2. Create a button and place it in row 0, col 0
# 'sticky="nsew"' tells the button to stretch to the edges of its grid cell
button = ctk.CTkButton(app, text="I Expand!")
button.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

app.mainloop()