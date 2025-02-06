### 📜 **README.md**

# 📂 Automated Report Processing

This script automates the process of organizing and managing reports by moving files from a source folder to a processed folder. It also collects useful details about each file, such as size and creation date.

## 🚀 What This Script Does
- Moves files ending in `_processado.xlsx` from the **source folder** (`relatorios`) to the **processed folder** (`relatorios_processados`).
- Before moving, it captures important details like:
  - 📆 **Creation date**
  - 📏 **File size**
- Automatically creates the destination folder if it doesn’t exist.
- Handles errors gracefully and provides clear feedback.
- Displays a summary of processed files at the end.

---

## 📌 Requirements
- Python **3.7 or later**
- Uses only built-in libraries: `os`, `shutil`, and `time` (no extra installations needed).

---

## 🛠️ How to Use

### 1️⃣ Clone the repository (or copy the script)
```sh
git clone https://github.com/yourusername/file-processing-script.git
cd file-processing-script
```

### 2️⃣ Check if Python is installed
```sh
python --version
```

### 3️⃣ Set up the folders
- **Source folder:** `relatorios` → Place the files to be processed here.
- **Destination folder:** `relatorios_processados` → The script will move files here automatically.

### 4️⃣ Run the script
```sh
python process_files.py
```

---

## 📂 Folder Structure

```
/file-processing-script
│── process_files.py          # Main script
│── README.md                 # Documentation
│── relatorios/               # Source folder (put files here)
│── relatorios_processados/   # Destination folder (files will be moved here)
```

---

## 📊 Example Output

```
Files to be moved: ['report1_processado.xlsx', 'report2_processado.xlsx']
File "report1_processado.xlsx" moved to "relatorios_processados"
File "report2_processado.xlsx" moved to "relatorios_processados"
Number of files moved: 2
File: report1_processado.xlsx, Created on: Sat Feb 3 14:23:01 2024, Size: 45,321 bytes
File: report2_processado.xlsx, Created on: Sun Feb 4 09:12:45 2024, Size: 12,894 bytes
```

---

## 🔍 How It Works (Behind the Scenes)
1. The script **checks if the source folder exists**. If not, it stops and shows an error message.
2. It **creates the destination folder** if it doesn’t exist.
3. It **scans the source folder** and finds files ending in `_processado.xlsx`.
4. Before moving the files, it **extracts file details** like creation date and size.
5. It **moves each file** to the processed folder.
6. Finally, it **displays a summary** of the moved files.

---

## 🛑 Error Handling
This script includes built-in safeguards to prevent issues:
- 🚫 If the **source folder doesn’t exist**, it stops and informs the user.
- 🔎 If **no `_processado.xlsx` files are found**, it prints a message and exits.
- ❌ If an **error occurs while moving files**, it logs the issue but continues processing the rest.

---

## 🏆 Want to Contribute?
Feel free to improve this script! Fork the repository and submit a pull request. 🚀

---

## 📄 License
This project is licensed under the **MIT License** – you can use and modify it freely.
```

---
