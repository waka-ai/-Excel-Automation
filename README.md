

# 📊 Excel Sales Data Processor

A simple and efficient Python tool that processes Excel files and performs automated calculations on structured data.

This script reads an Excel file, calculates totals based on quantity and price, and saves a new processed Excel file with the computed results.

---

## 🚀 Features

* Reads Excel (`.xlsx`) files
* Automatically calculates totals (`Quantity × Price`)
* Adds a new **Total** column
* Saves a processed output file
* Clean and easy-to-modify code

---

## 🛠 Tech Stack

* Python 3.x
* [pandas](https://pandas.pydata.org/)
* openpyxl (used internally by pandas for Excel handling)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/excel-data-processor.git
cd excel-data-processor
```

Install required dependencies:

```bash
pip install pandas openpyxl
```

---

## ▶️ Usage

Make sure your Excel file contains at least the following columns:

* `Quantity`
* `Price`

Example:

| Product | Quantity | Price |
| ------- | -------- | ----- |
| Item A  | 10       | 5     |
| Item B  | 3        | 20    |

Run the script:

```bash
python excel_processor.py
```

Or modify the input file name in the script:

```python
process_excel("sales_data.xlsx")
```

---

## 📄 Output

The script generates a new file:

```
sales_data_processed.xlsx
```

With an additional column:

| Product | Quantity | Price | Total |
| ------- | -------- | ----- | ----- |
| Item A  | 10       | 5     | 50    |
| Item B  | 3        | 20    | 60    |

---

## ⚙️ How It Works

1. Reads the Excel file using `pandas.read_excel()`
2. Multiplies `Quantity` and `Price`
3. Creates a new column called `Total`
4. Saves the updated DataFrame to a new Excel file

---

## ⚠️ Requirements & Assumptions

* Input file must be in `.xlsx` format
* Columns must be named exactly:

  * `Quantity`
  * `Price`
* Data should be numeric (no text in numeric fields)

---

## 🔧 Customization Ideas

You can extend this project by:

* Adding tax calculation
* Adding discount logic
* Creating monthly sales summaries
* Adding data validation
* Adding charts (matplotlib / Excel charts)
* Supporting CSV input/output
* Adding CLI arguments with `argparse`
* Creating a GUI version (Tkinter / Streamlit)

---

## 💼 Use Cases

* Sales reporting automation
* Invoice preparation
* Inventory management
* Small business accounting tasks
* Data preprocessing before analysis

---

## 📄 License

MIT License — Free to use and modify.

