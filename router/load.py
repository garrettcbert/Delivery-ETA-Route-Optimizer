import pandas as pd


def load_stops(path):
    stops = pd.read_csv(path)

    return stops