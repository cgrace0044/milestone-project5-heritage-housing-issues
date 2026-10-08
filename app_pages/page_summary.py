
import streamlit as st


def page_summary_body():

    st.write("### 🏡 Quick Project Summary")

    # Project introduction
    st.write(
        "Lydia Doe has inherited four houses in Ames, Iowa, USA. "
        "As she is unfamiliar with the local housing market, she wants "
        "to understand their value before selling them. "
        "This project investigates how house attributes relate to sale prices "
        "and uses machine learning to predict the sale prices of her "
        "inherited houses."
    )

    st.divider()

    # Project overview
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏠 Historical Houses", "1,460")

    with col2:
        st.metric("🔑 Inherited Houses", "4")

    with col3:
        st.metric("🎯 Business Requirements", "2")

    st.divider()

    # Project information
    st.write("### 📚 Project Information")

    st.info(
        "**Project Terms & Jargon**\n"
        "* **SalePrice** is the price at which a house was sold.\n"
        "* **House attributes** are characteristics of a property, "
        "such as living area, overall quality, year built, number of bedrooms, "
        "garage area, basement size, kitchen quality, and lot size.\n"
        "* **Correlation** describes the relationship between "
        "house attributes and sale prices.\n"
        "* **Regression** is a machine learning technique used "
        "to predict numerical values, such as house sale prices.\n"
        "* **Data visualisation** is the use of charts and graphs "
        "to show patterns and relationships in the data.\n\n"

        "**Project Dataset**\n"
        "* The project uses a publicly available housing dataset from "
        "Ames, Iowa, containing **1,460 houses**, with **23 house attributes** "
        "and their respective sale prices.\n"
        "* A separate dataset contains **4 inherited houses**, "
        "with the same 23 house attributes but no recorded sale prices.\n"
        "* As the project uses publicly available data, "
        "no privacy concerns have been identified."
    )

    st.divider()

    # Business requirements
    st.write("### 🎯 Business Requirements")

    st.success(
        "The project has 2 business requirements:\n"
        "* **1 -** The client is interested in discovering how house "
        "attributes correlate with sale prices. Therefore, the client "
        "expects data visualizations of the correlated variables "
        "against the sale price.\n"
        "* **2 -** The client is interested in predicting the house "
        "sale prices from her 4 inherited houses, and any other "
        "house in Ames, Iowa."
    )

    st.divider()

    # Project success criteria
    st.write("### 📈 Project Success Criteria")

    st.info(
        "The project aims to develop a regression model capable of "
        "predicting house sale prices with an **R² score of at least 0.75** "
        "on both the training and test datasets."
    )

    st.divider()

    # Project documentation
    st.write("### 📖 Project Documentation")

    st.write(
        "* For additional information, please read the "
        "[Project README file]"
        "(https://github.com/cgrace0044/milestone-project5-heritage-housing-issues)."
    )

