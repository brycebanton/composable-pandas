from composable import pipeable
import pandas as pd
from datetime import datetime, timedelta
import pandas._testing as tm

@pipeable
def second(col):
    """
    Series.dt can be used to access the values of the series as datetimelike and return several properties. 
    Pandas Series.dt.second attribute return a numpy array containing the second
    of the datetime in the underlying data of the given series object.
    return col.dt.second.

    Example:

    expected = Series([45,21,38,19,44])
    sr = pd.Series(['2012-10-21 09:30:45', '2019-7-18 12:30:21', '2008-02-2 10:30:38', 
            '2010-4-22 09:25:19', '2019-11-8 02:22:44']) 
    sr = to_datetime(sr) 
    results = sr >> second

    returns:

    [45
     21
     38
     19
     41]
        
         """
    return col.dt.second

@pipeable
def day_name(col,*,locale = 'English'):
    """ 
    day_name(*args, **kwargs) method of pandas.core.indexes.accessors.DatetimeProperties instance
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
    Timestamp("2017-08-28 23:00:00")

    data >> day_name

    Returns:

    '0 Monday'

    It is '0 Monday' because it was converted from pandas series to a string. Using pandas.to_string puts a 0 in the string' 

    """

    return col.dt.day_name(locale=locale)

@pipeable
def month_name(col,*,locale = 'English'):
    """ 
    month_name(*args, **kwargs) method of pandas.core.indexes.accessors.DatetimeProperties instance
    Return the month names of the DateTimeIndex with specified locale.

    Parameters
    ----------
    locale : str, optional
    Locale determining the language in which to return the day name.
    Default is English locale.

    Returns
    -------
    Index
    Index of month names.

    Examples
    --------
    Timestamp("2017-08-28 23:00:00")

    data >> month_name

    Returns:

    '0 August'

    It is '0 August' because it was converted from pandas series to a string. Using pandas.to_string puts a 0 in the string' 

    """
    return col.dt.month_name(locale = locale)

@pipeable
def year(col):
    """ 
    Series.dt can be used to access the values of the series as datetimelike and return several properties.
    Pandas Series.dt.year attribute return a numpy array containing year of the datetime in the underlying data
    of the given series object.

    Syntax: Series.dt.year

    Parameter : None

    Returns : numpy array

    Example:

    sr = Series(['2012-12-31 08:45', '2019-1-1 12:30', '2008-02-2 10:30', 
                '2010-1-1 09:25', '2019-12-31 00:00'])

    sr = to_datetime(sr)

    result = sr >> year

    Returns np.array[2012,2019,2008,2010,2019]

    """
    return col.dt.year

@pipeable
def is_month_end(col):
    """
    Series.dt can be used to access the values of the series as datetimelike and return several properties. 
    Pandas Series.dt.is_month_end attribute return a boolean value Indicating whether the date is the last day
    of the month.

    Syntax: Series.dt.is_month_end

    Parameter : None

    Returns : numpy array

    Example:

    sr = Series(['2012-1-31', '2019-7-18 12:30', '2008-02-2 10:30', 
               '2010-4-22 09:25', '2019-1-1 00:00'])

    sr = to_datetime(sr) 

    result = sr >> is_month_end

    Returns:

    [True, False, False, False, False]
    
    """
    return col.dt.is_month_end