from composable import pipeable
import pandas as pd
from datetime import datetime, timedelta
import pandas._testing as tm

@pipeable
def second(col):
    return col.dt.second

@pipeable
def day_name(col,*,locale = 'English'):
    """ day_name(*args, **kwargs) method of pandas.core.indexes.accessors.DatetimeProperties instance
    Return the day names of the DateTimeIndex with specified locale.
    
    Parameters
    ----------
    locale : str, optional
        Locale determining the language in which to return the day name.
        Default is English locale.
    
    Returns
    -------
    Index
        Index of day names.
    
    Examples
    --------
    >>> idx = pd.date_range(start='2018-01-01', freq='D', periods=3)
    >>> idx
    DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03'],
                  dtype='datetime64[ns]', freq='D')
    >>> idx.day_name()
    Index(['Monday', 'Tuesday', 'Wednesday'], dtype='object')"""

    return col.dt.day_name(locale=locale)

@pipeable
def month_name(col,*,locale = 'English'):
    return col.dt.month_name(locale = locale)

@pipeable
def year(col):
    return col.dt.year

@pipeable
def is_month_end(col):
    return col.dt.is_month_end