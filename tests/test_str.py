from composable_pandas.str import casefold
from composable_pandas.str import center
from composable_pandas.str import contains
from composable_pandas.str import count
from composable_pandas.str import cat

from composable import pipeable
from datetime import datetime
import numpy as np
import pytest
import re

from pandas import Series, _testing as tm

def test_casefold():
    expected = Series(["ss", np.nan, "case", "ssd"])
    s = Series(["ß", np.nan, "case", "ßd"])
    result = s >> casefold()
    tm.assert_series_equal(result, expected)

def test_center():
    values = Series(["a", "b", np.nan, "c", np.nan, "eeeeee"])
    exp = Series(["  a  ", "  b  ", np.nan, "  c  ", np.nan, "eeeeee"])
    result = values >> center(5)
    tm.assert_almost_equal(result, exp)

def test_contains():
    values = np.array(
        ["foo", np.nan, "fooommm__foo", "mmm_", "foommm[_]+bar"], dtype=np.object_
    )
    values = Series(values)
    pat = "mmm[_]+"

    result = values >> contains(pat)
    expected = Series(np.array([False, np.nan, True, True, False], dtype=np.object_))
    tm.assert_series_equal(result, expected)

def test_count():
    pat = "a"
    values = Series(["a", "b", 'aa', "c","dddd", "eeeeee"])
    exp = Series([1,0,2,0,0,0])
    result = values >> count(pat)
    tm.assert_almost_equal(result, exp)

def test_cat():
    s = Series(["a", "a", "b", "b", "c"])
    result = s >> cat("_")
    expected = "a_a_b_b_c"
    tm.assert_almost_equal(result, expected)