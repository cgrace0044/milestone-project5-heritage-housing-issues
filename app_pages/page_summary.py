import streamlit as st


def page_summary_body():

    st.write("### 🏡 Quick Project Summary")

    # Project introduction
    st.write(
        "Lydia Doe has inherited four houses in Ames, Iowa, USA. "
        "She wants to understand their value before selling them. "
        "This project explores how house attributes relate to sale prices "
        "and uses machine learning to predict the value of her "
        "inherited properties."
    )

    st.divider()

    # Project overview
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏠 Historical Houses", "1,460")

    with col2:
        st.metric("🔑 Inherited Houses", "4")

    with col3:
        st.metric("📈 Test R² Score", "0.813")

    st.divider()

    # Project information
    st.write("### 📚 Project Information")

    st.info(
        "**Project Dataset**\n"
        "* **1,460 historical houses** in Ames, Iowa, "
        "with 23 house attributes and recorded sale prices.\n"
        "* **4 inherited houses** with the same attributes "
        "but no recorded sale prices.\n"
        "* The project uses publicly available data."
    )

    # Optional terminology
    with st.expander("📖 Project Terms & Jargon"):
        st.write(
            "* **SalePrice:** The price at which a house was sold.\n"
            "* **House attributes:** Property characteristics such as "
            "living area, overall quality, year built, garage area, "
            "basement size and kitchen quality.\n"
            "* **Correlation:** A statistical measure describing the "
            "strength and direction of the relationship between two "
            "variables. In this project, it helps identify which house "
            "attributes are associated with higher or lower sale prices.\n"
            "* **Regression:** A machine learning technique used "
            "to predict numerical values, such as house prices."
        )

    st.divider()

    # Business requirements
    st.write("### 🎯 Business Requirements")

    st.success(
        "The project has **2 business requirements**:\n\n"
        "* **1 -** The client is interested in discovering how "
        "**house attributes correlate with sale prices**. "
        "Therefore, the client expects **data visualizations** "
        "of the correlated variables against the sale price.\n\n"
        "* **2 -** The client is interested in **predicting the house "
        "sale prices** from her **4 inherited houses**, and "
        "**any other house in Ames, Iowa**."
    )

    st.divider()

    # Project success criteria
    st.write("### 📈 Project Success Criteria")

    st.success(
        "**Target:** R² ≥ 0.75 on both datasets.\n\n"
        "* **Training R²:** 0.923 ✅\n"
        "* **Test R²:** 0.813 ✅\n\n"
        "**Outcome:** Both performance targets achieved."
    )

    st.divider()

    # Project documentation
    st.write("### 📖 Project Documentation")

    st.write(
        "For more information, visit the "
        "[Project README]"
        "(https://github.com/cgrace0044/milestone-project5-heritage-housing-issues)."
    )