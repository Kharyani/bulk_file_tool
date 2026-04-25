# 📁 Bulk File Renamer & Smart Organizer

## 📄 Description

This project is a Python-based CLI application that automates file management tasks. It allows users to rename multiple files in bulk and organize them into structured folders efficiently.

---

## 🚀 Features

* 🔹 Bulk file renaming
* 🔹 Add prefix and suffix
* 🔹 Replace words in filenames
* 🔹 Auto-numbering (file_1, file_2, …)
* 🔹 Organize files by type (JPG, PDF, etc.)
* 🔹 Organize files by date
* 🔹 Preview changes before applying
* 🔹 Logging system (CSV file)
* 🔹 Error handling (invalid path, file exists, etc.)

---

## 🛠 Technologies Used

* Python 3
* `os` module
* `shutil` module
* `datetime` module
* `csv` module

---

## 📁 Project Structure

```
bulk_file_tool/
│
├── main.py
├── file_operations_log.csv
├── sample_files/
│   ├── image1.jpg
│   ├── doc1.pdf
│   └── video1.mp4
```

---

## ▶️ How to Run

1. Open terminal or command prompt
2. Navigate to project folder
3. Run the program:

```
python main.py
```

4. Follow the menu options

---

## 📌 Usage Steps

1. Select folder
2. Rename files (optional)
3. Preview changes
4. Apply changes
5. Organize files
6. View logs

---

## 📊 Output

* Files renamed based on selected pattern
* Files organized into folders (type/date)
* Log file generated with operation details

---

## 👨‍💻 Author

Kashish Haryani

---

## 📎 Notes

* Make sure Python is installed
* Use correct folder path
* Avoid selecting empty folders
