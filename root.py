import tkinter as tk
from PIL import Image, ImageTk
import datetime

def close_splash():
    splash.destroy()
    root.deiconify()

def get_greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if 5 <= hour < 12:
        return "Good Morning,"
    elif 12 <= hour < 18:
        return "Good Afternoon,"
    else:
        return "Good Evening,"

# Create the main window
root = tk.Tk()
root.title("Ruia Student Diary")
root.geometry("360x640")
root.withdraw()  # Hide main window until splash screen closes

# Create a splash screen window
splash = tk.Toplevel(root)
splash.overrideredirect(True)  # Remove window decorations
splash.geometry("360x640")
splash.configure(bg="maroon")

# Load image
image_path = "images/college_logo.jpg"  # Change this to your image path
image = Image.open(image_path)
image = image.resize((240, 320))  # Resizing without ANTIALIAS for simplicity
photo = ImageTk.PhotoImage(image)

# Display image on splash screen
label = tk.Label(splash, image=photo, bg="maroon")
label.image = photo  # keep a reference
label.place(relx=0.5, rely=0.5, anchor="center")

# Close splash screen after 2 seconds
splash.after(2000, close_splash)

# Get greeting message
greeting = get_greeting()

# Create header
header = tk.Frame(root, bg="maroon", height=120, width=360)
header.pack(fill="x")

# Create label for greeting
greeting_label = tk.Label(header, text=greeting, fg="white", bg="maroon", font=("Arial", 16))
greeting_label.pack(side="left", padx=10, anchor="w")

# Student name (replace "Student Name" with actual name)
student_name = "Jagveer Kaur"
name_label = tk.Label(header, text=student_name, fg="white", bg="maroon", font=("Arial", 16))
name_label.pack(side="left", padx=10, anchor="w")

# Load small image on the right side
small_image_path = "images/college_logo.jpg"  # Change this to your small image path
small_image = Image.open(small_image_path)
small_image = small_image.resize((50, 50))  # Resizing the image
small_photo = ImageTk.PhotoImage(small_image)

small_image_label = tk.Label(header, image=small_photo, bg="maroon")
small_image_label.image = small_photo  # keep a reference
small_image_label.pack(side="right", padx=10, pady=10)

# Create a section below the header with a single slideable image
canvas = tk.Canvas(root, bg="white", width=360, height=120)
canvas.pack()

# Add slideable image (replace the path with your image path)
image_path = "images/image1.jpg"  # Change this to your image path
image = Image.open(image_path)
image = image.resize((360, 100))  # Adjust size as needed
photo = ImageTk.PhotoImage(image)

frame_id = canvas.create_image(0, 0, anchor="nw", image=photo)
canvas.itemconfig(frame_id, tags=("image",))

# Text below the slideable image
college_text = "Ramnarian Ruia Autonomous College"
college_label = tk.Label(root, text=college_text, font=("Arial", 12), bg="white")
college_label.pack()

# Rectangle below the college text (for Attendance, Theory, Practical, Overall)
rectangle1 = tk.Frame(root, bg="#e6e6e6", height=120)
rectangle1.pack(fill="x", pady=10)

# Text on the rectangle1
attendance_text = "Attendance"
theory_text = "Theory"
practical_text = "Practical"
overall_text = "Overall"

attendance_label = tk.Label(rectangle1, text=attendance_text, font=("Arial", 12), bg="#e6e6e6", anchor="center")
attendance_label.grid(row=0, column=1, padx=5, pady=10)

theory_label = tk.Label(rectangle1, text=theory_text, font=("Arial", 12), bg="#e6e6e6", anchor="w")
theory_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

practical_label = tk.Label(rectangle1, text=practical_text, font=("Arial", 12), bg="#e6e6e6", anchor="w")
practical_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

overall_label = tk.Label(rectangle1, text=overall_text, font=("Arial", 12), bg="#e6e6e6", anchor="w")
overall_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Horizontal bars beside each text on rectangle1
theory_bar = tk.Canvas(rectangle1, bg="white", height=20, width=100, bd=0, highlightthickness=0)
theory_bar.create_rectangle(0, 0, 100, 20, fill="green")
theory_bar.grid(row=1, column=1, padx=(5, 10), pady=5)

practical_bar = tk.Canvas(rectangle1, bg="white", height=20, width=100, bd=0, highlightthickness=0)
practical_bar.create_rectangle(0, 0, 50, 20, fill="blue")
practical_bar.grid(row=2, column=1, padx=(5, 10), pady=5)

overall_bar = tk.Canvas(rectangle1, bg="white", height=20, width=100, bd=0, highlightthickness=0)
overall_bar.create_rectangle(0, 0, 75, 20, fill="red")
overall_bar.grid(row=3, column=1, padx=(5, 10), pady=5)

# Rectangle for small image buttons
rectangle2 = tk.Frame(root, bg="#e6e6e6")
rectangle2.pack(fill="both", expand=True)

# Create a frame to hold the buttons
button_frame = tk.Frame(rectangle2, bg="#e6e6e6")
button_frame.pack(fill="both", expand=True, padx=5, pady=5)

# Create a canvas for vertical scrolling
canvas = tk.Canvas(button_frame, bg="#e6e6e6")
canvas.pack(side="left", fill="both", expand=True)

# Add scrollbar for vertical scrolling
scrollbar = tk.Scrollbar(button_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Create a frame to hold the buttons
button_frame_inner = tk.Frame(canvas, bg="#e6e6e6")
canvas.create_window((0, 0), window=button_frame_inner, anchor="nw")

# Leave space for 4x4 small image buttons
# Create 14 small image buttons with text below them
for i in range(14):
    # Load small image for button
    small_button_image = Image.open("images/button1.png")  # Replace with your image path
    small_button_image = small_button_image.resize((40, 40))  # Resize the image
    small_button_photo = ImageTk.PhotoImage(small_button_image)

    # Create button
    button = tk.Button(button_frame_inner, image=small_button_photo, borderwidth=0)
    button.image = small_button_photo  # Keep a reference to prevent garbage collection
    button.grid(row=i // 4, column=i % 4, padx=5, pady=5)

    # Add text below button
    text_label = tk.Label(button_frame_inner, text=f"Button {i+1}", bg="#e6e6e6")
    text_label.grid(row=(i // 4) + 1, column=i % 4, pady=(0, 5))

# Update the scroll region
button_frame_inner.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Create footer frame
footer_frame = tk.Frame(root, bg="white", height=100, width=360)
footer_frame.pack(side="bottom", fill="x")

# Draw semi-circle void
semi_circle_canvas = tk.Canvas(footer_frame, bg="white", width=360, height=50, highlightthickness=0)
semi_circle_canvas.pack()

# Draw maroon button in the void
maroon_button = tk.Button(footer_frame, text="Maroon", bg="maroon", fg="white", width=10)
maroon_button.place(relx=0.5, rely=0.5, anchor="center")

# Draw house symbol button
# Draw maroon circular button in the void with house icon in the center
house_image = Image.open("images/house.png")  # Replace with your house symbol image
house_image = house_image.resize((40, 40))  # Adjust the size of the house icon
house_icon = ImageTk.PhotoImage(house_image)

def on_enter(event):
    house_button.config(bg="brown")

def on_leave(event):
    house_button.config(bg="maroon")

house_button = tk.Button(footer_frame, image=house_icon, bg="maroon", bd=0, width=50, height=50, compound="center")  # Adjust the button width and height
house_button.image = house_icon
house_button.place(relx=0.5, rely=0.5, anchor="center")
house_button.bind("<Enter>", on_enter)
house_button.bind("<Leave>", on_leave)


# Draw calendar button
calendar_image = Image.open("images/calendar.png")  # Replace with your calendar image
calendar_image = calendar_image.resize((30, 30))
calendar_icon = ImageTk.PhotoImage(calendar_image)
calendar_button = tk.Button(footer_frame, image=calendar_icon, text="Calendar", compound="top", bg="white", bd=0)
calendar_button.image = calendar_icon
calendar_button.place(relx=0.2, rely=0.5, anchor="center")
calendar_button.config(width=40)

# Draw notification button
notification_image = Image.open("images/notification.png")  # Replace with your notification image
notification_image = notification_image.resize((30, 30))
notification_icon = ImageTk.PhotoImage(notification_image)
notification_button = tk.Button(footer_frame, image=notification_icon, text="Notification", compound="top", bg="white", bd=0)
notification_button.image = notification_icon
notification_button.place(relx=0.4, rely=0.5, anchor="center")

# Draw profile button
profile_image = Image.open("images/profile.png")  # Replace with your profile image
profile_image = profile_image.resize((30, 30))
profile_icon = ImageTk.PhotoImage(profile_image)
profile_button = tk.Button(footer_frame, image=profile_icon, text="Profile", compound="top", bg="white", bd=0)
profile_button.image = profile_icon
profile_button.place(relx=0.6, rely=0.5, anchor="center")

# Draw ID card button
id_card_image = Image.open("images/id_card.png")  # Replace with your ID card image
id_card_image = id_card_image.resize((30, 30))
id_card_icon = ImageTk.PhotoImage(id_card_image)
id_card_button = tk.Button(footer_frame, image=id_card_icon, text="ID Card", compound="top", bg="white", bd=0)
id_card_button.image = id_card_icon
id_card_button.place(relx=0.8, rely=0.5, anchor="center")

# Run the Tkinter event loop
root.mainloop()
