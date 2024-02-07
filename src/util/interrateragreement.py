def calc_percentage_agreement(rating1: list, rating2: list) -> float:
    """Calculate the percentage agreement between two ordered lists of ratings.

    parameters:
        rating1 - list of values of one rater
        rating2 - list of values of another rater

    returns
        percentage agreement - the fraction of perfect matches in the two ratings between 0 and 1
        ValueError - raised if the two lists are not of equal length
    """

    if len(rating1) != len(rating2):
        raise ValueError(f'The two ratings to compare are of inequal length ({len(rating1)} vs. {len(rating1)}).')
    
    n: int = len(rating1)
    agreement: float = 0
    for (r1, r2) in zip(rating1, rating2):
        if r1 == r2:
            agreement += 1

    return agreement/n

def calc_bennetts_s_score(rating1: list, rating2: list, labels: list) -> float:
    """Calculate the Bennett's S score, which represents the agreement between two rater over two ratings given a set of possible labels.
    
    parameters:
        rating1 - list of values of one rater
        rating2 - list of values of another rater
        labels - list of potential values

    returns
        s score - Bennett's S score of agreement between 0 and 1
        ValueError - raised if the two lists are not of equal length
    """
    k = len(labels)
    p = calc_percentage_agreement(rating1, rating2)
    return (k/(k-1)) * (p-(1/k))  
