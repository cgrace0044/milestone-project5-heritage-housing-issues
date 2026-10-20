# 🏠 Heritage Housing Issues

## Project Overview

Lydia Doe has inherited four houses located in Ames, Iowa, USA. Although she has knowledge of property prices in her home country of Belgium, she is unfamiliar with the housing market in Ames and is concerned that this could lead to inaccurate property valuations.

The purpose of this project is to use historical housing data from Ames, Iowa, to investigate the factors associated with house sale prices and develop a machine learning model capable of predicting property values.

The project will deliver a Streamlit dashboard that allows Lydia to explore the factors associated with house prices, view predicted sale prices for the four inherited properties, and predict the sale price of other houses in Ames.

## 📊 Dataset Content

The dataset was sourced from <a href="https://www.kaggle.com/codeinstitute/housing-prices-data" target="_blank">Kaggle</a> and contains housing records from **Ames, Iowa, USA**. It is used within a fictitious business scenario where predictive analytics can help estimate residential property values.

### 📋 Dataset Overview

| | |
|---|---|
| **Number of records** | 1,460 properties |
| **Number of variables** | 24 |
| **Target variable** | `SalePrice` |
| **Location** | Ames, Iowa, USA |
| **Construction years represented** | 1872–2010 |
| **Analysis type** | Regression / Predictive Analytics |

The dataset describes a range of property characteristics, including floor area, basement and garage features, kitchen quality, lot dimensions, property condition and quality, construction dates, and sale price.

### 🏠 Variable Definitions

| **Variable** | **Meaning** | **Values / Range** |
|---|---|---|
| `1stFlrSF` | First-floor area in square feet | 334–4692 |
| `2ndFlrSF` | Second-floor area in square feet | 0–2065 |
| `BedroomAbvGr` | Bedrooms above grade (excluding basement bedrooms) | 0–8 |
| `BsmtExposure` | Walkout or garden-level basement walls | Gd: Good; Av: Average; Mn: Minimum; No: No Exposure; None: No Basement |
| `BsmtFinType1` | Rating of basement finished area | GLQ: Good Living Quarters; ALQ: Average; BLQ: Below Average; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinished; None: No Basement |
| `BsmtFinSF1` | Type 1 finished basement area in square feet | 0–5644 |
| `BsmtUnfSF` | Unfinished basement area in square feet | 0–2336 |
| `TotalBsmtSF` | Total basement area in square feet | 0–6110 |
| `GarageArea` | Garage area in square feet | 0–1418 |
| `GarageFinish` | Interior finish of the garage | Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage |
| `GarageYrBlt` | Year garage was built | 1900–2010 |
| `GrLivArea` | Above-ground living area in square feet | 334–5642 |
| `KitchenQual` | Kitchen quality | Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor |
| `LotArea` | Lot size in square feet | 1300–215245 |
| `LotFrontage` | Linear feet of street connected to property | 21–313 |
| `MasVnrArea` | Masonry veneer area in square feet | 0–1600 |
| `EnclosedPorch` | Enclosed porch area in square feet | 0–286 |
| `OpenPorchSF` | Open porch area in square feet | 0–547 |
| `OverallCond` | Overall condition of the house | 1: Very Poor – 10: Very Excellent |
| `OverallQual` | Overall material and finish quality | 1: Very Poor – 10: Very Excellent |
| `WoodDeckSF` | Wood deck area in square feet | 0–736 |
| `YearBuilt` | Original construction year | 1872–2010 |
| `YearRemodAdd` | Remodel year (same as construction year if not remodelled) | 1950–2010 |
| `SalePrice` | Property sale price | 34,900–755,000 |

## 🎯 Business Requirements

Based on the client's needs, the project focuses on two key business requirements:

### 📊 BR1 — Understand Sale Price Drivers

Identify which house attributes are most strongly associated with `SalePrice` and present these relationships through clear data visualisations.

**Success criteria:** The client should be able to understand which property characteristics have the strongest relationships with house sale prices in Ames, Iowa.

### 🏠 BR2 — Predict House Sale Prices

Develop a machine learning model capable of predicting the sale price of the client's four inherited properties and other houses in Ames, Iowa.

**Success criteria:** The model should provide reliable sale price predictions and its performance should be evaluated against an appropriate regression performance metric.

### Prediction Error

The client requires the predictive model to achieve an R² score of at least **0.75 on both the training and test datasets**.

An R² score of 0.75 indicates that the model explains approximately 75% of the variation in house sale prices.

The model is designed to provide an **estimated sale price rather than an exact property valuation** this is why 0.75 is deemed to be sufficient in this case.

In other machine learning models, for example diagnostics a higher R² score would be required. 

## Hypotheses and How to Validate Them

We developed three hypotheses about the factors influencing house sale prices in Ames, Iowa:

1. **Overall Quality:** I suspect houses with higher overall property quality have higher sale prices.
2. **Living Area:** I suspect houses with larger above-ground living areas have higher sale prices.
3. **Year Built:** I suspect newer houses have higher sale prices.

**Validation Method**

We will investigate these hypotheses through exploratory data analysis, using scatterplots and Pearson and Spearman correlation studies to examine the relationships between `OverallQual`, `GrLivArea`, `YearBuilt` and `SalePrice`.

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary

- Project overview, terms and jargon.
- Description of the housing dataset.
- Client's business requirements and project success criteria.

### Page 2: House Sales Price Study

- Address Business Requirement 1.
- Checkboxes to inspect the historical and inherited housing datasets.
- Interactive scatterplots and Pearson and Spearman correlation heatmaps.
- Findings and conclusions about the attributes most correlated with `SalePrice`.

### Page 3: Inherited Houses Valuation

- Address Business Requirement 2.
- Display the four inherited houses' attributes.
- Predict the sale price of each house using the trained ML pipeline.
- Display the combined estimated value of all four houses.

### Page 4: Project Hypothesis and Validation

- Present three hypotheses and their validation:
  - **Overall quality:** Higher-quality houses have higher sale prices — Supported.
  - **Living area:** Larger living areas are associated with higher sale prices — Supported.
  - **Year built:** Newer houses have higher sale prices — Supported.
- Conclusions supported by the House Sales Price Study.

### Page 5: Predict a House Price

- Address Business Requirement 2.
- Interactive widgets to enter house attributes.
- Predict and display the estimated sale price using the trained ML pipeline.

### Page 6: ML Pipeline Performance

- Display the trained regression pipeline steps and selected features.
- Present model evaluation metrics for training and test datasets.
- Checkbox to display the feature importance plot.
- Summarise model performance against the project's success criteria.

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the .python-version Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements

I would like to thank my mentor, **Can Sücüllü**, for his guidance, support and valuable feedback throughout the development of this project.

