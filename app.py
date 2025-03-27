import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "" #add ypur api key
    }

    response = requests.get(url, headers=headers)  # Include headers for authentication
    if response.status_code != 200:
        return "Error: Unable to fetch movie data"

    data = response.json()

    # Ensure 'poster_path' exists before returning the URL
    if 'poster_path' in data and data['poster_path']:
        return f"http://image.tmdb.org/t/p/w500/{data['poster_path']}"
    else:
        return "No poster available"


def recommend(movie):
    movie_index = movies_list_df[movies_list_df.title == movie].index[0]
    cosine_distances = similarity_matrix[movie_index]
    recommended_list = sorted(list(enumerate(cosine_distances)), reverse=True, key=lambda x: x[1])[1:6]
    output = []
    movie_posters = []
    for i in recommended_list:
        movie_id = movies_list_df.iloc[i[0]]['movie_id']
        output.append(movies_list_df.iloc[i[0]]['title'])
        movie_posters.append(fetch_poster(movie_id))
    return output, movie_posters


similarity_matrix = pickle.load(open('../similarity_matrix.pkl', 'rb'))
movies_list_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies_list_df = pd.DataFrame(movies_list_dict)

st.title("Movie Recommender System")

option_selected = st.selectbox(
    'PLease select a movie',
    movies_list_df['title'].values)

if st.button('Recommend Movies'):
    names, posters = recommend(option_selected)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
