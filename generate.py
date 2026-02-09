from datetime import datetime
import os
import random

topics = {
    "Frontend": [
        "HTML Fundamentals",
        "CSS Flexbox",
        "CSS Grid",
        "JavaScript Basics",
        "DOM Manipulation",
        "React Basics",
    ],
    "Backend": [
        "Node.js Basics",
        "Express.js Fundamentals",
        "REST API Design",
        "JWT Authentication",
        "MVC Architecture",
    ],
    "Database": [
        "SQL Basics",
        "MySQL Joins",
        "MongoDB Basics",
        "Indexes in Databases",
    ],
    "Programming": [
        "Java Basics",
        "Python Functions",
        "Arrays in Java",
        "Object-Oriented Programming",
    ],
    "Cyber Security": [
        "Cyber Security Basics",
        "SQL Injection",
        "XSS Attacks",
        "Authentication vs Authorization",
    ],
    "DSA": [
        "Data Structures Introduction",
        "Arrays and Strings",
        "Linked List Basics",
        "Stack and Queue",
    ],
}

today = datetime.now().strftime("%Y-%m-%d")

category = random.choice(list(topics.keys()))
topic = random.choice(topics[category])

content = f"""
# 📘 Daily Learning Log – {today}

## 🧩 Category
{category}

## 🧠 Topic
{topic}

## ✍️ What I Learned
Today I studied **{topic}** under **{category}** and understood its core concepts.

## 💻 Code Example
```python
print("Learning every day!")