# Performance Analyzer – Day 3 Challenge

## Problem Overview

This program analyzes student performance based on their internal assessment marks. It takes marks as input, stores them in a list, and processes each mark using a **for loop**. Based on the score, each student is classified into a performance category.

The program also counts:

* Total number of valid students
* Total number of failed students

A small personalization rule is included so that the program output changes based on the user’s name.

---

## Classification Rules

| Marks Range  | Category  |
| ------------ | --------- |
| 90 – 100     | Excellent |
| 75 – 89      | Very Good |
| 60 – 74      | Good      |
| 40 – 59      | Average   |
| 0 – 39       | Fail      |
| < 0 or > 100 | Invalid   |

---

## Personalization Logic

The program uses the **length of the user’s name** as a personalized condition.

* If the name length is **odd**, the program adds **1 grace mark** to each valid student’s score.
* The mark is capped at **100** if it exceeds the limit.

This makes the output slightly different for each user.

---

## Program Features

* Takes number of students as input
* Stores marks in a list
* Uses a for loop to process each mark
* Classifies performance using conditions
* Counts valid and failed students
* Displays final summary

---

## How to Run the Program

1. Run the Python file.
2. Enter the number of students.
3. Enter your name.
4. Enter the marks for each student.
5. The program will display the classification and final summary.

---

## Example Output

```
Enter number of students: 3
Enter your name: Rahul
Enter marks: 78
Enter marks: 45
Enter marks: 32

79 → Very Good
46 → Average
33 → Fail
Total Valid Students: 3
Total Failed Students: 1
```

*(Output may vary depending on name length due to personalization.)*

---

## Concepts Used

* for loop
* list
* conditional statements
* string handling
* user input
