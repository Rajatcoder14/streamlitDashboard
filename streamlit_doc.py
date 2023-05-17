import streamlit as st

import pandas as pd

import time


st.title('Startup Dashboard')

st.header('I am learning Streamlit')

st.subheader('My name is Rajat')

st.write('This is noraml text')


st.markdown("""
### My Favorite Movies
- Iron man
- X man
- Batman
""")


st.code("""
def foo(input):
    return foo**2
x=foo(2)
""")

st.latex('x^2+y^2=0')

df=pd.DataFrame({'Name':['Rajat','Nitesh','Rohit'],
                 "mark":[87,67,75],
                 'package':[10,7,8]})




st.dataframe(df)



st.metric('Revenue','Rs 3L','3%')



st.json({'Name':['Rajat','Nitesh','Rohit'],
                 "mark":[87,67,75],
                 'package':[10,7,8]})



st.image('Default.jpg')
# st.vedio()
# st.audio()

st.sidebar.title('sidebar ka title')


col1 ,col2 = st.columns(2)
with col1:
    st.image('Default.jpg')
with col2:
    st.image('Default.jpg')



st.error('Login failed')

st.success('Login failed')

st.info('Login failed')

st.warning('Login failed')

bar=st.progress(0)
for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)


email=st.text_input('Enter a email')

number=st.number_input('Enter your age')

date=st.date_input('Entar your date of birth')



email=st.text_input('Enter Email')
password=st.text_input('Enter Password')
gender=st.selectbox('select gender',['Male','female','others'])

btn=st.button('Login')
# if the bottom click
if btn:
    if email=='rajatkumar@gmail.com' and password=='12345':
        st.success('Login successful')
        st.balloons()
        st.write(gender)


    else:
        st.error('Login Failed')



file=st.file_uploader('upload a csv file')

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())