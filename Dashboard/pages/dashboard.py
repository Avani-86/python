
import streamlit as st
import seaborn as sns
import plotly.express as px

st.title("Explore the Insight of Titanic Data")

df = sns.load_dataset("titanic")
st.dataframe(df)

#gender filter
gender = st.sidebar.multiselect("Gender",
                             options=df['sex'].unique(),
                             default = df['sex'].unique())

#class filter
class_filter = st.sidebar.multiselect("Class",
                                      options=df['class'].unique(),
                                          default = df['class'].unique())

# age filter
min_age, max_age = st.sidebar.slider("Age",
                               min_value=int(df['age'].min()),
                               max_value=int(df['age'].max()),
                               value=(int(df['age'].min()),int(df['age'].max())))

filtered_df = df[
    (df['sex'].isin(gender)) &
    (df['class'].isin(class_filter)) &
    (df['age']>=min_age)  &
    (df['age']<=max_age)
                 ]

#total survived by classs
fig = px.bar(filtered_df, x='class' , y='survived',
            title = 'Total Survived by Class',
            labels = {'class':'Class','survived':'Total Survived'},
            color= 'survived', template='plotly_dark'
)
st.plotly_chart(fig)            

# Age distribution
fig = px.histogram(filtered_df, x='age',
                   title='Age Distribution',
                   color_discrete_sequence=['#F39c12'],
                   template='plotly_dark'
                   )
st.plotly_chart(fig)

#pie chart for claas distribution
fig = px.pie(filtered_df,names='class',
             title='Class distribution',
             color_discrete_sequence=px.colors.sequential.RdBu,
             template='plotly_dark'
             )
st.plotly_chart(fig)


