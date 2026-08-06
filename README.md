# Professional Django & Django REST Framework Course

Welcome to the **Professional Django & Django REST Framework (DRF) Course** repository.

This repository contains all the source code, examples, exercises, and documentation used throughout the course. It is designed to provide a structured learning path from Django fundamentals to building production-ready REST APIs with Django REST Framework.

---

# Repository Structure

```
.
├── docs/               # Course notes, theory, guides, and documentation
├── README.md           # Repository overview
└── .gitignore
```

> **Note:** The exact folder names may vary depending on the course section, but the overall organization follows the same structure.

---

# Documentation & Notes

All theoretical explanations, lecture notes, troubleshooting guides, and reference material are available inside the **`docs/`** directory.

This includes topics such as:

- Django fundamentals
- Django ORM
- Templates
- Forms
- Authentication
- Static & Media Files
- Django REST Framework
- Best Practices
- Common Errors & Solutions
- Additional reference material

Always check the documentation before moving on to a new topic.

---

# Source Code

The repository contains:

- Complete project source code
- Step-by-step examples
- Practice implementations
- Mini projects
- DRF examples
- Exercises completed during the course

Each section builds upon the previous one, so it is recommended to follow them in order.

---

# Virtual Environment

You will notice that the **virtual environment (`venv/`) is not included** in this repository.

This is intentional.

Virtual environments are machine-specific and should **never** be committed to Git. The `venv/` directory is excluded using **`.gitignore`**.

After cloning the repository, create your own virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

Then install the required packages:

```bash
pip install -r requirements.txt
```

---

# Recommended Learning Order

1. Read the notes in `docs/`
2. Follow the example code
3. Build the projects yourself
4. Complete the exercises
5. Experiment with your own modifications

Writing the code yourself is the best way to learn Django.

---

# Prerequisites

Before starting this course, you should have:

- Basic Python knowledge
- Python 3.x installed
- Git (recommended)
- Visual Studio Code (recommended)

No prior Django experience is required.

---

# Best Practices

- Always activate your virtual environment before working.
- Run migrations whenever models change.
- Commit your work regularly using Git.
- Read error messages carefully before making changes.
- Refer to the documentation whenever you encounter difficulties.

---

## Happy Learning!

This repository is intended to serve as a complete reference throughout the course. Take your time, explore the examples, practice consistently, and use the documentation whenever you need additional explanation.