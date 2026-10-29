
import streamlit as st


def page_project_hypothesis_body():

    st.write("### 🌿 Project Hypothesis and Validation")

    st.divider()

    # Hypothesis 1
    col1, col2 = st.columns([4, 1], vertical_alignment="center")

    with col1:
        st.markdown("#### 🏡 Hypothesis 1 — Overall Quality")
        st.write(
            "Houses with **higher overall quality** are "
            "expected to have higher sale prices.\n\n"
            "**Validation:** Positive correlation between "
            "`OverallQual` and `SalePrice`."
        )

    with col2:
        st.success("✓ Supported")

    st.divider()

    # Hypothesis 2
    col1, col2 = st.columns([4, 1], vertical_alignment="center")

    with col1:
        st.markdown("#### 📐 Hypothesis 2 — Living Area")
        st.write(
            "Houses with **larger living areas** are "
            "expected to have higher sale prices.\n\n"
            "**Validation:** Positive correlation between "
            "`GrLivArea` and `SalePrice`."
        )

    with col2:
        st.success("✓ Supported")

    st.divider()

    # Hypothesis 3
    col1, col2 = st.columns([4, 1], vertical_alignment="center")

    with col1:
        st.markdown("#### 📅 Hypothesis 3 — Year Built")
        st.write(
            "**Newer houses** are expected to have "
            "higher sale prices.\n\n"
            "**Validation:** Positive correlation between "
            "`YearBuilt` and `SalePrice`."
        )

    with col2:
        st.success("✓ Supported")

    st.divider()

    st.write(
        "**Conclusion:** All three hypotheses were "
        "supported by the correlation analysis."
    )


if __name__ == "__main__":
    page_project_hypothesis_body()
