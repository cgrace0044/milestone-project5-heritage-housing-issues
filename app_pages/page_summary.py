
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

    # Project information
    st.write("### 📚 Project Information")

    st.info(
        "**Project Dataset**\n"
        "* **1,460 historical houses** in Ames, Iowa, "
        "with 23 house attributes and recorded sale prices.\n"
        "* **4 inherited houses** with house attributes "
        "but no recorded sale prices.\n"
        "* The project uses publicly available data."
    )

    # Optional terminology
    with st.expander("📖 Project Terms & Jargon"):
        st.write(
            "* **SalePrice:** The price at which a house was sold.\n"
            "* **House attributes:** Property characteristics such as "
            "living area, overall quality, year built, garage area "
            "and basement size.\n"
            "* **Correlation:** A measure of how strongly two "
            "variables are related. It helps identify which house "
            "attributes are associated with sale prices.\n"
            "* **Regression:** A machine learning technique used "
            "to predict numerical values, such as house prices.\n"
            "* **R² Score:** A measure of how well the model "
            "explains differences in house prices. A higher "
            "score generally indicates better performance."
        )

    st.divider()

    # Business requirements
    st.write("### 🎯 Business Requirements")

    st.success(
        "The project has **2 business requirements**:\n\n"
        "* **1 -** The client wants to understand how "
        "**house attributes correlate with sale prices**, "
        "using data visualisations.\n\n"
        "* **2 -** The client wants to **predict sale prices** "
        "for her **4 inherited houses** and other houses "
        "in Ames, Iowa."
    )

    st.divider()

    # Project success criteria
    st.write("### 📈 Project Success Criteria")

    st.success(
        "**Target:** R² ≥ 0.75 on both datasets.\n\n"
        "* **Training R²:** 0.912 ✅\n"
        "* **Test R²:** 0.808 ✅\n\n"
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


if __name__ == "__main__":
    page_summary_body()
