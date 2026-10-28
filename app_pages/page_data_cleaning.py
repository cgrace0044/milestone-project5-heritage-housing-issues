
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")


@st.cache_data
def load_original_data():
    return pd.read_csv(
        "outputs/datasets/collection/house_prices_records.csv"
    )


def plot_data_distributions(df):

    variables = {
        "BedroomAbvGr": "Number of Bedrooms",
        "LotFrontage": "Street Frontage",
        "MasVnrArea": "Masonry Veneer Area",
        "2ndFlrSF": "Second-Floor Area"
    }

    fig, axes = plt.subplots(2, 2, figsize=(11, 7))

    for ax, (column, label) in zip(
        axes.flatten(),
        variables.items()
    ):
        sns.violinplot(
            y=df[column].dropna(),
            ax=ax
        )

        ax.set_title(label, fontsize=12)
        ax.set_ylabel("")

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


def page_data_cleaning_body():

    st.write("### 🧹 Data Cleaning")

    st.markdown(
        "- **Historical housing dataset:** Checked for missing "
        "information and cleaned for further analysis.\n"
        "- **Inherited housing dataset:** Contained no missing values."
    )

    st.divider()

    st.write("### 🛠️ How the Data Was Cleaned")

    st.markdown(
        "- **Garage and basement data:** Missing values were "
        "labelled as 'No Garage', 'No Basement' or 'Missing'.\n"
        "- **Removed attributes:** Dropped `EnclosedPorch` "
        "(91% missing) and `WoodDeckSF` (89% missing).\n"
        "- **Garage construction year:** Used zero for "
        "properties without garages (81 records).\n"
        "- **Numerical data:** Missing values were filled "
        "using medians after examining their distributions."
    )

    with st.expander("📊 View Violin Plots — Numerical Data"):

        st.info(
            "**Median Imputation:** Some attributes have skewed "
            "distributions or extreme values, so the median was "
            "chosen to fill missing data because it is less "
            "affected by outliers."
        )

        df = load_original_data()
        plot_data_distributions(df)

    st.divider()

    st.write("### ✅ Cleaning Outcome")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏠 Houses Retained", "1,460")

    with col2:
        st.metric("📋 House Attributes", "21")

    with col3:
        st.metric("🔍 Missing Values", "0")

    st.success(
        "The cleaned dataset is ready for the "
        "House Sales Price Study and machine learning."
    )


if __name__ == "__main__":
    page_data_cleaning_body()
