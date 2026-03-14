# 📂 File Organizer Automation

A simple automation script written in Python that automatically organizes files into folders based on their file type.

This project was created as a learning exercise to practice file system automation and basic scripting using Python.

---

## 🚀 Features

- Automatically organizes files from a selected directory
- Creates folders if they do not already exist
- Moves files into categories based on extension
- Ignores folders to avoid errors
- Prevents overwriting existing files

Current file categories:

| File Type | Destination Folder |
|-----------|-------------------|
| `.pdf` | `pdf/` |
| `.png` | `imagens/` |
| `.xlsx` | `excel/` |
| other files | `outros/` |

---

## 🛠 Technologies Used

- Python
- Built-in Python libraries:
  - `os`
  - `shutil`

```
## 📁 Project Structure

file-organizer-automation
│
├── organizer.py
├── run_organizer.bat
└── README.md

```

## ⚙️ How It Works

The script scans a directory, checks the extension of each file, and moves it to the appropriate folder.

Example:

```
Downloads/
│
├── report.pdf
├── image.png
├── spreadsheet.xlsx
└── file.txt
```

After running the script:

```
Downloads/
│
├── pdf/
│ └── report.pdf
│
├── imagens/
│ └── image.png
│
├── excel/
│ └── spreadsheet.xlsx
│
└── outros/
└── file.txt
```


## ▶️ How to Run

1. Clone this repository


git clone https://github.com/EstevesB23/download-folder-organizer.git


2. Navigate to the project folder


cd file-organizer-automation


3. Run the script


python organizer.py

```

## 🔄 Automation (Optional)

You can automate the execution using the Windows Task Scheduler to run the script periodically.

The repository includes a `.bat` file that can be scheduled for automatic execution.

```

## 📚 Learning Goals

This project was built to practice:

- Python scripting
- File system manipulation
- Basic automation
- Organizing code for GitHub projects


## 👩‍💻 Author

Brenda Esteves  

GitHub:  
https://github.com/EstevesB23
