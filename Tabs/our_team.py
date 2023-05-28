import streamlit as st

def app():
    st.title("Our Team 💻")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This Website is created by  <b style="color:red">4 individuals who still has lot to learn</b> 
            </p>
            
        """, unsafe_allow_html=True)
    st.image("./images/akshat_photo.jpg", width  = 350)
    st.markdown(
        """
             <p style="font-size:25px">
               <b style="color:green">
                 Upcoming SDE at Transunion</b>
                <br>  
                <a href="https://www.linkedin.com/in/akshatbhatnagar17">Akshat Bhatnagar</a>
                <hr>
            </p>
        """, unsafe_allow_html=True)
    st.image("./images/alok_photo.jpg", width  = 300)
    st.markdown(
        """
            <p style="font-size:25px">
            <b style="color:green">
                Upcoming SDE at Cavisson</b>
                <br>  
                <a href="https://www.linkedin.com/in/alokmaurya30/">Alok Maurya</a>
                <hr>
            </p>
            
        """, unsafe_allow_html=True)

    st.image("./images/abhishek_photo.jpg", width  = 300)
    st.markdown(
        """
            <p style="font-size:25px">
            <b style="color:green">
                Upcoming SDE at Cavisson</b>
                <br>  
                <a href="https://www.linkedin.com/in/abhishek-kumar-6197131ab">Abhishek Kumar</a>
                <hr>
            </p>
            
        """, unsafe_allow_html=True)
    st.image("./images/amit_photo.jpg", width  = 300)
    st.markdown(
        """
            <p style="font-size:25px">
            <b style="color:green">
                Upcoming SDE at Cavisson</b>
                <br>  
                <a href="https://www.linkedin.com/in/amit-agrahari-2b94351a0">Amit Agrahari</a>
                <hr>
            </p>
            
        """, unsafe_allow_html=True)
