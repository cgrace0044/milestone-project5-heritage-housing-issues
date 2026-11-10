
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split


sns.set_style("whitegrid")


@st.cache_data
def load_original_data():

    df = pd.read_csv(
        "outputs/datasets/collection/house_prices_records.csv"
    )

    # Recreate the original training split as we want to show
    # data prior to cleaning.
    TrainSet, TestSet, _, __ = train_test_split(
        df,
        df["SalePrice"],
        test_size=0.2,
        random_state=0
    )

    return TrainSet


# Plotting code adapted from the Data Cleaning Jupyter notebook.
def plot_data_distributions(TrainSet):

    variables = [
        "BedroomAbvGr",
        "LotFrontage",
        "MasVnrArea",
        "2ndFlrSF"
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    for ax, col in zip(axes.flatten(), variables):
        sns.violinplot(y=TrainSet[col].dropna(), ax=ax)
        ax.set_title(col)

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


def page_data_cleaning_body():

    st.write("### 🧹 Data Cleaning")

    # Introduction
    st.write(
        "The historical housing dataset contained missing values "
        "and some attributes that were not needed for modelling. "
        "Data cleaning was carried out to address these issues, "
        "improve data quality and prepare the dataset for machine "
        "learning. The inherited housing dataset did not require "
        "any cleaning as there were no missing values."
    )

    st.divider()

    # Cleaning methods
    st.write("#### 🛠️ How the Data Was Cleaned")

    st.markdown(
        "- **Garage and basement:** Missing values were "
        "labelled 'No Garage', 'No Basement' or 'Missing'.\n"
        "- **Removed attributes:** `EnclosedPorch` (91% missing) "
        "and `WoodDeckSF` (89% missing) were dropped.\n"
        "- **Garage construction year:** `GarageYrBlt` was "
        "dropped because it was strongly related to `YearBuilt`.\n"
        "- **Numerical information:** Missing values for "
        "`BedroomAbvGr`, `LotFrontage`, `MasVnrArea` "
        "and `2ndFlrSF` were filled using median imputation."
    )

    # Numerical distributions
    with st.expander("📊 View Numerical Data Distributions"):

        st.info(
            "Median imputation replaces missing numerical values "
            "with the median (middle value) of each attribute. "
            "It was chosen because it is less affected by "
            "unusually high or low values."
        )

        TrainSet = load_original_data()
        plot_data_distributions(TrainSet)

    st.divider()

    # Cleaning outcome
    st.write("#### ✅ Cleaning Outcome")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Houses Retained", "1,460")

    with col2:
        st.metric("Dataset Variables", "21")

    with col3:
        st.metric("Missing Values", "0")


if __name__ == "__main__":
    page_data_cleaning_body()
