import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# -------- Google Sheet Connection --------

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)

client = gspread.authorize(creds)

sheet = client.open("StreamlitData").sheet1


# -------- Streamlit UI --------

st.title("Simple Data Form")

name = st.text_input("Enter Name")
email = st.text_input("Enter Email")

if st.button("Submit"):
    sheet.append_row([name, email])
    st.success("Data sent to Google Sheet ✅")
import os

port = int(os.environ.get("PORT", 8501))

# Streamlit run configuration
if __name__ == "__main__":
    os.system(f"streamlit run app.py --server.port {port} --server.address 0.0.0.0")
