from composable import pipeable
import pandas as pd
from datetime import datetime, timedelta
import re

import numpy as np
import pytest

from pandas import DataFrame, Index, MultiIndex, Series, isna, notna
import pandas._testing as tm

@pipeable
def casefold(col):
    """
    Series.str.casefold: Removes all case distinctions in the string.
    
    Examples
    ---------
    >>> s = pd.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
    >>> s
    0                 lower
    1              CAPITALS
    2    this is a sentence
    3              SwApCaSe
    dtype: object

    >>> s >> casefold
    0                 lower
    1              capitals
    2    this is a sentence
    3              swapcase
    dtype: object"""
    return col.str.casefold()

@pipeable
def center(width,col,*,fillchar = " ") :
    """ center(width, fillchar=' ') method of pandas.core.strings.accessor.StringMethods instance
    Pad left and right side of strings in the Series/Index.
    
    Equivalent to :meth:`str.center`.
    
    Parameters
    ----------
    width : int
        Minimum width of resulting string; additional characters will be filled
        with ``fillchar``.
    fillchar : str
        Additional character for filling, default is whitespace.
    
    Returns
    -------
    filled : Series/Index of objects."""
    return col.str.center(width,fillchar=fillchar)

@pipeable
def contains(pat,col,*,flags = 0,na=None,regex=True):

    """contains(pat, case=True, flags=0, na=None, regex=True) method of pandas.core.strings.accessor.StringMethods instance
    Test if pattern or regex is contained within a string of a Series or Index.
    
    Return boolean Series or Index based on whether a given pattern or regex is
    contained within a string of a Series or Index.
    
    Parameters
    ----------
    pat : str
        Character sequence or regular expression.
    case : bool, default True
        If True, case sensitive.
    flags : int, default 0 (no flags)
        Flags to pass through to the re module, e.g. re.IGNORECASE.
    na : scalar, optional
        Fill value for missing values. The default depends on dtype of the
        array. For object-dtype, ``numpy.nan`` is used. For ``StringDtype``,
        ``pandas.NA`` is used.
    regex : bool, default True
        If True, assumes the pat is a regular expression.
    
        If False, treats the pat as a literal string.
    
    Returns
    -------
    Series or Index of boolean values
        A Series or Index of boolean values indicating whether the
        given pattern is contained within the string of each element
        of the Series or Index.
        >>> s1 = pd.Series(['Mouse', 'dog', 'house and parrot', '23', np.NaN])
    >>> s1 >> contains('og', regex=False)
    0    False
    1     True
    2    False
    3    False
    4      NaN
    dtype: object"""

    return col.str.contains(pat,flags=flags,na=na,regex=regex)

@pipeable
def count(pat,col,*,flags = 0):
    """count(pat, flags=0) method of pandas.core.strings.accessor.StringMethods instance
    Count occurrences of pattern in each string of the Series/Index.
    
    This function is used to count the number of times a particular regex
    pattern is repeated in each of the string elements of the
    :class:`~pandas.Series`.
    
    Parameters
    ----------
    pat : str
        Valid regular expression.
    flags : int, default 0, meaning no flags
        Flags for the `re` module. For a complete list, `see here
        <https://docs.python.org/3/howto/regex.html#compilation-flags>`_.
    **kwargs
        For compatibility with other string methods. Not used.
    
    Returns
    -------
    Series or Index
        Same type as the calling object containing the integer counts.
    
    See Also
    --------
    re : Standard library module for regular expressions.
    str.count : Standard library version, without regular expression support.
    
    Notes
    -----
    Some characters need to be escaped when passing in `pat`.
    eg. ``'$'`` has a special meaning in regex and must be escaped when
    finding this literal character.
    
    Examples
    --------
    >>> s = pd.Series(['A', 'B', 'Aaba', 'Baca', np.nan, 'CABA', 'cat'])
    >>> s >> count('a')
    0    0.0
    1    0.0
    2    2.0
    3    2.0
    4    NaN
    5    0.0
    6    1.0
    dtype: float64"""
    return col.str.count(pat,flags = flags)

@pipeable
def cat(sep,col,*,others=None,na_rep=None, join=None):
    """  Help on method cat in module pandas.core.strings.accessor:

    cat(others=None, sep=None, na_rep=None, join='left') method of pandas.core.strings.accessor.StringMethods instance
    Concatenate strings in the Series/Index with given separator.

    Parameters
    ----------
    others : Series, Index, DataFrame, np.ndarray or list-like
        Series, Index, DataFrame, np.ndarray (one- or two-dimensional) and
        other list-likes of strings must have the same length as the
        calling Series/Index, with the exception of indexed objects (i.e.
        Series/Index/DataFrame) if `join` is not None.
    
        If others is a list-like that contains a combination of Series,
        Index or np.ndarray (1-dim), then all elements will be unpacked and
        must satisfy the above criteria individually.
    
        If others is None, the method returns the concatenation of all
        strings in the calling Series/Index.
    sep : str, default ''
        The separator between the different elements/columns. By default
        the empty string `''` is used.
    na_rep : str or None, default None
        Representation that is inserted for all missing values:
        
    join : {'left', 'right', 'outer', 'inner'}, default 'left'
        Determines the join-style between the calling Series/Index and any
        Series/Index/DataFrame in `others` (objects without an index need
        to match the length of the calling Series/Index). To disable
        alignment, use `.values` on any Series/Index/DataFrame in `others`.
    
    Returns
    -------
    str, Series or Index
        If `others` is None, `str` is returned, otherwise a `Series/Index`
        (same type as caller) of objects is returned.
    
    Examples
    --------
    When not passing `others`, all values are concatenated into a single
    string:
    
    >>> s = pd.Series(['a', 'b', np.nan, 'd'])
    >>> s >> cat(sep=' ')
    'a b d'"""
    return col.str.cat(sep=sep, others=others, na_rep=na_rep, join = join)