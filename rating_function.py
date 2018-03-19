def convert_to_numeric(score):
    """
    If input is a string, convert it to a number
    """
    return float(score)


def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Calculate the sum of the middle 3 scores
    """
    all_scores = [score1,score2,score3,score4,score5]
    return (sum(all_scores) - min(all_scores) - max(all_scores))


def score_to_rating_string(avg_score):
    """
    Map the score number to a written rating
    """
    if 0 <= avg_score and avg_score < 1:
        return("Terrible")
    elif 1 <= avg_score and avg_score < 2:
        return("Bad")
    elif 2 <= avg_score and avg_score < 3:
        return("OK")
    elif 3 <= avg_score and avg_score < 4:
        return("Good")
    elif 4 <= avg_score and avg_score <= 5:
        return("Excellent")


def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

print(scores_to_rating(1,1,"1","1",1))
print(scores_to_rating(2,2,2,2,2))
print(scores_to_rating("3",3,3,"3",3))
print(scores_to_rating("4",4,"4",4,4))
print(scores_to_rating(5,"5",5,"5",5))
