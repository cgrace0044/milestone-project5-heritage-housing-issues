
import streamlit as st


def page_project_hypothesis_body():

    st.write("### 🌿 Project Hypothesis and Validation")

    st.info(
        "Three hypotheses were tested using Pearson and Spearman "
        "correlation analysis, scatterplots, and heatmaps. "
        "The **House Sales Price Study** page presents these "
        "findings in detail."
    )

    st.write("---")

    # Hypothesis 1
    st.write("#### 🏡 Hypothesis 1 — Overall Quality")

    st.write(
        "Houses with **higher overall quality** are expected "
        "to have higher sale prices."
    )

    st.write(
        "**Validation:** `OverallQual` showed the strongest positive "
        "correlation with `SalePrice` (0.81) of all variables studied."
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
        "**Validation:** `GrLivArea` showed the second strongest "
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
        "**Validation:** `YearBuilt` showed a positive correlation "
        "with `SalePrice` (0.65), although this relationship was "
        "weaker than those observed for overall quality and living area."
    )

    st.success("✓ Supported")

    st.write("---")

    # Overall conclusion
    st.write("#### 📊 Overall Conclusion")

    st.write(
        "The correlation analysis supports all three hypotheses. "
        "Overall quality (0.81) showed the strongest positive "
        "relationship with sale price, followed by above-ground "
        "living area (0.73) and year built (0.65). "
        "These findings suggest that higher-quality, larger and "
        "newer houses tend to achieve higher sale prices in Ames, Iowa. "
    )


if __name__ == "__main__":
    page_project_hypothesis_body()

