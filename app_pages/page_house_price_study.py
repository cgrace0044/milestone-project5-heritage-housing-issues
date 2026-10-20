
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")


# Load historical housing data
def load_data():
    train = pd.read_csv(
        "outputs/datasets/cleaned/TrainSetCleaned.csv"
    )

    test = pd.read_csv(
        "outputs/datasets/cleaned/TestSetCleaned.csv"
    )

    return pd.concat([train, test], ignore_index=True)


# Load the four inherited houses
def load_inherited_houses():
    return pd.read_csv(
        "outputs/datasets/collection/inherited_houses.csv"
    )


# Scatterplot function
def scatter_plot_for_eda(df, col, target_var):

    # Exclude zero values from selected scatterplots
    if col in ["GarageArea", "GarageYrBlt", "TotalBsmtSF"]:
        df = df[df[col] > 0]

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.scatterplot(
        data=df,
        x=col,
        y=target_var,
        ax=ax
    )

    ax.set_title(
        f"{col} vs {target_var}",
        fontsize=20,
        y=1.05
    )

    st.pyplot(fig)
    plt.close(fig)


# Correlation heatmap function
def heatmap_corr(df, method, threshold=0.4):

    df_corr = df.corr(method=method)

    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(
        df_corr,
        annot=True,
        cmap="viridis",
        mask=abs(df_corr) < threshold,
        annot_kws={"size": 10},
        linewidths=0.5,
        ax=ax
    )

    ax.set_title(
        f"{method.capitalize()} Correlation Heatmap"
    )

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

    # Inspect datasets
    st.write("### 📂 Inspect Housing Datasets")

    if st.checkbox("Inspect Historical Housing Dataset"):

        st.write(
            f"The historical dataset contains "
            f"**{df.shape[0]} houses** and "
            f"**{df.shape[1]} columns**. "
            "The first 10 rows are shown below."
        )

        st.dataframe(df.head(10))

    if st.checkbox("Inspect Four Inherited Houses"):

        inherited_houses = load_inherited_houses()

        st.write(
            f"The inherited housing dataset contains "
            f"**{inherited_houses.shape[0]} houses** and "
            f"**{inherited_houses.shape[1]} columns**."
        )

        st.dataframe(inherited_houses)

    st.divider()

    # Variables selected in the correlation study notebook
    vars_to_study = [
        "OverallQual",
        "GrLivArea",
        "GarageArea",
        "GarageYrBlt",
        "TotalBsmtSF",
        "1stFlrSF",
        "YearBuilt"
    ]

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

    # Interpretation from Jupyter notebook - Section 5.3
    st.info(
        "**Correlation Study Interpretation**\n\n"
        "We can conclude from the above results that the "
        "following variables are associated with a higher sale price:\n\n"
        "- Higher overall property quality (`OverallQual`)\n"
        "- Larger living areas (`GrLivArea`)\n"
        "- Larger garages (`GarageArea`)\n"
        "- Properties with newer garages (`GarageYrBlt`)\n"
        "- Larger basement areas (`TotalBsmtSF`)\n"
        "- Larger first-floor areas (`1stFlrSF`)\n"
        "- Newer properties (`YearBuilt`)"
    )

    st.write(
        "OverallQual and GrLivArea showed the strongest "
        "relationships with SalePrice across both "
        "Pearson and Spearman correlation methods."
    )

    st.divider()

    # Prepare data for visual analysis
    df_eda = df[vars_to_study + ["SalePrice"]]

    # Individual scatterplots
    st.write("### 📈 Variables vs Sale Price")

    st.write(
        "The selected variables are plotted against SalePrice "
        "to examine their relationships and identify any "
        "unusual observations. Select a variable below "
        "to explore the results."
    )

    selected_variable = st.selectbox(
        "Select a property attribute",
        vars_to_study
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
            "to make the relationship with SalePrice easier "
            "to visualise."
        )

    st.divider()

    # Correlation heatmaps
    st.write("### 🔥 Correlation Heatmaps")

    st.write(
        "Pearson and Spearman correlation heatmaps provide "
        "an overview of the relationships between the "
        "selected variables and SalePrice. "
        "Correlations with an absolute value below 0.4 "
        "are hidden for clarity."
    )

    st.subheader("Spearman Correlation")

    heatmap_corr(
        df_eda,
        method="spearman"
    )

    st.subheader("Pearson Correlation")

    heatmap_corr(
        df_eda,
        method="pearson"
    )

    st.divider()

    # EDA interpretation from Jupyter notebook
    st.write("### 🔍 EDA Interpretation")

    st.write(
        "The scatterplots and heatmaps support the findings "
        "from the correlation study."
    )

    st.write(
        "The heatmaps also show strong correlations between "
        "YearBuilt and GarageYrBlt, and between "
        "TotalBsmtSF and 1stFlrSF."
    )

    st.write(
        "The scatterplots highlight some outliers "
        "in the dataset:"
    )

    st.markdown(
        "- **GrLivArea:** A couple of very large properties "
        "have relatively low SalePrice.\n"
        "- **GarageArea:** A small number of properties "
        "have very large garages and relatively low SalePrice.\n"
        "- **TotalBsmtSF:** One property has a very large "
        "basement and relatively low SalePrice."
    )

    st.write(
        "GarageYrBlt, GarageArea and TotalBsmtSF contain "
        "zero values representing properties without a "
        "garage or basement, so these are not considered "
        "true outliers."
    )

    st.divider()

    # Study conclusions
    st.write("### ✅ Study Conclusions")

    st.success(
        "The House Sales Price Study answered "
        "**Business Requirement 1** by identifying "
        "the property attributes most strongly "
        "associated with SalePrice."
    )

    st.write(
        "OverallQual and GrLivArea showed the strongest "
        "relationships with SalePrice across both "
        "Pearson and Spearman correlation methods. "
        "GarageArea, GarageYrBlt, TotalBsmtSF, "
        "1stFlrSF and YearBuilt were also identified "
        "as important variables."
    )

    st.write(
        "The scatterplots identified a small number of "
        "outliers, which are to be expected. "
        "The heatmaps highlighted strong correlations "
        "between some of the property features."
    )

    st.write(
        "These findings were considered during the "
        "feature engineering and machine learning stages."
    )


if __name__ == "__main__":
    page_house_price_study_body()
