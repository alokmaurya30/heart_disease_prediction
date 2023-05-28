"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st
from Tabs import our_team

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict, visualise, contact_form, our_team

# Configure the app
st.set_page_config(
    page_title = 'Cardiac Disease Prediction',
    page_icon = 'heart',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Tabs = {
    "HOME": home,
    "DATA INFO": data,
    "PREDICTION": predict,
    "VISUALISATION": visualise,
    "CONTACT-FORM": contact_form,
    "OUR TEAM" : our_team
}
# Create a sidebar
# Add title to sidear

st.sidebar.title("Manoeuvre")
# Create radio option to select the page
page = st.sidebar.radio("", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["PREDICTION", "VISUALISATION"]:
    Tabs[page].app(df, X, y)
elif (page == "DATA INFO"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
