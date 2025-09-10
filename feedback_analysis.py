
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
def positive_feedback(ratings):
    if not ratings:
        return 0  
    positive_count = 0
    for rating in ratings:
        if rating >= 4:
            positive_count += 1
    percentage = (positive_count / len(ratings)) * 100
    return percentage
positive_percent = positive_feedback(ratings)
print("Positive Feedback:", positive_percent, "%")
