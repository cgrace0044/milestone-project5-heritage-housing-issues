# Testing

This document records testing carried out for the **Heritage Housing Issues** project.

## Manual Dashboard Testing

Manual tests were performed on the deployed Streamlit application:

**[Heritage Housing Issues Dashboard](https://project5-heritage-housing-25399c2d2f27.herokuapp.com/)**

Each check below was confirmed as passed.

### Test 1 — Dashboard Navigation

| Check | Result |
| --- | --- |
| Application loads successfully | Pass |
| All seven dashboard pages are listed | Pass |
| All seven pages open successfully | Pass |
| Navigation between pages works | Pass |

### Test 2 — Quick Project Summary

| Check | Result |
| --- | --- |
| Project introduction and dataset information display correctly | Pass |
| Project terminology expander opens and displays its content | Pass |
| Both business requirements display correctly | Pass |
| Training R² of 0.925 and test R² of 0.825 display correctly | Pass |
| Project README link is available | Pass |

### Test 3 — Data Cleaning

| Check | Result |
| --- | --- |
| Introduction and cleaning methods display correctly | Pass |
| Numerical data distributions expander works | Pass |
| Violin plots display for `BedroomAbvGr`, `LotFrontage`, `MasVnrArea` and `2ndFlrSF` | Pass |
| Metrics show 1,460 houses, 21 variables and 0 missing values | Pass |
| Page displays without errors | Pass |

### Test 4 — House Sales Price Study

| Check | Result |
| --- | --- |
| Historical housing dataset displays its first 10 rows | Pass |
| Four inherited houses are displayed | Pass |
| Six correlated attributes are presented | Pass |
| All six scatterplots and their interpretations display | Pass |
| Notes about excluded zero values display | Pass |
| Correlation heatmap and its interpretation display | Pass |

### Test 5 — Project Hypothesis and Validation

| Check | Result |
| --- | --- |
| Page introduction displays | Pass |
| Overall quality correlation of 0.81 displays | Pass |
| Above-ground living area correlation of 0.73 displays | Pass |
| Year built correlation of 0.65 displays | Pass |
| Hypotheses are shown as supported, with explanations | Pass |

### Test 6 — Inherited Houses Valuation

| Check | Result |
| --- | --- |
| Page introduction displays | Pass |
| Data for all four inherited houses can be viewed | Pass |
| Predict House Prices button works | Pass |
| Individual predicted prices display for all four houses | Pass |
| Combined predicted value equals the sum of the four predictions | Pass |

### Test 7 — Predict a House Price

| Check | Result |
| --- | --- |
| Page introduction displays | Pass |
| All seven feature inputs and their default values display | Pass |
| All seven inputs can be changed | Pass |
| Prediction works with default inputs | Pass |
| Prediction works with modified inputs | Pass |
| A positive predicted house price is displayed | Pass |

### Test 8 — ML Pipeline Performance

| Check | Result |
| --- | --- |
| Page introduction displays | Pass |
| Pipeline checkbox reveals the ExtraTreesRegressor model | Pass |
| Seven selected model features display | Pass |
| Feature importance graph displays | Pass |
| Performance table shows training R² of 0.925 and test R² of 0.825 | Pass |
| Actual-versus-predicted plots display for training and test data | Pass |
| Interpretations and associated checkboxes display and work | Pass |

### Test 9 — Responsive Design

Responsive layout was checked using **[Responsive Test Tool](assets/responsiveness.png)**.

| Check | Result |
| --- | --- |
| Desktop layout displays correctly | Pass |
| Tablet layout displays correctly | Pass |
| Mobile layout displays correctly | Pass |

## PEP8 Code Validation

Python code was checked using the **[Code Institute PEP8 Validator](https://pep8ci.herokuapp.com/)**. Where formatting issues were reported, they were corrected and the code was checked again. All 11 checked Python files passed their final validation.

| Python file / component | Initial issue or action | Final result |
| --- | --- | --- |
| `app.py` | No issues reported | Pass |
| Page 1 — Quick Project Summary | Long README URL line split across adjacent strings | Pass |
| Page 2 — Data Cleaning | Long comment split across two lines | Pass |
| Page 3 — House Sales Price Study | No issues reported | Pass |
| Page 4 — Project Hypothesis and Validation | No issues reported | Pass |
| Page 5 — Inherited Houses Valuation | Long import split across lines | Pass |
| Page 6 — Predict a House Price | Formatting adjusted for pipeline and feature loading | Pass |
| Page 7 — ML Pipeline Performance | No issues reported | Pass |
| Regression evaluation supporting Python file | Long lines, import and comment formatting corrected | Pass |
| `src/data_management.py` | No issues reported | Pass |
| `src/machine_learning/predictive_analysis_ui.py` | No issues reported | Pass |

## Jupyter Notebook Testing

**Status: Not yet tested.**

Notebook code-quality validation and notebook execution checks will be documented here once completed. These have not been counted as passed.

## Current Testing Outcome

The deployed dashboard passed all **48 manual checks**, including responsive design checks, and all **11 checked Python files** passed PEP8 validation. Notebook testing remains outstanding.
