import pandas as pd

def get_unique_codes(df: pd.DataFrame, column: str) -> [str]:
    """Returns a list of unique codes contained in a given column.

    parameters:
        df -- pandas.DataFrame containing the data
        column -- name of the column containing cells with codes or groups of codes separated by semicolons (e.g., "code1;code2)

    returns:
        list of unique codes
    """

    # obtain all codes of the column (which still contains code groups like "code1;code2")
    all_codes = list(df[column].value_counts().index)

    # split up code groups (the sum([...], []) flattens the list of lists)
    singular_codes = sum([code.split(';') for code in all_codes], [])

    # remove duplicates
    return list(set(singular_codes))