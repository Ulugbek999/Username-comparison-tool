# 🔍 Username Comparison Tool

This Python-based tool was initially created to compare usernames across two large datasets (each with 6000+ entries) to identify mismatches and ensure consistency across systems. It’s designed to help developers, data engineers, or IT professionals perform fast, accurate username verification between databases.

---

### 📁 Background

This project was originally developed during my internship at **BGE (Baltimore Gas and Electric)**, where I worked in the Project Management Office as a **Software Administrator**. My work involved Oracle's Primavera Unifier — an outdated version with several integration issues.

The software relied on three separate databases, each with different formatting rules. Some allowed middle names or suffixes, while others did not. This caused discrepancies when users entered their full names differently across systems. Manually identifying mismatches across **14,000+ usernames** was nearly impossible.

---

### 💡 The Solution

To solve this, I created a Python script that:
- Compares first names, last names, middle names, and suffixes.
- Flags mismatches across multiple datasets.
- Processes over **14,000 entries in under 8 seconds** using **NumPy** and **Pandas**.

If the first and last names match, the tool checks the middle name. If the middle name mismatches, it highlights the field. Then it checks the suffix (e.g., "III"). If that also mismatches, it flags it. Otherwise, the entry is considered a match.

---

### 🖥️ GUI & Usability

After seeing how helpful the tool was, I built a simple **GUI** so that the team at BGE could continue using the tool after my internship ended. I also included a **user manual** with installation and usage instructions — available inside the ZIP folder with the project files.

---

### ⭐ Final Note

Thank you for your interest in the project.  
If you found it helpful, don’t forget to **star** the repo!

---


## 🧰 Tech Stack

- **Language**: Python
- **Libraries**: Pandas, NumPy, Tkinter (for GUI)
- **Interface**: CLI + GUI
- **Functionality**: File I/O, CSV processing, String matching


---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Ulugbek999/Username-comparison-tool.git
cd Username-comparison-tool
2. Install the zip archive with the file, and follow the installation requirements and steps listed in the User's manual.docx

python compare_usernames.py
Modify the script paths to match your CSV/text files.

```
---

##📂 File Structure

```text
Username-comparison-tool/
├── build/
│ └── pythonscript/
├── dist/
├── User's manual.docx
├── pythonscript.py # Main Python script with GUI and logic
├── pythonscript.spec # PyInstaller config (if used for creating .exe)
├── .gitattributes
└── README.md
```
---
🙌 Author
Bek (Ulugbek999)
Feel free to connect via GitHub or explore more of my work!

---
