# Testing

This document records testing carried out for the **Heritage Housing Issues** project.

---

## User Story Testing

The 12 user stories defined in the README were used to guide the
development of the project.

| User Story | Business Requirement | Implementation and Evidence |
|---|---|---|
| [US1 — Understanding the Business Case](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/1) | BR1, BR2 | [README](README.md) — Business Requirements, ML Business Case and project rationale |
| [US2 — Collect and Explore the Data](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/2) | BR1, BR2 | [Data Collection Notebook](jupyter_notebooks/01%20-%20DataCollection.ipynb) — data collection and initial exploration |
| [US3 — Clean and Prepare Datasets](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/3) | BR1, BR2 | [Data Cleaning Notebook](jupyter_notebooks/02_DataCleaning.ipynb) and [Data Cleaning Dashboard Page](app_pages/page_data_cleaning.py) |
| [US4 — Patterns and Correlations in the Data](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/4) | BR1 | [House Price Study Notebook](jupyter_notebooks/03_HousePriceStudy.ipynb) and [House Price Study Dashboard Page](app_pages/page_house_price_study.py) |
| [US5 — Feature Engineering](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/5) | BR2 | [Feature Engineering Notebook](jupyter_notebooks/04_FeatureEngineering.ipynb) — feature transformations and analysis |
| [US6 — Develop a Regression Model](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/6) | BR2 | [Model Development Notebook](jupyter_notebooks/05_Modeling%20and%20Evaluation%20Predict%20SalePrice.ipynb) — regression model development and comparison |
| [US7 — Optimise Regression Machine Learning Model](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/7) | BR2 | [Model Development Notebook](jupyter_notebooks/05_Modeling%20and%20Evaluation%20Predict%20SalePrice.ipynb) — hyperparameter optimisation and model evaluation |
| [US8 — Create Streamlit Dashboard](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/8) | BR1, BR2 | [Streamlit Application](app.py) and [Manual Dashboard Testing](#manual-dashboard-testing) |
| [US9 — Develop Project Summary, House Price Study and Hypothesis Pages](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/9) | BR1, BR2 | [Project Summary](app_pages/page_summary.py), [House Price Study](app_pages/page_house_price_study.py) and [Hypothesis Validation](app_pages/page_project_hypothesis_body.py) |
| [US10 — Create Pages for House Price Prediction and ML Performance](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/10) | BR1, BR2 | [House Price Prediction](app_pages/page_predict_house_prices.py), [Inherited Houses](app_pages/page_inherited_houses.py) and [ML Performance](app_pages/page_ml_pipeline.py) |
| [US11 — Prepare Streamlit Dashboard for Deployment to Heroku](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/11) | BR1, BR2 | [README](README.md) — deployment instructions; [Manual Dashboard Testing](#manual-dashboard-testing) and [Cross-Browser Testing](#cross-browser-compatibility-testing) |
| [US12 — Complete Project Documentation and Testing](https://github.com/cgrace0044/milestone-project5-heritage-housing-issues/issues/12) | BR1, BR2 | [README](README.md), [Manual Dashboard Testing](#manual-dashboard-testing), [PEP8 Validation](#pep8-code-validation) and [Notebook Validation](#jupyter-notebook-code-validation) |

## Manual Dashboard Testing

Manual testing was completed on the deployed [Heritage Housing Issues Dashboard](https://project5-heritage-housing-25399c2d2f27.herokuapp.com/). All 46 documented checks passed.

<details>
<summary><strong>Test 1 — Dashboard Navigation ✅</strong></summary>

| Check | Result |
| --- | :---: |
| Application loads successfully | ✓ |
| All seven dashboard pages are listed | ✓ |
| All seven pages open successfully | ✓ |
| Navigation between pages works | ✓ |

</details>

<details>
<summary><strong>Test 2 — Quick Project Summary ✅</strong></summary>

| Check | Result |
| --- | :---: |
| Project introduction and dataset information display correctly | ✓ |
| Project terminology expander opens and displays its content | ✓ |
| Both business requirements display correctly | ✓ |
| Training R² of 0.925 and test R² of 0.825 display correctly | ✓ |
| Project README link is available | ✓ |

</details>

<details>
<summary><strong>Test 3 — Data Cleaning ✅</strong></summary>

| Check | Result |
| --- | :---: |
| Introduction and cleaning methods display correctly | ✓ |
| Numerical data distributions expander works | ✓ |
| Violin plots display for `BedroomAbvGr`, `LotFrontage`, `MasVnrArea` and `2ndFlrSF` | ✓ |
| Metrics show 1,460 houses, 21 variables and 0 missing values | ✓ |
| Page displays without errors | ✓ |

</details>

<details>
<summary><strong>Test 4 — House Sales Price Study ✅</strong></summary>

| Check | Result |
| --- | :---: |
| Historical housing dataset displays its first 10 rows | ✓ |
| Four inherited houses are displayed | ✓ |
| Six correlated attributes are presented | ✓ |
| All six scatterplots and their interpretations display | ✓ |
| Notes about excluded zero values display | ✓ |
| Correlation heatmap and its interpretation display | ✓ |

</details>

<details>
<summary><strong>Test 5 — Project Hypothesis and Validation ✅</strong></summary>

| Check | Result |
| --- | :---: |
| Page introduction displays | ✓ |
| Overall quality correlation of 0.81 displays | ✓ |
| Above-ground living area correlation of 0.73 displays | ✓ |
| Year built correlation of 0.65 displays | ✓ |
| Hypotheses are shown as supported, with explanations | ✓ |

</details>

<details>
<summary><strong>Test 6 — Inherited Houses Valuation ✅</strong></summary>

| Check | Result |
| --- | :---: |
| Page introduction displays | ✓ |
| Data for all four inherited houses can be viewed | ✓ |
| Predict House Prices button works | ✓ |
| Individual predicted prices display for all four houses | ✓ |
| Combined predicted value equals the sum of the four predictions | ✓ |

</details>

<details>
<summary><strong>Test 7 — Predict a House Price ✅</strong></summary>

| Check | Result |
| --- | :---: |
| Page introduction displays | ✓ |
| All seven feature inputs and their default values display | ✓ |
| All seven inputs can be changed | ✓ |
| Prediction works with default inputs | ✓ |
| Prediction works with modified inputs | ✓ |
| A positive predicted house price is displayed | ✓ |

</details>

<details>
<summary><strong>Test 8 — ML Pipeline Performance ✅</strong></summary>

| Check | Result |
| --- | :---: |
| Page introduction displays | ✓ |
| Pipeline checkbox reveals the ExtraTreesRegressor model | ✓ |
| Seven selected model features display | ✓ |
| Feature importance graph displays | ✓ |
| Performance table shows training R² of 0.925 and test R² of 0.825 | ✓ |
| Actual-versus-predicted plots display for training and test data | ✓ |
| Interpretations and associated checkboxes display and work | ✓ |

</details>

<details>
<summary><strong>Test 9 — Responsive Design ✅</strong></summary>

Responsive layouts were checked using [Responsive Test Tool](https://responsivetesttool.com/).

| Check | Result |
| --- | :---: |
| Desktop layout displays correctly | ✓ |
| Tablet layout displays correctly | ✓ |
| Mobile layout displays correctly | ✓ |

**Responsive Design Screenshot**

![Responsive Design Testing](assets/responsiveness.png)

</details>

---

## PEP8 Code Validation

Python files were checked using the [Code Institute PEP8 Validator](https://pep8ci.herokuapp.com/). Reported formatting issues were corrected and retested. All 11 files passed.

| Python file / component | Result |
| --- | :---: |
| `app.py` | ✓ |
| Page 1 — Quick Project Summary | ✓ |
| Page 2 — Data Cleaning | ✓ |
| Page 3 — House Sales Price Study | ✓ |
| Page 4 — Project Hypothesis and Validation | ✓ |
| Page 5 — Inherited Houses Valuation | ✓ |
| Page 6 — Predict a House Price | ✓ |
| Page 7 — ML Pipeline Performance | ✓ |
| Regression evaluation supporting Python file | ✓ |
| `src/data_management.py` | ✓ |
| `src/machine_learning/predictive_analysis_ui.py` | ✓ |

---

## Jupyter Notebook Code Validation

All five Jupyter notebooks were checked using **Ruff** in GitHub Codespaces for common Python code issues and line-length violations. Reported issues were corrected and each notebook passed on retesting.

| Jupyter notebook | Result |
| --- | :---: |
| `01 - DataCollection.ipynb` | ✓ |
| `02_DataCleaning.ipynb` | ✓ |
| `03_HousePriceStudy.ipynb` | ✓ |
| `04_FeatureEngineering.ipynb` | ✓ |
| `05_Modeling and Evaluation Predict SalePrice.ipynb` | ✓ |

Ruff validates code quality; it does not execute the notebooks.

---

### CSS
No errors were found when passing my CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

 <details>

 <summary>CSS</summary>

![CSS Validation](assets/cssvalidation.png)
 </details>

---

### Cross-Browser Compatibility Testing

The Heritage Housing application was tested across multiple web browsers to ensure consistent functionality, usability, and appearance.

| Browser | Test Result |
|---|---|
| Google Chrome | Pass |
| Safari | Pass |
| Mozilla Firefox | Pass |

---