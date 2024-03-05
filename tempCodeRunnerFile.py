import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("300x200")

# Create a frame to contain the canvas and scrollbars
button_frame = tk.Frame(root)
button_frame.pack(fill="both", expand=True)

# Create a canvas for vertical scrolling
canvas = tk.Canvas(button_frame, bg="#e6e6e6", width=280, height=180)  # Adjusted canvas size
canvas.pack(side="left", fill="both", expand=True)  # Expand both horizontally and vertically

# Add scrollbar for vertical scrolling
scrollbar_vertical = tk.Scrollbar(button_frame, orient="vertical", command=canvas.yview)
scrollbar_vertical.pack(side="right", fill="y")

# Link the scrollbars to the canvas
canvas.config(yscrollcommand=scrollbar_vertical.set)

# Create a frame to hold the content
content_frame = tk.Frame(canvas, bg="#e6e6e6")

# Add the frame to the canvas
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Update the scroll region
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Add horizontal scrollbar to canvas for slideable images
hbar = tk.Scrollbar(button_frame, orient="horizontal", command=canvas.xview)
hbar.pack(side="bottom", fill="x")
canvas.config(xscrollcommand=hbar.set)

root.mainloop()
