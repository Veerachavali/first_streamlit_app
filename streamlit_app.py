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
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)),[Avocado,strawberries]
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

