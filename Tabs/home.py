"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.markdown("""

    <style>
    .big-font {
    font-size:70px !important;
    color : Black;
    font-weight:bolder;
    font-family: Georgia, serif;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font"> Heart Disease Prediction 💗</p>', unsafe_allow_html=True)
    st.image("./images/home.png",width =1050)
    # Add image to the home page

    # Add brief describtion of your web app
    st.markdown(
    """
       <p>
         <span style = "font-size: 30px ;color : black ;background-color:#FEFF86"> 
            What is Heart Attack and why it happens ? 
         </span>
       </p>
        <p style="font-size:24px ; color :red"> 
            A heart attack, also called a myocardial infarction, <b style = "color:green">happens when a part of the heart muscle doesn't get enough blood</b>. The more time that passes without treatment to restore blood flow, the greater the damage to the heart muscle. Coronary artery disease (CAD) is the main cause of heart attack

        </p>

        <p>
         <span style = "font-size: 30px ;color : black ;background-color:#FEFF86"> 
            How can we help ? 
         </span>
        </p>
        <p style="font-size:24px ; color :red"> 
            This Web app will help you to <b style="color:green"> predict whether a person has chances of cardiac arrest or is prone to </b> get it in future by analysing the values of several features using the Decision Tree Classifier.
            We also provide <b style="color:green"> suitable links for healthy diets and workout routines. </b>
        </p>

        <p>
         <span style = "font-size: 30px ;color : black ;background-color:#FEFF86"> 
            Symptoms to watch out for: 
         </span>
        </p>
        <p> 
            <ul>
                <li style="font-size:24px ; color :red">Chest pain or discomfort </li> 
                <li style="font-size:24px ; color :red">Shortness of breath </li>
                <li style="font-size:24px ; color :red">Pain or discomfort in the jaw, neck, back, arm, or shoulder </li> 
                <li style="font-size:24px ; color :red">Feeling nauseous, light-headed, or unusually tired </li>
            </ul>
        </p>
    """, unsafe_allow_html=True)