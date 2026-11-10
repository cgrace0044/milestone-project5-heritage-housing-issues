import streamlit as st
import pandas as pd
import joblib


@st.cache_data
def load_housing_data():
    df = pd.read_csv(
        "outputs/datasets/cleaned/TrainSetCleaned.csv"
    )
    return df


@st.cache_data
def load_housing_study_data():
    train = pd.read_csv(
        "outputs/datasets/cleaned/TrainSetCleaned.csv"
    )
    test = pd.read_csv(
        "outputs/datasets/cleaned/TestSetCleaned.csv"
    )
    return pd.concat([train, test], ignore_index=True)


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
