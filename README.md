# NumPy Practice – Clinical Data Processing

## Overview

This repository contains my practice exercises while learning **NumPy** for scientific computing and data analysis.

The exercises are based on simulated patient data and focus on core NumPy concepts commonly used in healthcare analytics, machine learning, and scientific programming.

---

## Learning Objectives

The goal of this project is to develop practical skills in:

- Creating NumPy arrays
- Understanding array dimensions and shapes
- Reshaping data
- Array indexing and slicing
- Boolean masking
- Statistical calculations
- Combining multiple datasets
- Building simple clinical risk scores

---

## Skills Demonstrated

- Python
- NumPy
- Array Manipulation
- Boolean Masking
- Feature Engineering
- Statistical Analysis
- Clinical Data Processing
- Healthcare Analytics

---

## Topics Covered

### Array Creation

Creating one-dimensional and two-dimensional arrays:

```python
import numpy as np

hr = np.array([80, 110, 130, 90, 150])
rr = np.array([120, 85, 70, 95, 60])
lactate = np.array([1.0, 2.5, 3.0, 0.8, 4.2])
```

---

### Array Shapes and Reshaping

Examples:

```python
hr.shape

hr.reshape(5, 1)
```

Learning how to convert vectors into matrices and prepare data for analysis.

---

### Combining Arrays

Combining multiple clinical variables into a single patient matrix:

```python
patients = np.column_stack(
    (hr, rr, lactate)
)
```

Example structure:

| HR | RR | Lactate |
|----|----|---------|
| 80 | 120 | 1.0 |
| 110 | 85 | 2.5 |
| 130 | 70 | 3.0 |

---

### Statistical Analysis

Computing summary statistics:

```python
np.mean(hr)
np.median(hr)
np.std(hr)

np.min(hr)
np.max(hr)
```

---

### Boolean Masking

Identifying patients meeting clinical criteria:

```python
tachycardia = hr > 100
```

Example output:

```python
array([
    False,
    True,
    True,
    False,
    True
])
```

Combining multiple criteria:

```python
(hr > 100) &
(rr < 90) &
(lactate > 2)
```

---

### Simulated ICU Dataset

Generating synthetic patient data:

```python
np.random.seed(42)

hr = np.random.randint(60, 160, 100)
rr = np.random.randint(50, 140, 100)
lactate = np.random.uniform(0, 8, 100)
```

Used to practice data analysis on larger datasets.

---

## Clinical Risk Score Challenge

A simple sepsis-inspired risk score was implemented.

### Scoring Rules

| Criterion | Points |
|------------|---------|
| HR > 100 | 1 |
| RR < 90 | 1 |
| Lactate > 2 | 1 |

### Risk Categories

| Score | Category |
|---------|----------|
| 0–1 | Low Risk |
| 2 | Medium Risk |
| 3 | High Risk |

Example approach:

```python
score = (
    (hr > 100).astype(int)
    + (rr < 90).astype(int)
    + (lactate > 2).astype(int)
)
```

---

## Technologies Used

- Python
- NumPy
- Jupyter Notebook
- Google Colab

---

## Future Improvements

Planned next steps include:

- Pandas integration
- Data visualization with Matplotlib
- Exploratory Data Analysis (EDA)
- Real-world healthcare datasets
- Machine learning workflows
- Clinical dashboard development

---

## Purpose

This repository documents my learning journey from clinical medicine toward healthcare analytics, data science, and AI applications in healthcare.

The long-term goal is to combine medical expertise with data-driven methods to improve clinical decision support and healthcare outcomes.
