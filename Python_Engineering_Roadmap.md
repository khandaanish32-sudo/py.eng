# 🐍 The Complete Python Roadmap for 1st-Year Engineering Students
*Inspired by structured developer paths like [roadmap.sh](https://roadmap.sh/python), tailored for real-world campus & engineering challenges.*

---

## 🗺️ High-Level Learning Architecture

```
[Phase 0: Setup & Tooling] 
       │
       ▼
[Phase 1: Basics & Logic] ──────► 🛠️ Mini-Project 1: Smart Attendance & Grade Predictor
       │
       ▼
[Phase 2: Data Structures] ─────► 🛠️ Mini-Project 2: Hostel Pocket-Money & Mess Tracker
       │
       ▼
[Phase 3: Files, Errors & OOP] ─► 🛠️ Mini-Project 3: Lab Equipment & Book Lending System
       │
       ▼
[Phase 4: Libraries & UI] ──────► 🛠️ Mini-Project 4: Live Academic Analytics Dashboard
       │
       ▼
🚀 GRAND CAPSTONE PROJECT: "UniLife 360" (Combining Mini-Projects 1 + 2 + 3 + 4)
```

---

## 🏁 Phase 0: The Launchpad (Installation & Setup)
Before writing code, you need to set up a professional developer workspace on your laptop.

### Topic 0.1: Installing Python
1. **Download:** Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest stable version of Python (Python $3.12+$).
2. **Crucial Installation Step (Windows):** Run the installer and **CHECK THE BOX** that says `"Add python.exe to PATH"` before clicking "Install Now".
3. **Mac/Linux Users:** Open your terminal and run `python3 --version` (macOS via Homebrew: `brew install python`).
4. **Verify Installation:**
   * Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux).
   * Type `python --version` (or `python3 --version`) and press Enter.
   * Type `pip --version` to verify the package manager is installed.

### Topic 0.2: Setting Up Your Code Editor (VS Code)
1. Download and install **[Visual Studio Code](https://code.visualstudio.com/)**.
2. Open VS Code, click on the **Extensions** icon on the left sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`).
3. Search for and install the official **Python** extension by Microsoft.
4. Create a folder on your computer named `Python_Engineering_Journey` and open it inside VS Code.

### 📝 Phase 0 Assignment: "The Digital Student ID Card"
* **Problem Statement:** Every engineering student gets an ID card in their first week. Create a file named `id_card.py` and use pure `print()` statements to display a formatted ASCII-art ID card in your terminal showing your Name, Roll Number, Branch, Blood Group, and Hostel/Day Scholar status.
* **Goal:** Get comfortable creating `.py` files, saving them, and running them via the terminal (`python id_card.py`).

---

## 🧱 Phase 1: Python Basics & Logic Building (Weeks 1–3)
*Goal: Understand how a computer stores data, calculates formulas, makes decisions, and repeats tasks.*

### Topic 1.1: Variables, Data Types & Typecasting
* **Concepts to Learn:**
  * Variables and naming conventions (`snake_case`).
  * Primitive types: Integers (`int`), Floating-point numbers (`float`), Strings (`str`), Booleans (`bool`).
  * Checking types with `type()` and converting types with `int()`, `float()`, `str()`.
* **📝 Assignment 1.1: The Physics Lab Unit Converter**
  * **Real-World Challenge:** In your 1st-year Physics or Basic Electrical Lab, readings are often taken in one unit and need conversion for lab manuals.
  * **Task:** Write a script that stores fixed test values for temperature in Celsius ($C$), length in millimeters ($mm$), and resistance in Ohms ($\Omega$), then converts and prints them into Kelvin ($K = C + 273.15$), meters ($m = \frac{mm}{1000}$), and Kilo-ohms ($k\Omega = \frac{\Omega}{1000}$) with proper data types.

### Topic 1.2: Input/Output & Operators
* **Concepts to Learn:**
  * Taking user input with `input()` and formatting output using **f-strings** (`f"Result: {value:.2f}"`).
  * Arithmetic operators (`+`, `-`, `*`, `/`, `//` floor division, `%` modulus, `**` exponentiation).
  * Comparison (`==`, `!=`, `>`, `<`, `>=`, `<=`) and Logical operators (`and`, `or`, `not`).
* **📝 Assignment 1.2: Late-Night Canteen Bill Splitter**
  * **Real-World Challenge:** You and your hostel friends order food at 2 AM, including delivery charges and GST, and nobody wants to do mental math.
  * **Task:** Ask the user for the total food amount, GST percentage, delivery fee, and number of friends. Calculate the total payable amount and exact share per person rounded to $2$ decimal places. Also, use the modulus operator (`%`) to show if any remainder rupees are left over.

### Topic 1.3: Control Flow (Conditionals)
* **Concepts to Learn:**
  * Decision making with `if`, `elif`, and `else`.
  * Nested `if` statements.
  * Truthy and Falsy values in Python.
* **📝 Assignment 1.3: The $75\%$ Attendance Detention Alert**
  * **Real-World Challenge:** Most engineering colleges enforce a strict $75\%$ attendance policy to sit for end-semester exams.
  * **Task:** Ask the student for total classes held and total classes attended. Calculate the current attendance percentage:
    $$\text{Attendance \%} = \left(\frac{\text{Classes Attended}}{\text{Classes Held}}\right) \times 100$$
  * **Conditions:**
    * $\ge 85\%$: Print *"Safe Zone! You can afford to skip a class for hackathon prep."*
    * $75\%$ to $84.99\%$: Print *"Warning Zone! Attend classes regularly."*
    * $< 75\%$: Ask if the student has a valid medical certificate (`yes`/`no`). If `yes` and attendance is $\ge 65\%$, print *"Condonation Eligible"*; otherwise, print *"Detention Alert!"*.

### Topic 1.4: Loops (`for` and `while`)
* **Concepts to Learn:**
  * `while` loops (condition-controlled) and infinite loop traps.
  * `for` loops with `range(start, stop, step)`.
  * Loop control statements: `break`, `continue`, and `pass`.
* **📝 Assignment 1.4: The Bunk & Recovery Simulator**
  * **Real-World Challenge:** When your attendance drops below $75\%$, you always wonder: *"How many consecutive classes must I attend to reach $75\%$ again?"*
  * **Task:** Take `classes_held` and `classes_attended` as input. If attendance is below $75\%$, use a `while` loop that increments both `classes_held` and `classes_attended` by $1$ on each iteration until the percentage reaches $\ge 75\%$. Print out the exact number of consecutive classes the student needs to attend.

---

### 🛠️ Phase 1 Mini-Project: Smart Academic & Attendance Assistant (CLI)
> **Combining Topics 1.1 + 1.2 + 1.3 + 1.4**
* **Problem Statement:** 1st-year students struggle to figure out how internal assessment marks (Mid-terms, Quizzes, Assignments) translate to the marks they need in the final End-Semester exam to pass or get an 'A' grade, alongside tracking attendance eligibility.
* **Features to Build:**
  1. A continuous menu-driven loop (`while True`) with options:
     * `[1] Check Attendance Status & Bunk Margin` (Calculates either how many classes you must attend to hit $75\%$, OR how many classes you can safely skip while staying above $75\%$).
     * `[2] End-Sem Target Score Predictor` (Takes Internal Marks out of $50$, asks desired Grade like S/A/B/C, and calculates minimum marks required out of $100$ in the End-Sem exam).
     * `[3] Basic Engineering Formula Solver` (Ohm's Law $V = I \cdot R$ and Quadratic Roots).
     * `[4] Exit`.

---

## 📦 Phase 2: Data Structures & Modular Code (Weeks 4–6)
*Goal: Store collections of items (like marks of 6 subjects or 50 expenses) and organize your code into reusable blocks.*

### Topic 2.1: Lists & Tuples
* **Concepts to Learn:**
  * Creating, indexing, and slicing lists (`my_list[0:3]`).
  * List methods: `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`.
  * List comprehensions (basic introduction).
  * Tuples: Immutability and when to use tuples over lists (e.g., fixed coordinates or subject codes).
* **📝 Assignment 2.1: Semester Lab Marks Analyzer**
  * **Real-World Challenge:** You have $10$ weekly lab evaluations, and the professor announces that the "best $8$ out of $10$" marks will be considered for final grading.
  * **Task:** Store $10$ lab marks in a list. Sort the list, drop the lowest $2$ scores, and calculate the average, highest, and lowest of the remaining $8$ scores without modifying the original raw backup tuple.

### Topic 2.2: Dictionaries & Sets
* **Concepts to Learn:**
  * Key-Value pairs in Dictionaries (`dict`), accessing values safely with `.get()`, iterating with `.items()`.
  * Nested dictionaries.
  * Sets (`set`): Unordered unique elements, set operations (Union `|`, Intersection `&`, Difference `-`).
* **📝 Assignment 2.2: Tech-Fest Club Registration De-duplicator**
  * **Real-World Challenge:** During college fest registrations, students accidentally submit Google Forms multiple times, and organizers want to know which students registered for *both* the Coding Club and Robotics Club.
  * **Task:**
    1. Take two lists of student roll numbers (with duplicates) for `coding_club` and `robotics_club`.
    2. Convert them to Sets to remove duplicates.
    3. Find: (a) Total unique participants across both clubs, (b) Students in *both* clubs, and (c) Students *only* in the Coding Club.
    4. Store student details (`Roll_No: {"name": ..., "branch": ...}`) in a dictionary and allow lookup by Roll Number.

### Topic 2.3: Strings & String Manipulation
* **Concepts to Learn:**
  * String indexing, slicing, and immutability.
  * String methods: `.strip()`, `.split()`, `.join()`, `.upper()`, `.lower()`, `.replace()`, `.startswith()`, `.isdigit()`.
* **📝 Assignment 2.3: University Roll Number & Official Email Parser**
  * **Real-World Challenge:** Engineering roll numbers encode hidden metadata (e.g., `26CS1045` means Batch `2026`, Branch `CS`, Roll `1045`).
  * **Task:** Write a script that accepts a student's roll number and college email ID. Validate that the email ends with `.edu` or `.ac.in`, extract the admission year, branch code, and unique serial number using string slicing, and print a decoded profile summary.

### Topic 2.4: Functions, Scope & Modules
* **Concepts to Learn:**
  * Defining functions with `def`, parameters vs. arguments, default parameters, and `return` values.
  * Returning multiple values from a function.
  * Local vs. Global variable scope.
  * Importing built-in modules (`math`, `random`, `os`).
* **📝 Assignment 2.4: Modular SGPA Calculator Engine**
  * **Real-World Challenge:** Calculating Semester Grade Point Average (SGPA) requires weighted averages based on course credits ($4$-credit theory vs. $1.5$-credit labs).
  * **Task:** Create clean, reusable functions:
    * `marks_to_grade_point(marks)`: Converts marks ($0\text{--}100$) to Grade Points ($0\text{--}10$).
    * `calculate_sgpa(credits_list, grade_points_list)`: Computes:
      $$\text{SGPA} = \frac{\sum_{i=1}^{n} (C_i \times G_i)}{\sum_{i=1}^{n} C_i}$$
    * Call these functions inside a `main()` function for a $6$-subject semester.

---

### 🛠️ Phase 2 Mini-Project: Hostel Pocket-Money & Mess Expense Tracker
> **Combining Topics 2.1 + 2.2 + 2.3 + 2.4**
* **Problem Statement:** Living away from home (or managing daily commute expenses) makes it super easy to run out of allowance by the 20th of the month without knowing where the money went.
* **Features to Build:**
  1. Store each expense as a dictionary inside a master list:
     `{"date": "2026-11-08", "category": "Food", "description": "Maggi & Chai", "amount": 60.0}`
  2. **Modular Functions:**
     * `add_expense()`: Validates category (`Food`, `Stationery`, `Travel`, `Photocopy`, `Misc`) using sets/strings.
     * `view_summary_by_category()`: Uses a dictionary to sum up spending per category.
     * `check_budget_alert(monthly_allowance)`: Warns if total spending crosses $80\%$ of allowance.
     * `search_expenses(keyword)`: Searches descriptions using string methods (`.lower()`).

---

## 🗂️ Phase 3: File Handling, Error Management & OOP (Weeks 7–9)
*Goal: Make sure your data doesn't vanish when you close the terminal, prevent your program from crashing on bad input, and structure code like real software engineers.*

### Topic 3.1: Exception Handling
* **Concepts to Learn:**
  * Syntax errors vs. Runtime exceptions (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `KeyError`).
  * `try`, `except`, `else`, and `finally` blocks.
  * Raising custom errors with `raise ValueError("...")`.
* **📝 Assignment 3.1: Crash-Proof Lab Data Entry Terminal**
  * **Real-World Challenge:** When entering $50$ readings from an experiment, accidentally typing `"12.5a"` instead of `"12.5"` crashes a beginner's Python script and loses all previous readings!
  * **Task:** Write an input loop that collects numerical voltage and current readings. Use `try-except` so that if a user types letters, negative resistance, or $0$ for current (when dividing $R = \frac{V}{I}$), the program catches the error gracefully, prints a helpful warning, and asks for that reading again without crashing.

### Topic 3.2: File Handling (`.txt`, `.csv`, `.json`)
* **Concepts to Learn:**
  * Reading and writing text files using context managers (`with open("file.txt", "r") as f:`).
  * File modes: `'r'`, `'w'`, `'a'`.
  * Working with CSV files (`import csv`) and JSON files (`import json` -> `json.load()`, `json.dump()`).
* **📝 Assignment 3.2: Persistent Expense & Attendance Logger**
  * **Real-World Challenge:** In Phase 1 and Phase 2, every time you closed the program, your attendance and expense records were wiped from RAM.
  * **Task:** Upgrade your Phase 2 Expense Dictionary so that every time an expense is added, it automatically saves to `expenses.json`, and every time the program starts, it loads existing data from `expenses.json`. Also add an `"Export to CSV"` feature so the file can be opened in Microsoft Excel or Google Sheets.

### Topic 3.3: Object-Oriented Programming (OOP) Fundamentals
* **Concepts to Learn:**
  * Why OOP? Moving from procedural functions to real-world entities.
  * Classes and Objects (Instances).
  * The `__init__()` constructor and the `self` keyword.
  * Instance attributes vs. Class attributes; Instance methods.
  * String representation with `__str__()`.
* **📝 Assignment 3.3: Modeling `Student` and `Course` Blueprints**
  * **Real-World Challenge:** A college ERP system manages thousands of students and courses.
  * **Task:** Create a `Student` class with attributes `name`, `roll_no`, `branch`, and `attendance_record` (a dictionary), along with methods like `mark_present(subject)`, `mark_absent(subject)`, and `get_attendance_percentage(subject)`. Create $3$ different student objects and test their methods.

### Topic 3.4: Advanced OOP Pillars
* **Concepts to Learn:**
  * **Encapsulation:** Private/Protected attributes (`_variable`, `__variable`) and getter/setter methods.
  * **Inheritance:** Parent and Child classes (`super().__init__()`).
  * **Polymorphism:** Method overriding.
* **📝 Assignment 3.4: Robotics Lab Inventory Hierarchy**
  * **Real-World Challenge:** Your college Innovation/Robotics Lab lends out microcontrollers (Arduino, Raspberry Pi), sensors, and mechanical tools, each having different lending rules.
  * **Task:**
    1. Create a base class `LabItem(item_id, name, is_available)`.
    2. Create two child classes inheriting from `LabItem`:
       * `ElectronicComponent` (adds `voltage_rating`, `is_fragile`).
       * `BookResource` (adds `author`, `isbn`, `max_borrow_days`).
    3. Use encapsulation so `__is_available` cannot be modified directly without calling `.checkout(student_roll)` or `.return_item()`.

---

### 🛠️ Phase 3 Mini-Project: Department Library & Hardware Lab Lending Manager
> **Combining Topics 3.1 + 3.2 + 3.3 + 3.4**
* **Problem Statement:** Student club leads and lab assistants still use messy paper registers to track who borrowed an Arduino board, a multimeter, or a reference textbook—leading to lost equipment before exams and hackathons.
* **Features to Build:**
  1. **OOP Architecture:** Classes for `Item` (Base), `HardwareKit` (Child), `ReferenceBook` (Child), and `LendingManager`.
  2. **Features:**
     * Add new lab equipment or books to inventory.
     * Issue an item to a student (records Roll Number, Issue Date, and Due Date).
     * Return an item and automatically calculate a late fine ($\text{Rs. } 10/\text{day}$ after $7$ days).
     * List all overdue or currently borrowed items.
  3. **Persistence & Safety:** Save/load the entire inventory state using a `.json` file and wrap all user inputs and file operations in `try-except` blocks.

---

## 🌐 Phase 4: The Python Ecosystem, APIs & UI (Weeks 10–12)
*Goal: Tap into Python's superpower—third-party libraries—to automate tasks, analyze data, and build a visual web dashboard.*

### Topic 4.1: Virtual Environments & `pip`
* **Concepts to Learn:**
  * Why virtual environments matter (avoiding package version conflicts).
  * Creating and activating a `venv`:
    * `python -m venv venv`
    * Windows: `venv\Scripts\activate` | Mac/Linux: `source venv/bin/activate`
  * Installing packages with `pip install <package>` and generating `requirements.txt` (`pip freeze > requirements.txt`).
* **📝 Assignment 4.1: Beautifying Your Terminal Output**
  * **Task:** Create a virtual environment, install the `rich` or `tabulate` library via `pip`, and convert one of your boring black-and-white terminal outputs from Phase 2 into a color-coded, neatly bordered table. Export your `requirements.txt`.

### Topic 4.2: Working with Dates, Time & External APIs (`requests`)
* **Concepts to Learn:**
  * Built-in `datetime` module (calculating days remaining until exams, formatting timestamps).
  * How the Web works: HTTP `GET` requests, Status Codes ($200$, $404$), and JSON responses.
  * Using the `requests` library to fetch live data from free public APIs.
* **📝 Assignment 4.2: Live Coding Contest & Study Quote Fetcher**
  * **Real-World Challenge:** Engineering students want a quick morning terminal script that shows how many days are left until End-Sem exams alongside a live motivational quote or weather forecast before walking to the academic block.
  * **Task:** Write a script using `datetime` to show a countdown to your exam date, and use `requests.get()` to fetch a random programming quote or trivia from a free public API (handle internet disconnection errors using `try-except requests.exceptions.RequestException`).

### Topic 4.3: Data Analysis & Visualization (`pandas` & `matplotlib`)
* **Concepts to Learn:**
  * Reading CSV files into a Pandas `DataFrame` (`pd.read_csv()`).
  * Basic DataFrame operations: `.head()`, `.describe()`, filtering rows, grouping with `.groupby()`.
  * Plotting charts with `matplotlib.pyplot`: Line charts, Bar charts, and Pie charts.
* **📝 Assignment 4.3: Visualizing Your Semester Spending & Marks**
  * **Real-World Challenge:** Looking at raw rows of numbers in a CSV file doesn't show you trends—visual charts immediately reveal if your food expenses spike during exam week!
  * **Task:** Load your `expenses.csv` (from Phase 3) using `pandas`. Generate and save two plots as `.png` images using `matplotlib`:
    1. A **Pie Chart** showing percentage breakdown of expenses by category.
    2. A **Bar Chart** comparing your Mid-Term 1 vs. Mid-Term 2 marks across all $6$ subjects.

### Topic 4.4: Building an Interactive Web App (`Streamlit`)
* **Concepts to Learn:**
  * Why `Streamlit`? It lets you turn pure Python scripts into modern, shareable web apps in minutes without needing HTML, CSS, or JavaScript.
  * Core widgets: `st.title()`, `st.sidebar`, `st.number_input()`, `st.selectbox()`, `st.button()`, `st.dataframe()`, `st.pyplot()`.
* **📝 Assignment 4.4: Web-Based SGPA & Attendance Calculator**
  * **Task:** Install `streamlit` (`pip install streamlit`) and take your Phase 1/Phase 2 CLI SGPA & Attendance functions and wrap them in a clean Streamlit web interface with sliders and interactive metric cards (`st.metric()`). Run it in your browser using `streamlit run app.py`.

---

### 🛠️ Phase 4 Mini-Project: Live Student Productivity & Analytics Dashboard
> **Combining Topics 4.1 + 4.2 + 4.3 + 4.4**
* **Problem Statement:** Command-line tools are great for learning, but real users want an interactive visual dashboard where they can see exam countdowns, study timer logs, and visual charts of their academic and financial health.
* **Features to Build:**
  1. A multi-tab **Streamlit Web App** running inside a virtual environment.
  2. **Live Header:** Displays days left until End-Sem exams (`datetime`) and a live daily quote fetched via `requests`.
  3. **Visual Analytics:** Uploads or reads CSV logs of study hours / expenses using `pandas` and displays interactive bar and pie charts using `matplotlib`.

---

## 🚀 Phase 5: The Grand Capstone Project (Weeks 13–14)
*Goal: Combine every concept and unite all four mini-projects into a single, modular, portfolio-worthy software product.*

### 🏆 Capstone Project: **UniLife 360 — The 1st-Year Engineering Companion Suite**

#### 🎯 The Real-World Problem Statement
First-year engineering students juggle multiple disconnected problems daily: maintaining $75\%$ attendance across $6\text{--}8$ subjects, predicting SGPA/CGPA, managing tight monthly hostel allowances, and tracking borrowed lab equipment or library books before due dates. Currently, students use random apps, messy notebooks, or guesswork for each of these.

**Your Mission:** Build **UniLife 360**, a unified, modular Python application (with both CLI and Streamlit Web Dashboard interfaces) that integrates all four of your previous mini-projects into one cohesive software architecture.

---

#### 🧩 How Your Previous Mini-Projects Combine Into "UniLife 360"

```
                  ┌──────────────────────────────────────────┐
                  │       UNILIFE 360 (Main Dashboard)       │
                  │    Built with Streamlit / Modular OOP    │
                  └────────────────────┬─────────────────────┘
                                       │
       ┌───────────────────────┬───────┴───────────────┬───────────────────────┐
       ▼                       ▼                       ▼                       ▼
┌──────────────┐       ┌──────────────┐        ┌──────────────┐        ┌──────────────┐
│  MODULE 1:   │       │  MODULE 2:   │        │  MODULE 3:   │        │  MODULE 4:   │
│  Attendance  │       │ Hostel & Mess│        │ Lab & Book   │        │  Visual Data │
│  & Academic  │       │   Finance    │        │  Borrowing   │        │  Analytics & │
│   Engine     │       │   Manager    │        │   Tracker    │        │  Exam Timer  │
│ (From MP #1) │       │ (From MP #2) │        │ (From MP #3) │        │ (From MP #4) │
└──────┬───────┘       └──────┬───────┘        └──────┬───────┘        └──────┬───────┘
       │                      │                       │                       │
       └──────────────────────┴───────────┬───────────┴───────────────────────┘
                                          ▼
                         ┌─────────────────────────────────┐
                         │   Persistent Storage Layer      │
                         │ (JSON / CSV Files + Exceptions) │
                         └─────────────────────────────────┘
```

#### 📁 Recommended Project Folder Structure
Organize your Capstone project like a real software engineer:

```text
unilife_360/
│
├── venv/                        # Virtual Environment (Phase 4.1)
├── data/                        # Persistent Storage (Phase 3.2)
│   ├── attendance.json
│   ├── expenses.csv
│   └── borrowed_items.json
│
├── modules/                     # Modular OOP & Functions (Phase 2.4 & 3.3)
│   ├── __init__.py
│   ├── academic_manager.py      # Evolved from Mini-Project 1
│   ├── finance_tracker.py       # Evolved from Mini-Project 2
│   ├── lending_tracker.py       # Evolved from Mini-Project 3
│   └── api_utils.py             # Evolved from Mini-Project 4
│
├── app.py                       # Main Streamlit Web UI Entry Point (Phase 4.4)
├── cli_main.py                  # Optional Terminal Interface
├── requirements.txt             # Dependencies list
└── README.md                    # Documentation for your GitHub profile
```

#### ✅ Core Checklist to Complete the Capstone
1. **Academic & Attendance Module (`academic_manager.py`):**
   * Track subject-wise classes held vs. attended.
   * Color-coded warnings for subjects below $75\%$ and exact calculation of classes needed to recover.
   * SGPA & Target End-Sem Score calculator.
2. **Hostel Finance Module (`finance_tracker.py`):**
   * Log daily expenses with date, category, and payment mode (`UPI` / `Cash`).
   * Monthly budget progress bar and alert when spending exceeds $80\%$.
3. **Lab & Library Due-Date Module (`lending_tracker.py`):**
   * Track borrowed library books or lab hardware kits with issue date and return deadline.
   * Automatic overdue fine estimator using `datetime`.
4. **Analytics & Live Dashboard (`app.py`):**
   * Built with Streamlit.
   * Visual charts (`matplotlib` / `pandas`) for attendance per subject and monthly spending breakdown.
   * Exam countdown timer and export-to-CSV button.

---

## 💡 Golden Rules for 1st-Year Students Following This Roadmap
1. **No Copy-Pasting From AI:** When solving the assignments after each topic, type every single line of code yourself. Making syntax errors and reading error tracebacks is how your brain builds programming muscle memory.
2. **Push Every Mini-Project to GitHub:** Create a free [GitHub](https://github.com/) account in Week 2. By the end of your 1st year, having $4$ mini-projects and $1$ complete Capstone project on your GitHub profile will put you ahead of $90\%$ of your peers when applying for internships in 2nd year.
3. **Customize for Your College:** Adjust the grading scale ($10$-point SGPA formulas) and attendance rules ($75\%$ vs. $80\%$) in the projects to match your specific university's regulations—your hostel friends might actually start using your app!