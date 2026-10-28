import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")


# Friendly labels for dataset variables
VARIABLE_LABELS = {
    "OverallQual": "Overall Property Quality",
    "GrLivArea": "Above-Ground Living Area",
    "GarageArea": "Garage Area",
    "GarageYrBlt": "Garage Year Built",
    "TotalBsmtSF": "Total Basement Area",
    "1stFlrSF": "First-Floor Area",
    "YearBuilt": "Year Built"
}


# Variables selected in the correlation study notebook
VARS_TO_STUDY = [
    "OverallQual",
    "GrLivArea",
    "GarageArea",
    "GarageYrBlt",
    "TotalBsmtSF",
    "1stFlrSF",
    "YearBuilt"
]


# Variables linked to the project hypotheses
HYPOTHESIS_VARIABLES = [
    "OverallQual",
    "GrLivArea",
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


# Load the four inherited houses
@st.cache_data
def load_inherited_houses():

    return pd.read_csv(
        "outputs/datasets/collection/inherited_houses.csv"
    )


# Scatterplot function
def scatter_plot_for_eda(df, col, target_var):

    plot_df = df.copy()

    # Exclude zero values from selected scatterplots
    if col in ["GarageArea", "GarageYrBlt", "TotalBsmtSF"]:
        plot_df = plot_df[plot_df[col] > 0]

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.scatterplot(
        data=plot_df,
        x=col,
        y=target_var,
        ax=ax,
        alpha=0.6
    )

    ax.set_title(
        f"{VARIABLE_LABELS[col]} vs Sale Price",
        fontsize=16
    )

    ax.set_xlabel(VARIABLE_LABELS[col])
    ax.set_ylabel("Sale Price ($)")

    ax.ticklabel_format(
        style="plain",
        axis="y"
    )

    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)


# Correlation heatmap function
def heatmap_corr(df, method, threshold=0.4):

    df_corr = df.corr(method=method)

    # Replace technical variable names with friendly labels
    df_corr = df_corr.rename(
        index=VARIABLE_LABELS,
        columns=VARIABLE_LABELS
    )

    fig, ax = plt.subplots(figsize=(11, 8))

    sns.heatmap(
        df_corr,
        annot=True,
        fmt=".2f",
        cmap="viridis",
        mask=abs(df_corr) < threshold,
        annot_kws={"size": 9},
        linewidths=0.5,
        vmin=-1,
        vmax=1,
        ax=ax
    )

    ax.set_title(
        f"{method.capitalize()} Correlation Heatmap",
        fontsize=16
    )

    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)

    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)


def page_house_price_study_body():

    st.write("### 🏠 House Sales Price Study")

    # Business Requirement 1
    st.info(
        "The client is interested in discovering how house "
        "attributes correlate with sale prices. "
        "Therefore, the client expects data visualisations "
        "of the correlated variables against SalePrice."
    )

    # Load historical housing data
    df = load_data()

    st.divider()

    # Inspect datasets
    st.write("### 📂 Inspect Housing Datasets")

    with st.expander("Inspect Historical Housing Dataset"):

        st.write(
            f"The historical dataset contains "
            f"**{df.shape[0]} houses** and "
            f"**{df.shape[1]} columns**. "
            "The first 10 rows are shown below."
        )

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

    with st.expander("Inspect Four Inherited Houses"):

        inherited_houses = load_inherited_houses()

        st.write(
            f"The inherited housing dataset contains "
            f"**{inherited_houses.shape[0]} houses** and "
            f"**{inherited_houses.shape[1]} columns**."
        )

        st.dataframe(
            inherited_houses,
            use_container_width=True
        )

    st.divider()

    # Correlation study summary
    st.write("### 📊 Correlation Study Summary")

    st.write(
        "Pearson and Spearman correlation studies were "
        "conducted to identify the property attributes "
        "most strongly associated with SalePrice. "
        "The five strongest correlations from each method "
        "were combined, resulting in seven unique variables "
        "selected for further analysis."
    )

    st.info(
        "**Seven variables identified:**\n\n"
        "- **Overall Property Quality** (`OverallQual`)\n"
        "- **Above-Ground Living Area** (`GrLivArea`)\n"
        "- Garage Area (`GarageArea`)\n"
        "- Garage Year Built (`GarageYrBlt`)\n"
        "- Total Basement Area (`TotalBsmtSF`)\n"
        "- First-Floor Area (`1stFlrSF`)\n"
        "- **Year Built** (`YearBuilt`)"
    )

    st.caption(
        "The three highlighted variables — OverallQual, "
        "GrLivArea and YearBuilt — are also investigated "
        "on the Project Hypothesis and Validation page."
    )

    st.write(
        "**Key finding:** Overall property quality and "
        "above-ground living area showed the strongest "
        "relationships with sale price across both "
        "correlation methods."
    )

    st.divider()

    # Prepare data for visual analysis
    df_eda = df[VARS_TO_STUDY + ["SalePrice"]]

    # Individual scatterplots
    st.write("### 📈 Variables vs Sale Price")

    st.write(
        "Explore the relationships between the seven "
        "selected property attributes and sale price. "
        "Choose a variable below to display its scatterplot."
    )

    selected_variable = st.selectbox(
        "Select a property attribute",
        VARS_TO_STUDY,
        format_func=lambda col: (
            f"{VARIABLE_LABELS[col]} ({col})"
        )
    )

    if selected_variable in HYPOTHESIS_VARIABLES:
        st.caption(
            "🌿 This variable is also investigated in "
            "the Project Hypothesis and Validation page."
        )

    scatter_plot_for_eda(
        df_eda,
        selected_variable,
        "SalePrice"
    )

    if selected_variable in [
        "GarageArea",
        "GarageYrBlt",
        "TotalBsmtSF"
    ]:
        st.info(
            "Zero values are excluded from this scatterplot "
            "to focus on properties with a recorded positive "
            "value for this attribute. The correlation "
            "heatmaps retain the original dataset values."
        )

    st.divider()

    # Correlation heatmaps
    st.write("### 🔥 Correlation Heatmaps")

    st.write(
        "Pearson and Spearman heatmaps show relationships "
        "between the selected variables and SalePrice. "
        "Correlations with an absolute value below 0.4 "
        "are hidden for clarity."
    )

    heatmap_selection = st.radio(
        "Choose a correlation method",
        ["Spearman", "Pearson", "Both"],
        horizontal=True
    )

    if heatmap_selection in ["Spearman", "Both"]:

        st.write("#### Spearman Correlation")

        st.caption(
            "Spearman measures how consistently two variables "
            "increase or decrease together, based on their ranks."
        )

        heatmap_corr(
            df_eda,
            method="spearman"
        )

    if heatmap_selection in ["Pearson", "Both"]:

        st.write("#### Pearson Correlation")

        st.caption(
            "Pearson measures the strength and direction "
            "of a linear relationship between two variables."
        )

        heatmap_corr(
            df_eda,
            method="pearson"
        )

    st.divider()

    # EDA interpretation
    st.write("### 🔍 EDA Interpretation")

    st.write(
        "The scatterplots support the positive relationships "
        "identified in the correlation study. "
        "The heatmaps also highlight relationships between "
        "YearBuilt and GarageYrBlt, and between "
        "TotalBsmtSF and 1stFlrSF."
    )

    with st.expander("View Outlier Findings"):

        st.write(
            "The scatterplots highlight some unusual "
            "observations in the historical dataset:"
        )

        st.markdown(
            "- **Above-Ground Living Area (`GrLivArea`):** "
            "A couple of very large properties have "
            "relatively low sale prices.\n"
            "- **Garage Area (`GarageArea`):** "
            "A small number of properties have very large "
            "garages and relatively low sale prices.\n"
            "- **Total Basement Area (`TotalBsmtSF`):** "
            "One property has a very large basement and "
            "relatively low sale price."
        )

        st.write(
            "Zero values in garage and basement attributes "
            "are treated separately from these unusually "
            "large-property observations. Their meaning "
            "depends on how the original data was recorded "
            "and cleaned."
        )

    st.divider()

    # Study conclusions
    st.write("### ✅ Study Conclusions")

    st.success(
        "The House Sales Price Study addressed "
        "**Business Requirement 1** by identifying "
        "seven property attributes associated with "
        "house sale prices."
    )

    st.write(
        "**OverallQual** and **GrLivArea** showed the "
        "strongest relationships with SalePrice. "
        "The analysis also supported the three project "
        "hypotheses relating to **overall quality**, "
        "**living area** and **year built**."
    )

    st.write(
        "These findings informed the subsequent "
        "feature engineering and machine learning stages."
    )


if __name__ == "__main__":
    page_house_price_study_body()