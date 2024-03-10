import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='Startup Analysis')

df = pd.read_csv('startup_cleaned.csv')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['month'] = df['Date'].dt.month
df['year'] = df['Date'].dt.year
def load_overall_analysis():
    st.title("Overall Analysis")
    #Total invested amount
    total = round(df['Amount'].sum())
    #Max Amount infused in a startup
    max_funding = df.groupby('Startup')['Amount'].max().sort_values(ascending=False).head().values[0]
    #Avg funding
    avg_funding = df.groupby('Startup')['Amount'].sum().mean()
    # total funded startups
    num_startups = df['Startup'].nunique()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric("Total", str(total) + ' Cr')
    with col2:
        st.metric("Max Funding", str(max_funding) + ' Cr')
    with col3:
        st.metric("Avg Funding", str(round(avg_funding)) + ' Cr')
    with col4:
        st.metric("Funded Startups", num_startups)
    st.header("MoM Graph")
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['Amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['Amount'].count().reset_index()
    temp_df['x_axis'] = temp_df['month'].astype('int').astype('str') + '-' + temp_df['year'].astype('int').astype('str')

    fig4, ax4 = plt.subplots()
    ax4.plot(temp_df['x_axis'], temp_df['Amount'])
    st.pyplot(fig4)
def load_investor_details(Investor):
    st.title(Investor)
    # Load the recent 5 investments
    last5_df = df[df['Investor'].str.contains(Investor)].head()[['Date', 'Startup', 'Vertical', 'city', 'Round','Amount']]
    st.subheader('Most recent investments')
    st.dataframe(last5_df)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        # biggest investments
        big_series = df[df['Investor'].str.contains(Investor)].groupby('Startup')['Amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

    with col2:
        vertical_series = df[df['Investor'].str.contains(Investor)].groupby('Vertical')['Amount'].sum()
        st.subheader('Sectors Invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels = vertical_series.index, autopct="%0.01f%%")
        st.pyplot(fig1)

    with col3:
        city_series = df[df['Investor'].str.contains(Investor)].groupby('city')['Amount'].sum()
        st.subheader('City Invested in')
        fig2, ax2 = plt.subplots()
        ax2.pie(city_series, labels = city_series.index, autopct="%0.01f%%")
        st.pyplot(fig2)

    df['year'] = df['Date'].dt.year
    year_series = df[df['Investor'].str.contains(Investor)].groupby('year')['Amount'].sum()
    st.subheader('YoY Investment')
    fig3, ax3 = plt.subplots()
    ax3.plot(year_series.index, year_series.values)
    st.pyplot(fig3)

st.sidebar.title("Startup Funding Analysis")

option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])
if option == 'Overall Analysis':
        load_overall_analysis()

elif option == 'Startup':
    st.sidebar.selectbox('select startup',sorted(df['Startup'].unique().tolist()))
    btn1 = st.sidebar.button('find startup details')
    st.title("startup Analysis")
else:
    selected_investor = st.sidebar.selectbox('select investor', sorted(set(df['Investor'].str.split(',').sum())))
    btn2 = st.sidebar.button('find investor details')
    if btn2:
        load_investor_details(selected_investor)

    st.title('Investor Analysis')