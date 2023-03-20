import streamlit
streamlit.title('my parents new helthy diner')
streamlit.header('🥣Breakfast Menu')
streamlit.text('🐔omega3 & Blueberry otameal')
streamlit.text('🥗kale,spinch,rocket smoothy')
streamlit.text('🥑🍞Hard boiled-free range egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe('my_fruit_list')
