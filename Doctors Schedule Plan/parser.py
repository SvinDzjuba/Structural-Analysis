import streamlit as st
import pandas as pd
import numpy as np
import json


with open('doctors.json', 'r') as file:
    data = json.load(file)

headings = []
doctors = 0
speciality = 0
cities = []

for i in data['city']:
    for j in i['speciality']:
        for k in j['doctor']:
            doctors += 1


for i in data['city']:
    cities.append(i['name'])
print(cities)

for i in data['city']:
    for j in i['speciality']:
        speciality = j

for i in data:
    headings.append(i)

print(headings)

df = pd.DataFrame(
    data=data,
)

st.write(df)