import os
import shutil

directory = r"C:\Users\crcabrera\Desktop\OJT Gab and Shin\SALN COPY"
os.chdir(directory)

for file in os.listdir():
    if file.startswith("SALN - ") and file.endswith(".pdf"):
        name = file.replace("SALN - ", "").replace(".pdf", "")
        folder_path = os.path.join(directory, name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)  # Create folder
        
        shutil.move(file, folder_path)  # Move file into folder
