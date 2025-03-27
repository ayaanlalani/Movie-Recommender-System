# 🎬 Movie Recommendation System

This is a **content-based** movie recommendation system that suggests movies based on their similarity in genres, keywords, cast, and overview. It uses **Natural Language Processing (NLP)** techniques and **Cosine Similarity** to find similar movies.

## 📂 Project Structure
```
├── movies_recommendation_system
│   ├── tmdb_5000_movies.csv
│   ├── tmdb_5000_credits.csv
│   ├── similarity_matrix.pkl
│   ├── movies_dict.pkl
│   ├── movie_recommender.py
│   ├── README.md
```

## 🔧 Technologies Used
- **Python**
- **Pandas** (Data Processing)
- **Scikit-learn** (Vectorization & Cosine Similarity)
- **NLTK** (Text Processing)
- **Pickle** (Saving Model Data)

## 🚀 How It Works
1. The dataset (`tmdb_5000_movies.csv` & `tmdb_5000_credits.csv`) is **preprocessed**:
   - Extracts relevant fields (title, genres, keywords, cast, crew, and overview).
   - Converts lists into formatted text data.
   - Removes spaces and applies stemming.

2. **Text vectorization** is applied using `CountVectorizer` (Bag of Words model).

3. **Cosine Similarity** is computed to measure the similarity between movies.

4. The `recommendations(movie_title)` function returns the **top 5 similar movies**.

## 🛠 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ayaanlalani/Movie-Recommender-System.git
cd Movie-Recommender-System
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Recommender
```python
from movie_recommender import recommendations

recommendations("Inception")  # Example usage
```

### 4️⃣ Output Example
```
Shutter Island
The Prestige
Interstellar
The Dark Knight
Memento
```

## 🏆 Features
✅ Content-based filtering  
✅ Uses **cosine similarity** for recommendations  
✅ **Fast & Efficient** movie retrieval  
✅ **Pre-trained model** stored in `similarity_matrix.pkl`

## 📌 Notes
- `similarity_matrix.pkl` is **over 100MB**, so it's stored using **Git LFS**.
- `movies_dict.pkl` contains a dictionary mapping movie IDs to titles.

## 📝 License
This project is **open-source** and free to use. Contributions are welcome! 🎥
