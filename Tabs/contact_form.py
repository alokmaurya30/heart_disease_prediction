"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    
    """This function create the home page"""

    st.header(":mailbox: Get In Touch With US!")


    contact_form = """
    <form action="https://formsubmit.co/alokmaurya3000@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("Tabs/style/style.css")