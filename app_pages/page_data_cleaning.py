
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

    fig, axes = plt.subplots(2, 2, figsize=(10, 6))

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

    st.write(
        "Data cleaning helps improve the reliability "
        "of house price predictions."
    )

    st.markdown(
        "- **Historical housing dataset:** Missing values "
        "required cleaning.\n"
        "- **Inherited housing dataset:** No missing values, "
        "so no cleaning was needed."
    )

    st.divider()

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

    with st.expander("📊 View Numerical Data Distributions"):

        st.info(
            "Median imputation was used because it is less "
            "affected by unusually high or low values."
        )

        df = load_original_data()
        plot_data_distributions(df)

    st.divider()

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

