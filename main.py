# my imported libraries
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")

# Page Setup 
page_setup = st.set_page_config(page_title="Superstore!!!", page_icon=":bar_chart:", layout="wide")

page_title = st.title(" :bar_chart: Sample Superstore EDA")

page_styling = st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

upload_file = st.file_uploader(":file_folder: Upload a file", type=(["csv", "xls", "txt", "xlsx"]))

if upload_file is not None:
    filename = upload_file.name
    st.write(filename)
    df = pd.read_csv(filename, encoding= "ISO-8859-1")
else:
    os.chdir(r"/Users/nanakwasiofosu-duodu/Documents/Streamlit")
    df = pd.read_csv("superstore.csv", encoding= "ISO-8859-1")

#Column Session
first_column, second_column = st.columns((2))

start_date = pd.to_datetime(df["Order Date"]).min()
end_date = pd.to_datetime(df["Order Date"]).max()

with first_column:
    first_col_datetime = pd.to_datetime(st.date_input("Start Date", start_date))

with second_column:
    second_col_datetime = pd.to_datetime(st.date_input("End Date", end_date))


df = df[(pd.to_datetime(df["Order Date"]) >= first_col_datetime) & (pd.to_datetime(df["Order Date"]) <= second_col_datetime)].copy()

# # Sidebar Session
sidebar = st.sidebar.header("Choose your filter: ")


# # Creating a region session
sorting_region = df.sort_values("Region")
select_region = st.sidebar.multiselect("Pick your Region", sorting_region["Region"].unique())
if not select_region:
    sorted_region_copy = sorting_region.copy() # df2
    #sorted_region_copy
else:
    sorted_region_copy = sorting_region[sorting_region["Region"].isin(select_region)] #df2
    #sorted_region_copy

# # Creating a state session
sorting_state = sorted_region_copy.sort_values("State")
# length = st.write(len(sorted_region_copy["State"].unique()))

select_state = st.sidebar.multiselect("Pick your State", sorted_region_copy["State"].unique())
if not select_state:
    sorted_state_copy = sorting_state.copy() # df3
    #sorted_state_copy
else:
    sorted_state_copy = sorting_state[sorting_state["State"].isin(select_state)] #df3
    #sorted_state_copy
state = []
for i in sorted_state_copy["State"].unique():
    state.append(i)
st.write(state)
# # # Creating a city session
sorting_city = sorted_state_copy.sort_values("City")
select_city = st.sidebar.multiselect("Pick your State", sorting_city["City"].unique()) #df3

if not select_city:
    sorted_city_copy = sorting_city.copy()
    #sorted_city_copy
else:
    sorted_city_copy = sorting_city[sorting_city["City"].isin(select_city)]
    #sorted_city_copy


if not select_region and not select_state and not select_city:
    filtered_df = sorting_region
    st.write(len(filtered_df))
    
elif not select_state and not select_city:
    filtered_df = sorted_region_copy
    st.write(len(filtered_df))
    # sorting_region[sorting_region["Region"].isin(select_region)]
    # filtered_df
elif not select_region and not select_city:
    filtered_df = sorting_region[sorting_region["State"].isin(select_state)]
    st.write(len(filtered_df))
    # filtered_df
    # sorting_state[sorting_state["State"].isin(select_state)]
elif not select_region and not select_state:
    filtered_df = sorting_region[sorting_region["City"].isin(select_city)]
    # filtered_df
    st.write(len(filtered_df))

elif select_state and select_city:
    filtered_df = sorted_state_copy[sorted_region_copy["State"].isin(select_state) & sorting_city["City"].isin(select_city)]
    # filtered_df
    st.write(len(filtered_df))

elif select_region and select_city:
    filtered_df = sorted_state_copy[sorted_region_copy["Region"].isin(select_region) & sorting_city["City"].isin(select_city)]
    # filtered_df
    st.write(len(filtered_df))

elif select_region and select_state:
    filtered_df = sorted_state_copy[sorted_region_copy["Region"].isin(select_region) & sorting_city["State"].isin(select_state)]
    # filtered_df
    st.write(len(filtered_df))

elif select_city:
    filtered_df = sorted_state_copy[sorting_city["City"].isin(select_city)]
    # filtered_df
    st.write(len(filtered_df))

else:
    filtered_df = sorted_state_copy[sorted_state_copy["Region"].isin(select_region) & sorted_state_copy["State"].isin(select_state) & sorted_state_copy["City"].isin(select_city)]
    # filtered_df
    st.write(len(filtered_df))