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

## 🧪 Hypotheses and Validation

To better understand the factors that may influence house prices in Ames, Iowa, three hypotheses were defined for investigation.

| # | Hypothesis | Key Variable |
|---|---|---|
| 🏆 H1 | Higher overall property quality is associated with higher sale prices. | `OverallQual` |
| 📐 H2 | Larger above-ground living areas are associated with higher sale prices. | `GrLivArea` |
| 🏗️ H3 | More recently built properties are associated with higher sale prices. | `YearBuilt` |

### 🏆 H1 — Overall Property Quality

> **Hypothesis:** Properties with a higher overall quality rating are expected to achieve higher sale prices.

**Rationale:** Overall property quality reflects the standard of materials and finish of a house and may therefore be an important factor in determining its value.

**Validation:** The relationship between `OverallQual` and `SalePrice` will be investigated using correlation analysis and visualisation.

---

### 📐 H2 — Above-Ground Living Area

> **Hypothesis:** Properties with a larger above-ground living area are expected to achieve higher sale prices.

**Rationale:** Greater living space may increase the usefulness and desirability of a property and therefore contribute to a higher sale price.

**Validation:** The relationship between `GrLivArea` and `SalePrice` will be investigated using correlation analysis and visualisation.

---

### 🏗️ H3 — Property Age

> **Hypothesis:** More recently built properties are expected to achieve higher sale prices than older properties.

**Rationale:** Newer properties may benefit from more modern construction, features and standards, which could contribute to a higher market value.

**Validation:** The relationship between `YearBuilt` and `SalePrice` will be investigated using correlation analysis and visualisation.

## Dashboard Design
A dashboard will be designed in Stremlit to allow the client to under

* A project summary page, showing the project dataset summary and the client's requirements.
* A page listing your findings related to which features have the strongest correlation to the house sale price.
* A page displaying the 4 houses' attributes and their respective predicted sale price. It should display a message informing the summed predicted price for all 4 inherited houses. You should add interactive input widgets that allow a user to provide real-time house data to predict the sale price.
* A page indicating your project hypothesis(es) and how you validated it across the project.
* A technical page displaying your model performance. If you deployed an ML pipeline, you have to display your pipeline steps.

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

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.

