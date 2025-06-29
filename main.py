import streamlit as st
import pandas as pd 
import plotly.express as px


st.set_page_config(page_title="Finance Manager", page_icon="💰", layout="wide")

def load_transaction(file):
    try: 
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        
        st.write(df)
        return df 
    except Exception as e: 
        st.error(f"error: {str(e)}")
        return None 


def main(): 
    st.title("Finance Manager")

    uploadFile = st.file_uploader("Upload your transaction CSV file", type=["csv"])

    if uploadFile is not None: 
        df = load_transaction(uploadFile)

main()

