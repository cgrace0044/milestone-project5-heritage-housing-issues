
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def page_house_price_study_body():

    # Load cleaned training and test datasets
    df_train = pd.read_csv("outputs/datasets/cleaned/TrainSetCleaned.csv")
    df_test = pd.read_csv("outputs/datasets/cleaned/TestSetCleaned.csv")
    df = pd.concat([df_train, df_test], ignore_index=True)

    # Selected variables from House Sales Price Study notebook
    vars_to_study = [
        "OverallQual",
        "GrLivArea",
        "GarageArea",
        "GarageYrBlt",
        "TotalBsmtSF",
        "1stFlrSF",
        "YearBuilt"
    ]

    st.write("### 🏡 House Sales Price Study")

    st.info(
        "The client is interested in discovering how house attributes "
        "correlate with sale prices. The findings below highlight "
        "the most relevant attributes."
    )

    # Inspect data
    if st.checkbox("Inspect Housing Dataset"):
        st.write(
            f"The dataset has **{df.shape[0]} rows** and "
            f"**{df.shape[1]} columns**. "
            "The first 10 rows are shown below."
        )
        st.dataframe(df.head(10))

    st.divider()

    # Correlation study summary
    st.write("### 📊 Correlation Study Summary")

    st.write(
        "A correlation study was conducted in the House Sales Price Study "
        "notebook to identify the house attributes most strongly related "
        "to sale prices."
    )

    st.write(
        "**Selected attributes:** "
        + ", ".join(vars_to_study)
    )

    st.info(
        "The correlation study indicates that:\n"
        "* Houses with higher overall quality generally have higher sale prices.\n"
        "* Larger living areas are generally associated with higher sale prices.\n"
        "* Houses with larger garages and basements tend to have higher sale prices.\n"
        "* Newer houses generally have higher sale prices."
    )

    # Select variables for visualisation
    df_eda = df.filter(vars_to_study + ["SalePrice"])

    st.divider()

    # Correlation heatmap
    if st.checkbox("Show Correlation Heatmap"):
        plot_correlation_heatmap(df_eda)

    # Individual plots
    if st.checkbox("Sale Price per Variable"):
        sale_price_per_variable(df_eda)


# Function adapted from Code Institute walkthrough
def sale_price_per_variable(df_eda):

    target_var = "SalePrice"

    for col in df_eda.drop(columns=[target_var]).columns:
        if df_eda[col].dtype == "object":
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)


# Categorical plots
def plot_categorical(df, col, target_var):

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.boxplot(data=df, x=col, y=target_var, ax=ax)

    ax.set_title(f"{col} vs SalePrice")
    ax.tick_params(axis="x", rotation=90)

    st.pyplot(fig)
    plt.close(fig)


# Numerical plots
def plot_numerical(df, col, target_var):

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.scatterplot(data=df, x=col, y=target_var, ax=ax)

    ax.set_title(f"{col} vs SalePrice")

    st.pyplot(fig)
    plt.close(fig)


# Correlation heatmap
def plot_correlation_heatmap(df_eda):

    fig, ax = plt.subplots(figsize=(10, 7))

    correlation_matrix = df_eda.corr(numeric_only=True)

    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        ax=ax
    )

    ax.set_title("Correlation Heatmap of House Attributes and Sale Price")

    st.pyplot(fig)
    plt.close(fig)
