
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")


# Variables selected in the House Sales Price Study notebook
VARS_TO_STUDY = [
    "OverallQual",
    "GrLivArea",
    "GarageArea",
    "TotalBsmtSF",
    "1stFlrSF",
    "YearBuilt"
]


# Load historical housing data
@st.cache_data
def load_data():
    train = pd.read_csv(
        "outputs/datasets/cleaned/TrainSetCleaned.csv"
    )
    test = pd.read_csv(
        "outputs/datasets/cleaned/TestSetCleaned.csv"
    )
    return pd.concat([train, test], ignore_index=True)


# Load inherited houses
@st.cache_data
def load_inherited_houses():
    return pd.read_csv(
        "outputs/datasets/collection/inherited_houses.csv"
    )


# Scatterplot based on the Jupyter notebook
def scatter_plot_for_eda(df, col, target_var):

    if col in ["GarageArea", "TotalBsmtSF"]:
        df = df[df[col] > 0]

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.scatterplot(
        data=df,
        x=col,
        y=target_var,
        ax=ax
    )

    ax.set_title(
        f"{col} vs {target_var}",
        fontsize=18
    )
    ax.set_xlabel(col, fontsize=13)
    ax.set_ylabel(target_var, fontsize=13)
    ax.tick_params(axis="both", labelsize=11)

    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)


# Heatmap function from the Jupyter notebook
def heatmap_corr(df, threshold, figsize=(10, 8), font_annot=10):

    if len(df.columns) > 1:

        mask = np.zeros_like(df, dtype=bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True

        fig, axes = plt.subplots(figsize=figsize)

        sns.heatmap(
            df,
            annot=True,
            xticklabels=True,
            yticklabels=True,
            mask=mask,
            cmap="viridis",
            annot_kws={"size": font_annot},
            ax=axes,
            linewidth=0.5
        )

        axes.set_yticklabels(df.columns, rotation=0)
        plt.ylim(len(df.columns), 0)

        st.pyplot(fig)
        plt.close(fig)


def page_house_price_study_body():

    st.write("### 🏠 House Sales Price Study")

    st.info(
        "The client wants to understand how house "
        "attributes relate to sale prices through "
        "data visualisations."
    )

    df = load_data()

    # Inspect datasets
    if st.checkbox("Inspect Historical Housing Dataset"):

        st.write(
            f"The dataset contains **{df.shape[0]} houses** "
            f"and **{df.shape[1]} columns**. "
            "The first 10 rows are shown below."
        )

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

    if st.checkbox("Inspect Four Inherited Houses"):

        inherited_houses = load_inherited_houses()

        st.write(
            f"The dataset contains "
            f"**{inherited_houses.shape[0]} houses** "
            f"and **{inherited_houses.shape[1]} columns**."
        )

        st.dataframe(
            inherited_houses,
            use_container_width=True
        )

    st.divider()

    # Correlation study
    st.write("### 📊 Correlation Study")

    st.write(
        "Pearson and Spearman correlation studies identified "
        "six house attributes most strongly related to sale prices."
    )

    st.info(
        "The correlation results and plots indicate that:\n\n"
        "- Houses with **higher overall quality** tend to sell "
        "for higher prices (`OverallQual`).\n"
        "- Houses with **larger living areas** tend to sell "
        "for higher prices (`GrLivArea`).\n"
        "- Houses with **larger garages** tend to sell "
        "for higher prices (`GarageArea`).\n"
        "- Houses with **larger basements** tend to sell "
        "for higher prices (`TotalBsmtSF`).\n"
        "- Houses with **larger first floors** tend to sell "
        "for higher prices (`1stFlrSF`).\n"
        "- **Newer houses** tend to sell for higher prices "
        "(`YearBuilt`)."
    )

    df_eda = df[VARS_TO_STUDY + ["SalePrice"]]

    st.divider()

    # Scatterplots
    st.write("### 📈 Variables vs Sale Price")

    st.info(
        "Select a house attribute below to explore "
        "its relationship with sale price."
    )

    selected_variable = st.selectbox(
        "Select a house attribute",
        VARS_TO_STUDY
    )

    scatter_plot_for_eda(
        df_eda,
        selected_variable,
        "SalePrice"
    )

    # Interpretations based on the Jupyter notebook
    if selected_variable == "GrLivArea":

        interpretation = (
            "Larger living areas are generally associated with "
            "higher sale prices. However, a couple of very large "
            "properties have relatively low sale prices."
        )

    elif selected_variable == "GarageArea":

        interpretation = (
            "Larger garages are generally associated with "
            "higher sale prices. A small number of properties "
            "have very large garages but relatively low sale prices."
        )

    elif selected_variable == "TotalBsmtSF":

        interpretation = (
            "Larger basements are generally associated with "
            "higher sale prices. One property has a particularly "
            "large basement but a relatively low sale price."
        )

    elif selected_variable == "OverallQual":

        interpretation = (
            "Properties with higher overall quality "
            "generally have higher sale prices."
        )

    elif selected_variable == "1stFlrSF":

        interpretation = (
            "Properties with larger first-floor areas "
            "generally have higher sale prices."
        )

    elif selected_variable == "YearBuilt":

        interpretation = (
            "Newer properties generally have higher sale prices."
        )

    st.success(f"**Graph interpretation:** {interpretation}")

    if selected_variable in ["GarageArea", "TotalBsmtSF"]:

        st.caption(
            "Properties without a garage or basement are "
            "excluded from this graph. These are not outliers."
        )

    st.divider()

    # Correlation heatmap
    st.write("### 🔥 Correlation Heatmap")

    st.info(
        "This heatmap shows how strongly house attributes "
        "are related to each other and to sale price. "
        "Higher positive values indicate stronger relationships."
    )

    if st.checkbox("View Correlation Heatmap"):

        df_corr_spearman = df_eda.corr(method="spearman")

        heatmap_corr(
            df=df_corr_spearman,
            threshold=0.4
        )

        st.success(
            "**Heatmap interpretation:**\n\n"
            "- **Overall quality** and **living area** show the "
            "strongest relationships with sale price.\n"
            "- **Garage size**, **basement area**, **first-floor area** "
            "and **year built** also show positive relationships "
            "with sale price.\n"
            "- Some property attributes are related to each other. "
            "For example, houses with larger basements often have "
            "larger first-floor areas."
        )


if __name__ == "__main__":
    page_house_price_study_body()
