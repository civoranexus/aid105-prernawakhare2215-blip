# SchemeAssist AI – Government Scheme Recommendation System

# Project Overview

SchemeAssist AI is a web-based application that recommends suitable Indian government schemes based on a user's profile details such as age, income, state, category, and gender.

The system uses rule-based scoring logic to match users with the most relevant schemes.

Data preprocessing and feature engineering were initially performed using Jupyter Notebook.

# Dataset Information

# Source

The dataset was collected from Kaggle and curated to include relevant Indian government schemes along with eligibility criteria, benefits, and state/category details.

# Why This Dataset Was Chosen

- Contains structured information about government schemes
- Includes eligibility-related attributes
- Suitable for rule-based recommendation logic
- Easy to preprocess and extend

# Data Preprocessing Steps

- Removed unnecessary columns
- Cleaned missing or inconsistent values
- Standardized text fields
- Added custom features such as:
  - Income eligibility range
  - Category tags
  - State mapping
- Structured the dataset for efficient scoring and filtering

# How It Is Used

The dataset is loaded using Pandas and passed into the recommendation engine.  
Each scheme is evaluated against user input parameters such as age, income, state, category, and gender.

The system assigns scores based on matching conditions and returns ranked recommendations.

---

# Features

- User-friendly web interface (Flask + HTML/CSS)
- Profile-based scheme recommendation
- Rule-based scoring engine
- Clean UI with structured result display
- Modular project structure

---
