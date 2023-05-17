import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout='wide',page_title='StartUp Analysis')


df=pd.read_csv('startup.csv')
# convert date to year
df['date']= pd.to_datetime(df["date"])
df['year'] = df['date'].dt.strftime('%Y')
df['month'] = df['date'].dt.month

def load_overall_analysis():
    st.title('Overall Analysis')

    # total invest amount
    total=round(df['amount'].sum())
    max_ = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    avg_=round(df.groupby('startup')['amount'].sum().mean())
    total_fund_startup=df['startup'].nunique()



    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Total", str(total) + ' Cr.')
    with col2:
        st.metric("Maximum Invest", str(max_) + ' Cr.')
    with col3:
        st.metric("Average Invest", str(avg_) + ' Cr.')
    with col4:
        st.metric("Total Funded Startup", str(total_fund_startup))

    st.header("MoM Graph")
    select_option=st.selectbox('Select Type',['Total','Count'])
    if select_option=='Total':
        temp_df=df.groupby(['year','month'])['amount'].sum().reset_index()
        temp_df['x_axis'] = temp_df['month'].astype('str') + "-" + temp_df['year'].astype('str')

    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
        temp_df['x_axis']=temp_df['month'].astype('str')+"-"+temp_df['year'].astype('str')
    fig3,ax3=plt.subplots()
    ax3.plot(temp_df['x_axis'],temp_df['amount'])
    st.pyplot(fig3)
   # st.dataframe(temp_df)

def load_investors_details(investor):
    st.title(investor)
    # load the recent 5 investment of the investor
    last5_df=df[df['investors'].str.contains(investor)].head()[['date',
            'startup','industry','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)
    # Largest investment by this investor for this company
    col1,col2=st.columns(2)
    with col1:
        big_series=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)
        st.subheader('Big Investment')
        #st.dataframe(big_series)
        fig,ax=plt.subplots()
        plt.figure(figsize=(5,5))
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)
    with col2:
        # inest by sector

        sec_inv=df[df['investors'].str.contains(investor)].groupby('industry')['amount'].sum().sort_values(ascending=False).head(5)
        st.subheader('Sector Invested In ')
        fig1, ax1 = plt.subplots()
        plt.figure(figsize=(5, 5))
        ax1.pie(sec_inv.values, labels=sec_inv.index, autopct='%1.1f%%',
                shadow=True, startangle=60)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)
    col1,col2=st.columns(2)
    with col1:
        stage_df=df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum().sort_values(
            ascending=False).head(5)
        st.subheader('Stage By Invest')
        fig, ax = plt.subplots()
        ax.pie(stage_df.values, labels=stage_df.index, autopct='%1.1f%%',
                shadow=True, startangle=60)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig)


    with col2:
        city_df=df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum().sort_values(
            ascending=False).head(5)
        st.subheader('City Wise Invest')
        fig1, ax1 = plt.subplots()
        ax1.pie(city_df.values, labels=city_df.index, autopct='%1.1f%%',
                shadow=True, startangle=60)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)

    year_df=df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum().sort_values(ascending=False)
    st.subheader('Year Wise Investment by Invertor')


    st.line_chart(year_df)





st.sidebar.title('Startup Funding Analysis')

option=st.sidebar.selectbox('Select One ',["Overall Analysis",'Startup','Investor'])

if option=="Overall Analysis":
    load_overall_analysis()

elif option=='Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup Details')
    st.title('Startup')

else :
    select_investor=st.sidebar.selectbox('Select Investor', set(df['investors'].str.split(',').sum()))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investors_details(select_investor)

