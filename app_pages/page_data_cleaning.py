
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")


# Load original historical housing data
@st.cache_data
def load_original_data():
    return pd.read_csv(
        "outputs/datasets/collection/house_prices_records.csv"
    )


# Create violin plots
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

    st.write(
        "Before analysing house prices, the historical "
        "housing dataset was checked for missing information "
        "and cleaned to prepare it for further analysis "
        "and prediction."
    )

    st.divider()

    # Cleaning summary
    st.write("### 🛠️ How the Data Was Cleaned")

    st.markdown(
        "- **Garage and basement data:** Missing values were "
        "labelled as 'No Garage', 'No Basement' or 'Missing', "
        "depending on the property's features.\n"
        "- **Removed attributes:** Dropped `EnclosedPorch` "
        "(91% missing) and `WoodDeckSF` (89% missing).\n"
        "- **Numerical data:** Missing values were filled using "
        "median values after examining their distributions "
        "(see violin plots below).\n"
        "- **Garage construction year:** Used zero to indicate "
        "properties without garages (81 records).\n"
        "- **Quality checks:** Confirmed no missing values "
        "or duplicate records remained."
    )

    st.divider()

    # Violin plots
    st.write("### 📊 Exploring Data Distributions")

    st.write(
        "The violin plots below show the distributions "
        "of four property attributes used to guide "
        "the treatment of missing numerical values."
    )

    with st.expander("📈 View Violin Plots"):

        df = load_original_data()

        plot_data_distributions(df)

        st.info(
            "**Why Median Imputation?**\n\n"
            "The violin plots show that some property attributes "
            "have skewed distributions, extreme values or many zeros. "
            "The median was chosen because it is less influenced by "
            "unusually high or low values."
        )

    st.divider()

    # Cleaning outcome
    st.write("### ✅ Cleaning Outcome")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏠 Houses Retained", "1,460")

    with col2:
        st.metric("📋 House Attributes", "21")

    with col3:
        st.metric("🔍 Missing Values", "0")

    st.success(
        "The historical housing dataset was successfully "
        "cleaned and prepared for the House Sales Price "
        "Study and machine learning."
    )


if __name__ == "__main__":
    page_data_cleaning_body()
