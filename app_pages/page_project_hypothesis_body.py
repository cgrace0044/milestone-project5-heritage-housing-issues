import streamlit as st


def page_project_hypothesis_body():

    st.write("### 🌿 Project Hypothesis and Validation")

    st.write(
        "Three hypotheses were investigated in the "
        "House Sales Price Study."
    )

    st.divider()

    # Hypothesis 1
    col1, col2 = st.columns([4, 1], vertical_alignment="center")

    with col1:
        st.markdown("#### 🏡 Hypothesis 1 — Overall Quality")
        st.write(
            "I suspect houses with **higher overall property "
            "quality** have higher sale prices."
        )
        st.write(
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
            "I suspect houses with **larger above-ground "
            "living areas** have higher sale prices."
        )
        st.write(
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
            "I suspect **newer houses** have higher sale prices."
        )
        st.write(
            "**Validation:** Positive correlation between "
            "`YearBuilt` and `SalePrice`."
        )

    with col2:
        st.success("✓ Supported")

    st.divider()

    st.write(
        "**Conclusion:** All three hypotheses were supported "
        "by the correlation analysis in the "
        "House Sales Price Study."
    )