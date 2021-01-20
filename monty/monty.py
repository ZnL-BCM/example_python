# Example functions


def printmenu():
    """Example function for printing a pandas dataframe"""
    import pandas as pd
    _menu = pd.DataFrame([["Egg"], ["Bacon"], ["SPAM"]], index=[1, 2, 3])
    print(_menu)
