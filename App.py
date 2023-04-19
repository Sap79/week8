import pandas as pd
import streamlit as st
import numpy as np
def user_input_numbers():
  first_number = float(st.number_input('First number'))
  second_number = float(st.number_input('Second number'))
  third_number = float(st.number_input('Third number'))
  numbers_list = [first_number,second_number,third_number]
  return numbers_list
st.header('User Input Numbers')
L = user_input_numbers()
max = np.array(L).max()
st.subheader('The maximum number')
st.write('The maximum number is : '+str(max))
