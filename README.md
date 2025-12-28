# CLI-Based Expense Tracker

## Overview
A command-line application to track daily expenses using Python. Records expenses with date, category, and amount, storing data in a text file for persistence across sessions.

## Problem Statement
Provides a simple tool to track personal expenses without requiring databases or internet connectivity. Helps users monitor spending patterns through filtering and analysis features.

## Features

### Core Features
- **Add Expense** - Auto-generated ID, date (manual or today), category, amount, optional note
- **Delete Expense** - Remove records by ID
- **Update Expense** - Modify any field of existing expense
- **View All** - Display all recorded expenses
- **Filter by Category** - View expenses in specific categories
- **Filter by Date** - View expenses from a specific date
- **Calculate Total** - Sum of all expenses

### Additional Capabilities
- Auto-save after every change
- Auto-load on startup
- Input validation (dates, amounts, categories)
- Case-insensitive category search
- Handles missing files gracefully

## How to Run

### Requirements
- Python 3.x (no external libraries needed)

### Steps
1. Place all `.py` files in one directory
2. Run: `python exp_main.py`
3. Select menu options (1-8)
4. First run shows "No file found" - normal behavior
5. File `expenses.txt` created automatically when you add first expense

### Quick Start
```
Enter 1 → Add expense → Enter details → Saved!
Enter 4 → View all expenses
Enter 8 → Exit
```

## Project Structure
```
expense_tracker/
├── expense.py           # Expense class (data model)
├── exp_ops.py          # Core operations (add, delete, update, view, filter)
├── expfile_handler.py  # File save/load functions
├── exp_main.py         # Main program with menu
└── expenses.txt        # Data storage (auto-created)
```

### Module Breakdown

**`expense.py`** - Defines Expense class with attributes: exp_id, date, category, amount, optional_note

**`exp_ops.py`** - Contains all functions: add, view, filter (category/date), calculate total, delete, update

**`expfile_handler.py`** - Handles file operations: load_expenses(), save_expenses()

**`exp_main.py`** - Menu loop and user interaction

## Data Format

File: `expenses.txt` (pipe-separated)
```
1|2025-12-27|food|250.50|lunch
2|2025-12-28|travel|1500.00|cab fare
3|2025-12-28|rent|15000.00|monthly rent
```

## Concepts Applied

### 1. **Classes & Objects**
Created Expense class to encapsulate data. Learned how objects represent real-world entities.

### 2. **Modular Programming**
Split code into 4 modules (data, operations, file handling, main). Each module has single responsibility.

### 3. **Functions**
Separate function for each operation. Avoided code duplication.

### 4. **File Handling**
Read/write with `open()`. Handle FileNotFoundError. Used context managers (`with`).

### 5. **Lists**
Store multiple expense objects. Use append(), remove(), iteration.

### 6. **String Manipulation**
strip(), split(), f-strings, lower() for case-insensitive matching.

### 7. **Loops & Conditionals**
Menu loop (while True), input validation loops, if-elif chains for choices.

### 8. **Exception Handling**
try-except for ValueError, FileNotFoundError, invalid inputs. Prevent crashes.

### 9. **Type Conversion**
Convert strings from file/input to int/float with validation.

### 10. **Date/Time**
datetime module for current date, strftime() for formatting, strptime() for validation.

## Key Challenges & Solutions

**Challenge 1:** Module communication - passing data between files  
**Solution:** Import modules, use parameters to pass data

**Challenge 2:** load_expenses() returning None  
**Solution:** Return statement must be outside try-except block

**Challenge 3:** Inconsistent naming (exp.id vs exp.exp_id)  
**Solution:** Standardized to exp.exp_id everywhere

**Challenge 4:** Invalid input crashes  
**Solution:** while loops with try-except for validation

**Challenge 5:** When to save data  
**Solution:** Load once at start, save after every change

## What I Learned

**Main Takeaway:** Modular structure makes debugging easier. When code is organized by responsibility, finding bugs is straightforward.

**Key Skills:**
- Breaking large problems into smaller modules
- Understanding data flow between components
- Input validation and error handling
- File-based persistence
- User-friendly error messages

**Compared to Previous Project (Student Management):**
- More complex: multiple modules instead of one file
- Better organization: separation of concerns
- More robust: comprehensive exception handling
- Better UX: case-insensitive search, date flexibility

## Future Improvements

- Date range filtering (from date X to date Y)
- Monthly/category-wise spending analysis
- Budget tracking with alerts
- Export to CSV
- Data backup feature

## Technical Notes

- Uses sequential IDs (1, 2, 3...)
- Date format: YYYY-MM-DD
- Modular design avoids circular imports
- No database - plain text for simplicity
- Educational project demonstrating Python fundamentals

---

**Course:** AI/ML Introduction | **Focus:** Python Fundamentals  
**Key Concepts:** OOP, Modules, File I/O, Exception Handling, Input Validation
