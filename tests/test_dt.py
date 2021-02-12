from composable_pandas.dt import day_name, month_name,second,year, is_month_end
import locale
import unicodedata
from composable import pipeable
from datetime import datetime, timedelta
import numpy as np
import pytest
import re
import calendar
import unicodedata
from dateutil.tz import tzutc
import pytz
from pytz import timezone, utc
import pandas as pd
from pandas import Series,date_range,to_datetime,Timestamp, _testing as tm
from pandas.tests.tseries.offsets.common import assert_offset_equal
from pandas.tseries import offsets
from pandas.tseries.offsets import Hour, Micro, Milli, Minute, Nano, Second
from pandas._libs.tslibs.timezones import dateutil_gettz as gettz, get_timezone
import pandas.util._test_decorators as td
from pandas import NaT, Timedelta, Timestamp
import pandas._testing as tm
from pandas.tseries import offsets

def test_second():
    expected = Series([45,21,38,19,44])
    sr = pd.Series(['2012-10-21 09:30:45', '2019-7-18 12:30:21', '2008-02-2 10:30:38', 
               '2010-4-22 09:25:19', '2019-11-8 02:22:44']) 
    sr = to_datetime(sr) 
    results = sr >> second
    tm.assert_series_equal(results, expected)


@pytest.mark.parametrize(
    "data",
    [Timestamp("2017-08-28 23:00:00"),Timestamp("2017-08-28 23:00:00", tz="EST")],
)
@pytest.mark.parametrize(
    "time_locale", [None] if tm.get_locales() is None else [None] + tm.get_locales()
)
def test_names(data, time_locale):
    # GH 17354
    # Test .day_name(), .month_name
    data = pd.Series(data)
    if time_locale is None:
        expected_day = "Monday"
        expected_day = pd.Series(expected_day)
        expected_day = expected_day.to_string()
        expected_month = "August"
        expected_month = pd.Series(expected_month)
        expected_month = expected_month.to_string()
    else:
        with tm.set_locale(time_locale, locale.LC_TIME):
            expected_day = calendar.day_name[0].capitalize()
            expected_day = pd.Series(expected_day)
            expected_day = expected_day.to_string()
            expected_month = calendar.month_name[8].capitalize()
            expected_month = pd.Series(expected_month)
            expected_month = expected_month.to_string()

    result_day = data >> day_name(locale = time_locale)
    result_month = data >> month_name(locale = time_locale)

    # Work around https://github.com/pandas-dev/pandas/issues/22342
    # different normalizations
    # These work just fine
    expected_day = unicodedata.normalize("NFD", expected_day)
    expected_month = unicodedata.normalize("NFD", expected_month)

    # The unicodes to be strings so convert Series to strings. Problem is that there is a 0 when using to_string()
    # This was fixed by doing the switching in the above if,else,with statement
    result_day = result_day.to_string()
    result_month = result_month.to_string()
    result_day = unicodedata.normalize("NFD", result_day)
    result_month = unicodedata.normalize("NFD", result_month)

    assert result_day == expected_day
    assert result_month == expected_month

    #Test NaT
    nan_ts = Timestamp(NaT)
    nan_ts = pd.Series(nan_ts)
    assert np.array(np.isnan(nan_ts >> day_name(locale = time_locale)))
    assert np.array(np.isnan(nan_ts >> month_name(locale = time_locale)))


def test_year():
    expected = Series([2012,2019,2008,2010,2019])
    sr = Series(['2012-12-31 08:45', '2019-1-1 12:30', '2008-02-2 10:30', 
               '2010-1-1 09:25', '2019-12-31 00:00'])
    sr = to_datetime(sr) 
    result = sr >> year
    tm.assert_series_equal(result, expected) 

def test_is_month_end():
    expected = Series([True, False, False, False, False])
    sr = Series(['2012-1-31', '2019-7-18 12:30', '2008-02-2 10:30', 
               '2010-4-22 09:25', '2019-1-1 00:00'])
    sr = to_datetime(sr) 
    result = sr >> is_month_end
    tm.assert_series_equal(result, expected) 