import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def load_file_path(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def save_file_path(entry):
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def compare_files():
    file1_path = file1_entry.get()
    file2_path = file2_entry.get()
    output_file_path = output_file_entry.get()

    if not file1_path or not file2_path or not output_file_path:
        messagebox.showerror("Error", "Please provide all file paths")
        return

    try:
        file1_df = pd.read_excel(file1_path)
        file2_df = pd.read_csv(file2_path)

        active_file2_df = file2_df[file2_df['Status'] == 1].copy()

        active_file2_df['first name'] = active_file2_df['first name'].str.strip().str.lower()
        active_file2_df['last name1'] = active_file2_df['last name1'].str.strip().str.lower()
        active_file2_df['middle name'] = active_file2_df['middle name'].str.strip().str.lower()
        active_file2_df['last name2'] = active_file2_df['last name2'].str.strip().str.lower()

        file1_df['first name'] = file1_df['first name'].str.strip().str.lower()
        file1_df['last name1'] = file1_df['last name1'].str.strip().str.lower()
        file1_df['middle name'] = file1_df['middle name'].str.strip().str.lower()
        file1_df['last name2'] = file1_df['last name2'].str.strip().str.lower()

        active_file2_df.drop_duplicates(subset=['first name', 'last name1', 'middle name', 'last name2'], inplace=True)
        file1_df.drop_duplicates(subset=['first name', 'last name1', 'middle name', 'last name2'], inplace=True)

        merged_df = pd.merge(active_file2_df, file1_df, on=['first name', 'last name1'], suffixes=('_file2', '_file1'), how='outer', indicator=True)

        matchCounter = 0
        NoMatchCounter = 0
        missMatchCounter = 0

        def determine_match(row):
            nonlocal matchCounter, NoMatchCounter, missMatchCounter

            if row['_merge'] == 'left_only':
                NoMatchCounter += 1
                return 'No Match'
            if row['_merge'] == 'right_only':
                NoMatchCounter += 1
                return 'No Match'

            middle_name_match = (row['middle name_file2'] == row['middle name_file1']) or (pd.isna(row['middle name_file2']) and pd.isna(row['middle name_file1']))
            last_name2_match = (row['last name2_file2'] == row['last name2_file1']) or (pd.isna(row['last name2_file2']) and pd.isna(row['last name2_file1']))

            if middle_name_match and last_name2_match:
                matchCounter += 1
                return 'MATCH'
            else:
                missMatchCounter += 1
                return 'MISSMATCH'

        merged_df['Match_Status'] = merged_df.apply(determine_match, axis=1)

        merged_df.to_excel(output_file_path, index=False, sheet_name='Comparison_Result')

        results_text = f"Comparison completed. Results saved to {output_file_path}\n"
        results_text += f"Matches: {matchCounter}\nMissMatches: {missMatchCounter}\nNo Matches: {NoMatchCounter}"
        results_display.delete('1.0', tk.END)
        results_display.insert(tk.END, results_text)

        messagebox.showinfo("Success", results_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("File Comparison Tool")

# Create the GUI layout
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add disclaimer/note
note_label = ttk.Label(frame, text="Note: The files need to be in the correct format.\n"
                                   "Names of the users need to be separated into: 'first name', 'last name1', 'middle name', 'last name2'.\n"
                                   "This sorting tool only considers active users in File 2.",
                       foreground="red", wraplength=400)
note_label.grid(row=0, column=0, columnspan=3, pady=10)

ttk.Label(frame, text="File 1 Path:").grid(row=1, column=0, sticky=tk.W)
file1_entry = ttk.Entry(frame, width=50)
file1_entry.grid(row=1, column=1, padx=5)
ttk.Button(frame, text="Browse", command=lambda: load_file_path(file1_entry)).grid(row=1, column=2, padx=5)

ttk.Label(frame, text="File 2 Path:").grid(row=2, column=0, sticky=tk.W)
file2_entry = ttk.Entry(frame, width=50)
file2_entry.grid(row=2, column=1, padx=5)
ttk.Button(frame, text="Browse", command=lambda: load_file_path(file2_entry)).grid(row=2, column=2, padx=5)

ttk.Label(frame, text="Output File Path:").grid(row=3, column=0, sticky=tk.W)
output_file_entry = ttk.Entry(frame, width=50)
output_file_entry.grid(row=3, column=1, padx=5)
ttk.Button(frame, text="Save As", command=lambda: save_file_path(output_file_entry)).grid(row=3, column=2, padx=5)

ttk.Button(frame, text="Compare Files", command=compare_files).grid(row=4, column=0, columnspan=3, pady=10)

results_display = tk.Text(frame, height=10, width=70, wrap=tk.WORD)
results_display.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
