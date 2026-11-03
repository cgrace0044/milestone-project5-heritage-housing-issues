import streamlit as st


def page_project_hypothesis_body():

    st.write("### 🌿 Project Hypothesis and Validation")

    st.info(
        "Three hypotheses were tested using correlation analysis "
        "and scatterplots. The Spearman correlation heatmap and "
        "supporting scatterplots are available on the "
        "**House Sales Price Study** page."
    )

    st.write("---")

    # Hypothesis 1
    st.write("#### 🏡 Hypothesis 1 — Overall Quality")

    st.write(
        "Houses with **higher overall quality** are expected "
        "to have higher sale prices."
    )

    st.write(
        "**Validation:** `OverallQual` had the strongest positive "
        "correlation with `SalePrice` (0.81)."
    )

    st.success("✓ Supported")

    st.write("---")

    # Hypothesis 2
    st.write("#### 📐 Hypothesis 2 — Living Area")

    st.write(
        "Houses with **larger living areas** are expected "
        "to have higher sale prices."
    )

    st.write(
        "**Validation:** `GrLivArea` had the second strongest "
        "positive correlation with `SalePrice` (0.73)."
    )

    st.success("✓ Supported")

    st.write("---")

    # Hypothesis 3
    st.write("#### 📅 Hypothesis 3 — Year Built")

    st.write(
        "**Newer houses** are expected to have higher sale prices."
    )

    st.write(
        "**Validation:** `YearBuilt` had a positive correlation "
        "with `SalePrice` (0.65), joint third strongest "
        "with `GarageArea`."
    )

    st.success("✓ Supported")


if __name__ == "__main__":
    page_project_hypothesis_body()