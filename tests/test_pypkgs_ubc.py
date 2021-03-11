from pypkgs_ubc import pypkgs_ubc
import pandas as pd


def test_catbind():
    a = pd.Categorical(["character", "hits", "your", "eyeballs"])
    b = pd.Categorical(["but", "integer", "where it", "counts"])
    assert ((pypkgs_ubc.catbind(a, b)).codes == [1, 4, 7, 3, 0, 5, 6, 2]).all()
    assert (
        (pypkgs_ubc.catbind(a, b)).categories
        == [
            "but",
            "character",
            "counts",
            "eyeballs",
            "hits",
            "integer",
            "where it",
            "your",
        ]
    ).all()
