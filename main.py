import streamlit as st
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the title of the app
st.title("Streamlit App: Main File Example")

# Example: Access a data file in the repository
data_file_path = os.path.join(current_dir, "data.csv")

# Check if the file exists
if os.path.exists(data_file_path):
    st.success(f"Data file found at: {data_file_path}")
    st.write("You can now process or display the data!")
else:
    st.warning("Data file not found! Please ensure the file exists in the repository.")

# Example of app functionality
st.header("Welcome to Your Streamlit App!")
st.write("This app is built using Streamlit and hosted on GitHub.")

# Simple user input example
user_input = st.text_input("Enter some text:", "Streamlit is awesome!")
st.write(f"You entered: {user_input}")

# Display the main file directory
st.text(f"Main file is located at: {current_dir}")

# Add an image (optional)
image_path = os.path.join(current_dir, "example_image.png")
if os.path.exists(image_path):
    st.image(image_path, caption="Example Image from the Repository")

# Footer
st.sidebar.header("About")
st.sidebar.info("This is a Streamlit app created using Python and hosted on GitHub.")

