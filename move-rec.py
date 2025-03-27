import numpy as np
import pandas as pd
import ast
import nltk
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

movies = movies.merge(credits, on='title')
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

movies.dropna(inplace=True)


def reformat(list):
    new_list = []
    list = ast.literal_eval(list)
    for i in list:
        new_list.append(i['name'])
    return new_list


movies['genres'] = movies['genres'].apply(reformat)
movies['keywords'] = movies['keywords'].apply(reformat)


def reformat_cast(list):
    new_list = []
    counter = 0
    list = ast.literal_eval(list)
    for i in list:
        if counter != 3:
            new_list.append(i['name'])
            counter += 1
        else:
            break
    return new_list


def extract_director(list):
    new_list = []
    list = ast.literal_eval(list)
    for i in list:
        if i['job'] == 'director':
            new_list.append(i['name'])
            break
    return new_list


movies.crew = movies.crew.apply(extract_director)

movies.overview = movies.overview.apply(lambda x: x.split())

movies.genres = movies.genres.apply(lambda x: [i.replace(" ", "") for i in x])
movies.keywords = movies.keywords.apply(lambda x: [i.replace(" ", "") for i in x])
movies.cast = movies.cast.apply(lambda x: [i.replace(" ", "") for i in x])
movies.crew = movies.crew.apply(lambda x: [i.replace(" ", "") for i in x])

movies['tags'] = movies.overview + movies.genres + movies.keywords + movies.cast + movies.crew
movies = movies[['movie_id', 'title', 'tags']]
movies.tags = movies.tags.apply(lambda x: " ".join(x))
movies.tags = movies.tags.apply(lambda x: x.lower())

ps = PorterStemmer()


def stem(text):
    list = []
    for i in text.split():
        ps.stem(i)
        list.append(i)
    return " ".join(list)


movies.tags = movies.tags.apply(stem)

cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(movies['tags']).toarray()

similarity_matrix = cosine_similarity(vectors)


def recommendations(movie):
    movie_index = movies[movies.title == movie].index[0]
    cosine_distances = similarity_matrix[movie_index]
    recommended_list = sorted(list(enumerate(cosine_distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in recommended_list:
        print(movies.iloc[i[0]].title)


pickle.dump(movies.to_dict(), open('movies_dict.pkl', 'wb'))
pickle.dump(similarity_matrix, open('../similarity_matrix.pkl', 'wb'))
