import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)


option = option_menu(
    menu_title = None,
    options = [ "Recipe Generator", "Steps Generator" ],
    icons = [ "list", "list" ],
    orientation = "horizontal",
)
st.title( "Recipe Generator" )

if option == "Steps Generator":
    recipe_name = st.text_input( "Recipe Name" )

    response = model.generate_content( "You are a world class chef. Please generate a detailed recipe for: " + recipe_name )
    st.write( response.text )

elif option == "Recipe Generator":
    description = st.text_area( " Enter Description of the recipe" )

    response = model.generate_content( "You are a world class chef. Please generate a detailed recipe for: " + description )
    st.write( response.text )
