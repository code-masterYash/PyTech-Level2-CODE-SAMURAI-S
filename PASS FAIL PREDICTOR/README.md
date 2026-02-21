Problem Chosen

Problem 7: Pass/Fail Predictor (ML – Classification)

The objective of this project is to predict whether a student passes or fails based on their academic performance in three subjects: Math, Science, and English.

The system:

Reads student marks from a dataset

Creates a target output:

Pass → if average score ≥ 40

Fail → if average score < 40

Splits the dataset into 80% training and 20% testing

Uses classification logic to evaluate accuracy

Predicts the result for new student inputs using a menu-driven program

This project is implemented as a modular Python mini-application using Object-Oriented Programming and file handling.

📂 Dataset Source

The dataset is a student performance dataset stored locally in a file named:

data.txt
Dataset Details:

The dataset contains student marks in:

Math

Science

English

The data is written manually / sourced from publicly available student-marks datasets (such as Kaggle) and formatted into a simple text file.

No data is hardcoded inside the Python program.

The dataset is loaded using file handling as per Level-2 rules.

Sample Format (data.txt):
math,science,english
78,82,75
35,38,40
90,92,88
22,30,28
▶️ How to Run the Project
Step 1: Project Structure

Ensure your project folder is structured exactly as below:

pass_fail_predictor/
│
├── main.py
├── model.py
└── data.txt
Step 2: Open Terminal / Command Prompt

Navigate to the project folder:

cd pass_fail_predictor
Step 3: Run the Application

Execute the program using:

python main.py
Step 4: Use the Menu

When the program runs, the following menu appears:

===== Pass / Fail Predictor =====
1. Train Model
2. Predict Result
3. Exit

Option 1 → Trains the model and displays accuracy

Option 2 → Predicts Pass/Fail for user-entered marks

Option 3 → Exits the program safely

The program handles invalid inputs gracefully and does not crash.
