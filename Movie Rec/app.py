import streamlit as st
import pickle
import pandas as pd

movies_dict=pickle.load(open('movies_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie  Recommender System')
selected_movie_name =st.selectbox('What You Like to Watch',movies['title'].values)

def reccomend(movie):
    movie_indices = movies[movies['title'].str.lower() == movie.lower()].index
    if movie_indices.empty:
        return f"'{movie}' not found in the dataset."
    movie_index = movie_indices[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended=[]
    for i in movie_list:
        recommended.append(movies.iloc[i[0]].title)

    return recommended


if st.button('Reccomend'):
    recommendations=reccomend (selected_movie_name)
    for i in recommendations:
        st.write(i)


