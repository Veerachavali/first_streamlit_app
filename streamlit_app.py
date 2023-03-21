import streamlit

streamlit.title('my parents new helthy diner')


streamlit.header('Breakfast Favorites')

streamlit.text('🍞omega3 & Blueberry otameal')
streamlit.text('🥑kale,spinch,rocket smoothy')
streamlit.text('🐔Hard boiled-free range egg')
streamlit.text('🥑🥗Avacodo Toste')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = my_fruit_list.set_index('Fruit')

