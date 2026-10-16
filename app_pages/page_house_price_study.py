import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style('whitegrid')


def load_data():
    train = pd.read_csv(
        'outputs/datasets/cleaned/TrainSetCleaned.csv'
    )

    test = pd.read_csv(
        'outputs/datasets/cleaned/TestSetCleaned.csv'
    )

    return pd.concat([train, test], ignore_index=True)


def scatter_plot_for_eda(df, col, target_var):
    # Filter zero values for selected variables only
    if col in ['GarageArea', 'GarageYrBlt', 'TotalBsmtSF']:
        df = df[df[col] > 0]

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.scatterplot(
        data=df,
        x=col,
        y=target_var,
        ax=ax
    )

    ax.set_title(
        f'{col} vs {target_var}',
        fontsize=20,
        y=1.05
    )

    st.pyplot(fig)
    plt.close(fig)


def heatmap_corr(df, method, threshold=0.4):
    df_corr = df.corr(method=method)

    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(
        df_corr,
        annot=True,
        cmap='viridis',
        mask=abs(df_corr) < threshold,
        annot_kws={'size': 10},
        linewidths=0.5,
        ax=ax
    )

    ax.set_title(f'{method.capitalize()} Correlation Heatmap')

    st.pyplot(fig)
    plt.close(fig)


def page_house_price_study():
    st.title('House Sales Price Study')

    st.write(
        'This page investigates the property attributes most '
        'strongly associated with house sale prices in Ames, Iowa.'
    )

    df = load_data()

    vars_to_study = [
        'OverallQual',
        'GrLivArea',
        'GarageArea',
        'GarageYrBlt',
        'TotalBsmtSF',
        '1stFlrSF',
        'YearBuilt'
    ]

    df_eda = df[vars_to_study + ['SalePrice']]

    st.header('Variables vs Sale Price')

    st.write(
        'Select a property feature to investigate its '
        'relationship with SalePrice.'
    )

    selected_variable = st.selectbox(
        'Select a variable',
        vars_to_study
    )

    scatter_plot_for_eda(
        df_eda,
        selected_variable,
        'SalePrice'
    )

    if selected_variable in [
        'GarageArea',
        'GarageYrBlt',
        'TotalBsmtSF'
    ]:
        st.info(
            'Zero values are excluded from this scatterplot '
            'to make the relationship easier to visualise. '
            'The original dataset remains unchanged.'
        )

    st.header('Correlation Heatmaps')

    st.write(
        'The following heatmaps show the relationships '
        'between the selected features and SalePrice.'
    )

    st.subheader('Spearman Correlation')
    heatmap_corr(df_eda, method='spearman')

    st.subheader('Pearson Correlation')
    heatmap_corr(df_eda, method='pearson')

    st.header('Study Conclusions')

    st.write(
        'OverallQual, GrLivArea, GarageArea, GarageYrBlt, '
        'TotalBsmtSF, 1stFlrSF and YearBuilt were selected '
        'for further investigation based on their '
        'relationships with SalePrice.'
    )

    st.write(
        'The scatterplots also highlight unusual observations, '
        'including properties with large living areas, garages '
        'or basements but relatively low sale prices.'
    )


# Use this if the page is run directly
if __name__ == '__main__':
    page_house_price_study()
