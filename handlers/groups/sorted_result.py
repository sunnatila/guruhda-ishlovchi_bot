def result_sort(result: list) -> list:
    response = []
    if result:
        scores = set(map(lambda user: user['score'], result))
        sorted_scores = sorted(list(scores), reverse=True)
        for score in sorted_scores:
            response.extend(list(filter(lambda user: user['score'] == score, result)))
    return response



