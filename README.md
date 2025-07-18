

# 🃏 21 Cards Trick – Python Console App

## 📋 Overview

The **21 Cards Trick** is a classic mind-reading game recreated in Python.
In this game, the computer shuffles and displays 21 random numbers (acting as cards) in 3 columns.
The player picks a card in their mind, and after asking **which column** it belongs to three times, the computer magically guesses the exact card!

---

## 🕹 How to Play

1. The program displays **21 random numbers in 3 columns**.
2. The player mentally chooses a number from the displayed set.
3. The player tells the program **which column (0, 1, or 2)** contains their chosen number.
4. The program rearranges the numbers and repeats this process **3 times**.
5. After the third round, the program **reveals the player's chosen card**.

---

## 🛠 How It Works

* The numbers are divided into 3 columns repeatedly.
* After each round, the selected column is moved to the middle.
* Using a simple mathematical positioning logic, after 3 iterations, the player’s card will always be in the **11th position (index 10)**.

---

## 🐍 Technologies Used

* Python 3
* `random` module for shuffling numbers
* Loops and conditionals for logic handling

---

## 💡 Key Concepts Practiced

* List manipulation
* Indexing and grouping logic
* User input handling with validation
* Iterative logic with predictable outcomes

---

## 🎯 Perfect For:

* Python beginners wanting to learn list logic
* Practicing interactive user input programs
* Magic trick fans who love programming!

---
