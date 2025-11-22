import socket
import tkinter as tk
from tkinter import messagebox
import json

def fetch_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "City name cannot be empty!")
        return

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 65432))
        client_socket.send(city.encode())
        weather_info = client_socket.recv(4096).decode()
        client_socket.close()

        # Display the weather info
        display_weather(weather_info)
    except Exception as e:
        messagebox.showerror("Connection Error", f"Error: {e}")

def display_weather(weather_info):
    try:
        weather_data = json.loads(weather_info)

        # Clear previous content
        for widget in weather_frame.winfo_children():
            widget.destroy()

        if "Error" in weather_data:
            error_label = tk.Label(weather_frame, text=weather_data["Error"], font=("Helvetica", 14), fg="red", bg="white")
            error_label.pack(pady=20)
        else:
            # Display weather details
            for key, value in weather_data.items():
                label = tk.Label(weather_frame, text=f"{key}: {value}", font=("Helvetica", 14), bg="white")
                label.pack(anchor="w", padx=10, pady=5)

    except json.JSONDecodeError:
        messagebox.showerror("Error", "Invalid data received from server.")

# ADD: Enter key trigger function
def on_enter(event):
    fetch_weather()

# Tkinter GUI setup
root = tk.Tk()
root.title("Weather Reporting App")
root.geometry("500x600")

header_label = tk.Label(root, text="Weather Reporting App", font=("Helvetica", 20, "bold"), bg="#0066cc", fg="white")
header_label.pack(fill="x")

input_frame = tk.Frame(root, bg="#0066cc")
input_frame.pack(fill="x", pady=10)

city_label = tk.Label(input_frame, text="Enter City:", font=("Helvetica", 14), bg="#0066cc", fg="white")
city_label.pack(side="left", padx=10)

city_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=20)
city_entry.pack(side="left", padx=10)

# ADD: Bind Enter key to fetch_weather
city_entry.bind('<Return>', on_enter)

fetch_button = tk.Button(input_frame, text="Get Weather", font=("Helvetica", 14), command=fetch_weather, bg="white", fg="#0066cc")
fetch_button.pack(side="left", padx=10)

weather_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
weather_frame.pack(fill="both", expand=True, padx=20, pady=20)

root.mainloop()
