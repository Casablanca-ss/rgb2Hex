"""
这是一个rgb转16进制的小工具
"""
import tkinter as tk
import pyperclip


def rgb_to_hex(rgb):
    hex_color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
    return hex_color


def convert_color():
    try:
        color_input = color_entry.get()
        rgb_color = [int(i) for i in color_input.split(",")]
        hex_color = rgb_to_hex(rgb_color)
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, hex_color)
        result_text.config(state=tk.DISABLED)
        color_entry.delete(0, tk.END)  # Clear the input field
    except Exception:
        color_entry.delete(0, tk.END)  # Clear the input field


def copy_to_clipboard():
    hex_color = result_text.get(1.0, tk.END).strip()
    pyperclip.copy(hex_color)


root = tk.Tk()
root.title("RGB to Hex Converter")

color_label = tk.Label(root, text="Enter RGB color (comma-separated):")
color_entry = tk.Entry(root, width=30)
convert_button = tk.Button(root, text="Convert", command=convert_color)
result_text = tk.Text(root, width=40, height=1, state=tk.DISABLED)
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)

color_label.pack(pady=10)
color_entry.pack(pady=10)
convert_button.pack(pady=10)
result_text.pack(pady=10)
copy_button.pack(pady=10)

root.mainloop()
