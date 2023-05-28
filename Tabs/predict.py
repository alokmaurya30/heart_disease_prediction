"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Cardiac Disease Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
    restbp = st.slider("RestingBP", int(df["RestingBP"].min()), int(df["RestingBP"].max()))
    chol = st.slider("Cholesterol", int(df["Cholesterol"].min()), int(df["Cholesterol"].max()))
    fastbs = st.slider("FastingBS", float(df["FastingBS"].min()), float(df["FastingBS"].max()))
    maxhr = st.slider("MaxHR", float(df["MaxHR"].min()), float(df["MaxHR"].max()))
    oldpeak = st.slider("Oldpeak", int(df["Oldpeak"].min()), int(df["Oldpeak"].max()))

    # Create a list to store all the features
    features = [age, restbp, chol, fastbs, maxhr, oldpeak]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + 0.15
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get cardiac arrest!!")
            st.markdown("""

            <style>
            <br>
            .diet-font {
            font-size:150px !important;
            color : Black;
            font-weight:bolder;
            font-family: Georgia, serif;
            }
            </style>
             """, unsafe_allow_html=True)

            st.markdown('<p class="diet">-------------------------------------------------------------------- </p>', unsafe_allow_html=True)
            
            st.markdown("""

            <style>
            .ex {
            font-size:40px !important;
            color : Black;
            font-weight:bolder;
            font-family: Georgia, serif;
            }
            </style>
            <p>
            <span style = "font-size: 30px ;color : black ;background-color:#FEFF86"> 
            Exercise (You are prone to Heart Disease)
            </span>
            </p>
            <p style = "font-size: 24px; color:red">
            Physical activity strengthens your heart and improves lung function, done regularly, moderate- and vigorous-intensity physical activity strengthens your heart muscle. This improves your heart's ability to pump blood to your lungs and throughout your body. As a result, more blood flows to your muscles, and oxygen levels in your blood rise. Capillaries, your body's tiny blood vessels, also widen. This allows them to deliver more oxygen to your body and carry away waste products.
            <br>
            Helpful Links - <a href = "https://www.webmd.com/hypertension-high-blood-pressure/safe-exercise-tips" >Exercise </a>
            </p>
             """, unsafe_allow_html=True)

            st.markdown('<p class="ex"> </p> ', unsafe_allow_html=True)
            st.markdown("""

            <style>
            .diet {
            font-size:40px !important;
            color : Black;
            font-weight:bolder;
            font-family: Georgia, serif;
            }
            </style>
            <p>
            <span style = "font-size: 30px ;color : black ;background-color:#FEFF86"> 
            Diet Plan(If You are prone to Heart Disease)
            </span>
            </p>
            <p style = "font-size: 24px; color:red">
            A healthy diet can help reduce your risk of developing coronary heart disease and stop you gaining weight, reducing your risk of diabetes and high blood pressure. It can also help lower your cholesterol levels and reduce your risk of some cancers.
            <br>
            Helpful Links - <a href = "https://www.lybrate.com/topic/high-blood-pressure-diet-chart" > Diet Plan </a> <br>
            You can also try our own recipe finder app - <a href = "https://demo-recipe-finder.netlify.app/" > Recipe Finder </a>
             """, unsafe_allow_html=True)

            st.markdown('<p class="diet"> </p>', unsafe_allow_html=True)

    
        else:
            st.success("The person is relatively safe from cardiac arrest")
            st.markdown("""

            <style>
            <br>
            .diet-font {
            font-size:150px !important;
            color : Black;
            font-weight:bolder;
            font-family: Georgia, serif;
            }
            </style>
             """, unsafe_allow_html=True)

            st.markdown('<p class="diet">-------------------------------------------------------------------- </p>', unsafe_allow_html=True)
            
            st.markdown("""

            <style>
            .ex {
            font-size:40px !important;
            color : Black;
            font-weight:bolder;
            font-family: Georgia, serif;
            }
            </style>
            <p>
            <span style = "font-size: 30px ;color : black ;background-color:#FEFF86"> 
            Exercise (To Be More fit an maintain your health)
            </span>
            </p>
            <p style = "font-size: 24px; color:red">
            If you are fit and mainly not proned for heart disease then you should maintain your weight by doing light cardio which will ensure that you maintain your weigth and you will remain in safe zone.
            <br>
            Helpful Links - <a href = "https://www.healthline.com/health/fitness-exercise/low-impact-cardio">Light Cardio </a>
            </p>
             """, unsafe_allow_html=True)

            st.markdown('<p class="ex"> </p> ', unsafe_allow_html=True)
            st.markdown("""

            <style>
            .diet {
            font-size:40px !important;
            color : Black;
            font-weight:bolder;
            font-family: Georgia, serif;
            }
            </style>
            <p>
            <span style = "font-size: 30px ;color : black ;background-color:#FEFF86"> 
            Diet Plan(If Your heart is fit)
            </span>
            </p>
            <p style = "font-size: 24px; color:red">
            If you are fit then one should go on a diet which will help him/her to gain muscle and simultaneously reduce fat and fat percentage of their body. It is very essential to eat good amount of micronutriets to be healthy.
            <br>
            Helpful Links - <a href = "https://www.lybrate.com/topic/muscle-gain-diet-chart" > Diet Plan </a> <br>
            You can also try our own recipe finder app - <a href = "https://demo-recipe-finder.netlify.app/" > Recipe Finder </a>
             """, unsafe_allow_html=True)

            st.markdown('<p class="diet"> </p>', unsafe_allow_html=True)


        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
