def movies_by_category(category_name, movies):
    return [movie for movie in movies if movie["category"] == category_name]