import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as   plt
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Customer Care !!!",page_icon=" :bar_chart:",layout="wide")
st.title(" :bar_chart: Customer Care EDA ")
st.markdown('<stylE>div.block-container{padding-top:1rem;}<style',unsafe_allow_html=True)

##f1=st.file_uploader(":file_folder: upload file",type=("csv"))
#if f1 is not None:
    #filename=f1.name
    #st.write(filename)
    #df=pd.read_csv(filename,encoding="ISO-8859-1")
#else:
    #os.chdir(r"H:\dashboard\Sample - Superstore.csv") 
    #df=pd.read_csv(r"Sample - Superstore",encoding="ISO-8859-1")   


#Getting the min and max date 




#st.sidebar.header("choose the name :")
#st.sidebar.header("choose your filter :")
df=pd.read_csv("H:\dashboard\cmd_c.csv")  
df["Doc Uploaded At"]=pd.to_datetime(df["Doc Uploaded At"])

startdate=pd.to_datetime(df["Doc Uploaded At"]).min()
enddate=pd.to_datetime(df["Doc Uploaded At"]).max()
col1,col2 =st.columns(2)
with col1:
    dat1=pd.to_datetime(st.date_input("Start Date",startdate))


with col2:
    dat2=pd.to_datetime(st.date_input("End Date",enddate))


df=df[(df["Doc Uploaded At"]>=dat1)&(df["Doc Uploaded At"]<=dat2)]

name=st.selectbox("select the name.... ",df["Uploaded By"].unique())

if not name:
    filterd_df = df
else:
    filterd_df = df[df["Uploaded By"].isin([name])]

    





ff=filterd_df.groupby("Doc Type")["Uploaded By"].count().reset_index().sort_values(by="Doc Type",ascending=False)



fig=px.bar(ff,x="Doc Type",y="Uploaded By",text_auto=True)
fig.update_layout(title="The Doc type by name")
fig.update_layout(title_x=.5)
fig.update_layout(xaxis_title="Doc Type")
fig.update_layout(yaxis_title="Value")
fig.update_traces(textposition='outside')
st.plotly_chart(fig)






#plot the count of DOC type by Location
fig2=px.pie(df.groupby(["Location"])["Uploaded By"].count().reset_index(),names="Location" ,values="Uploaded By" )
fig2.update_layout(title="Distribution of DOC BY Location")
fig2.update_layout(title_x=.5)
st.plotly_chart(fig2)



df["month"]=df["Doc Uploaded At"].dt.month_name()

h=df.groupby(["month","Location"])["Uploaded By"].count().reset_index().sort_values("Location",ascending=True)



fig3=px.bar(data_frame=h,x="month",y="Uploaded By",color='Location',barmode='group',text_auto=True)
fig3.update_layout(title="Distribution of doc by months every location")
fig3.update_layout(title_x=.5)
fig3.update_layout(xaxis_title="month")
fig3.update_layout(yaxis_title="Uploaded By")
fig3.update_traces(textposition='outside')
st.plotly_chart(fig3)





fig4=px.bar(data_frame=h,x="Location",y="Uploaded By",color='month',barmode='group',text_auto=True)
fig4.update_layout(title="Distribution of doc by Location every month")
fig4.update_layout(title_x=.5)
fig4.update_layout(xaxis_title="month")
fig4.update_layout(yaxis_title="Uploaded By")
fig4.update_traces(textposition='outside')
st.plotly_chart(fig4)


#dd=df["Uploaded By"].value_counts().reset_index()


