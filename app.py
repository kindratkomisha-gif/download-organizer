import os
import shutil
import sys
import time
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


base_pass = filedialog.askdirectory(title="Select folder for sorting")

if not base_pass:
    exit()

i = 0

while True:
    time.sleep(5)

    grouped_file = {}

    report = open("report.txt", "a", encoding="utf-8")
    stop_file = "stop.txt"
    if os.path.exists(stop_file):
        report.write("Stop by user")
        os.remove(stop_file)
        sys.exit(0)

    for item in os.scandir(base_pass):
        if item.is_dir():
            continue

        file_name = item.name

        if file_name.endswith(('.crdownload', '.part', '.tmp')):
            continue

        ext = file_name.rpartition(".")[2]
        if ext not in grouped_file:
            grouped_file[ext] = []

        grouped_file[ext].append(item.path)

    if not grouped_file:
        continue
    for ext, file_l in grouped_file.items():
        report.write(f"{ext.upper()}: {file_l}\n")
    report.flush()
    report.close()

    for ext, file_list in grouped_file.items():
        folder_path = os.path.join(base_pass, ext.upper() + "_folder")
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        for file_path in file_list:
            old_path = os.path.basename(file_path)
            new_path = os.path.join(folder_path, old_path)

            shutil.move(file_path, new_path)