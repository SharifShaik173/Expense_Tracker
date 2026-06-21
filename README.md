# 💰 Expense Tracker
 
A simple command-line **Expense Tracker** built in Python. It lets you log your monthly salary and expenses (food, shopping, travelling, electricity bill, and extra activities), automatically calculates your remaining balance, and stores everything in a CSV file for future reference and editing.
 
## ✨ Features
 
- Add a new user's monthly salary and expense details
- Automatically calculates total monthly expenses and remaining balance
- Generate a full text report of your finances
- Retrieve and view an existing user's saved data
- Update/increase any individual expense category or salary for an existing record
- Persists all data locally in `expense_tracker.csv`
- Prevents duplicate entries (same name + salary combination)
## 📁 Project Structure
 
```
expense-tracker/
├── Expense_tracker_Project.py   # Main application script
├── expense_tracker.csv          # Data file (auto-created/updated on first run)
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```
 
## 🛠️ Requirements
 
- Python 3.6 or higher
- No external/third-party packages — the project only uses Python's built-in `csv` and `datetime` modules
See [`requirements.txt`](requirements.txt) for details.
 
## 🚀 Installation
 
1. Clone the repository:
```bash
   git clone https://github.com/<your-username>/expense-tracker.git
   cd expense-tracker
```
2. (Optional) Create a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
```
3. No additional packages are required to run this project.
## ▶️ Usage
 
Run the script from your terminal:
 
```bash
python Expense_tracker_Project.py
```
 
You'll see a menu with the following options:
 
```
---------------------Expense Tracker--------------------------------
1.Add your Details
2.Get Existing Details
3.Exit
```
 
### 1. Add your Details
Enter your name, salary, and monthly expenses (food, shopping, travelling, electricity bill, extra activities). The app calculates your balance and saves the record to `expense_tracker.csv`. You can then:
- Generate a full report
- View total monthly expenses
- View remaining salary/balance
### 2. Get Existing Details
Enter your name and salary to look up a previously saved record. From here you can:
- Generate a report
- View total monthly expenses
- View remaining balance
- Update/increase any expense category or your salary
### 3. Exit
Closes the application.
 
## 📊 CSV Data Format
 
Data is stored in `expense_tracker.csv` with the following columns:
 
| Column | Description |
|---|---|
| `name` | Name of the user |
| `salary` | Monthly salary |
| `food` | Monthly food expense |
| `shopping` | Monthly shopping expense |
| `travelling` | Monthly travelling expense |
| `electricity_bill` | Monthly electricity bill |
| `extra_activities` | Monthly extra/miscellaneous expense |
| `remaining_balance` | Salary minus total expenses |
| `datetime` | Timestamp of the last update |
 
## 🧩 Example
 
```
Choose an Option: 1
enter name: Alex
enter monthly salary: 50000
enter food monthly expenses: 5000
enter monthly shopping expenses: 2000
enter monthly travelling expenses: 1500
enter electricity monthly bill expenses: 1000
enter your extra monthly expenses: 1500
details added successfully
```
 
## 🔮 Possible Future Improvements
 
- Replace nested `while`/`if` input validation with cleaner exception-based handling
- Add support for multiple records per user (monthly history instead of overwrite)
- Add data visualization (charts of expenses by category)
- Migrate storage to SQLite for more reliable lookups and updates
- Add unit tests
## 📄 License
 
This project is open source and available
