import tkinter as tk
from tkinter import filedialog
import os

desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")
filename = ""
output_file = desktop_path
light_b = 0
dark_b = 49


def gui_launch():
    def file_choose():
        global filename
        filename = filedialog.askopenfilename()
        text.delete(1.0, tk.END)
        text.insert(tk.END, filename)
        return

    def destroy_window():
        global filename
        global output_file
        global light_b
        global dark_b
        output_file = output.get(1.0, "end-1c")
        filename = text.get(1.0, "end-1c")
        light_b = int(light_b_i.get(1.0, "end-1c"))
        dark_b = int(dark_b_i.get(1.0, "end-1c"))
        root.destroy()
        return

    root = tk.Tk()
    button = tk.Button(root, text="Choose file", command=file_choose)
    text = tk.Text(root, width=57, height=0)
    button.pack()
    text.pack()
    text.insert(tk.END, "No file selected")

    out_folder = tk.Text(root, width=57, height=0)
    out_folder.insert(tk.END, "Output folder:")
    out_folder.configure(state="disabled")
    out_folder.pack()

    output = tk.Text(root, width=57, height=0)
    output.pack()
    output.insert(tk.END, os.path.join(desktop_path, "output.schematic"))

    dark_b_d = tk.Text(root, width=57, height=0)
    dark_b_d.insert(tk.END, "Dark block numerical id:")
    dark_b_d.configure(state="disabled")
    dark_b_d.pack()

    dark_b_i = tk.Text(root, width=57, height=0)
    dark_b_i.insert(tk.END, "49")
    dark_b_i.pack()

    light_b_d = tk.Text(root, width=57, height=0)
    light_b_d.insert(tk.END, "Light block numerical id:")
    light_b_d.configure(state="disabled")
    light_b_d.pack()

    light_b_i = tk.Text(root, width=57, height=0)
    light_b_i.insert(tk.END, "0")
    light_b_i.pack()

    begin_btn = tk.Button(root, text="Convert to schematic!", command=destroy_window)
    begin_btn.pack()

    root.title("Image to schematic")
    root.mainloop()
    return [filename, output_file, dark_b, light_b]
