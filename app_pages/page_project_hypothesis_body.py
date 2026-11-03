import streamlit as st


def page_project_hypothesis_body():

    st.write("### 🌿 Project Hypothesis and Validation")

    st.info(
        "Three hypotheses were tested using Pearson and "
        "Spearman correlation analysis and scatterplots "
        "to investigate relationships between house "
        "attributes and sale prices."
    )

    st.write("---")

    # Hypothesis 1
    st.write("#### 🏡 Hypothesis 1 — Overall Quality")

    st.write(
        "Houses with **higher overall quality** are expected "
        "to have higher sale prices."
    )

    st.write(
        "**Validation:** Correlation analysis and scatterplots "
        "showed a strong positive relationship between "
        "`OverallQual` and `SalePrice`. Higher-quality houses "
        "generally achieved higher sale prices."
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
        "**Validation:** Correlation analysis and scatterplots "
        "showed a positive relationship between `GrLivArea` "
        "and `SalePrice`. Prices generally increased with "
        "living area, although some unusually large houses "
        "had lower sale prices."
    )

    st.success("✓ Supported")

    st.write("---")

    # Hypothesis 3
    st.write("#### 📅 Hypothesis 3 — Year Built")

    st.write(
        "**Newer houses** are expected to have higher sale prices."
    )

    st.write(
        "**Validation:** Correlation analysis and scatterplots "
        "showed a positive relationship between `YearBuilt` "
        "and `SalePrice`. Newer houses generally sold for "
        "higher prices than older houses."
    )

    st.success("✓ Supported")

    st.write("---")

    st.write(
        "**Conclusion:** All three hypotheses were supported "
        "by the correlation analysis and scatterplots. "
        "The supporting visualisations can be explored on "
        "the **House Sales Price Study** page."
    )


if __name__ == "__main__":
    page_project_hypothesis_body()