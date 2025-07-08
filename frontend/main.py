import streamlit as st
import pickle
import pandas as pd
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    distances = list(enumerate(distances))
    movies_list = sorted(distances,reverse=True,key=lambda x : x[1])[1:6]

    recommended_movies = []
    # recommended_movie_ids = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        # recommended_movie_ids.append(movies.iloc[i[0]].movie_id)
    return recommended_movies

st.title("Movie Recomandation System")
selected_movie_name = st.selectbox("Select a Movie :",movies['title'].to_numpy())

if st.button('Recommend'):
    st.subheader(selected_movie_name)
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
    # for i in movi_ids:
    #     st.write(i)
    