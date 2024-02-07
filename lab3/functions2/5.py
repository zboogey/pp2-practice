def average_imdb_score_by_category(category_name, movies):
    category_movies = [movie for movie in movies if movie["category"] == category_name]
    total_score = sum(movie["imdb"] for movie in category_movies)
    return total_score / len(category_movies) if category_movies else 0