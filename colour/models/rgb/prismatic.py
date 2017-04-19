#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Prismatic Colourspace
=====================

Defines the *Prismatic* colourspace transformations:

-   :func:`RGB_to_Prismatic`
-   :func:`Prismatic_to_RGB`

See Also
--------
`Prismatic Colourspace Jupyter Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/models/prismatic.ipynb>`_

References
----------
.. [1]  Shirley, P., & Hart, D. (2015). The prismatic color space for rgb
        computations, 2–7.
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.utilities import tsplit, tstack

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2017 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['RGB_to_Prismatic',
           'Prismatic_to_RGB']


def RGB_to_Prismatic(RGB):
    """
    Converts from *RGB* colourspace to *Prismatic* :math:`L\\rho\gamma\\beta`
    colourspace array.

    Parameters
    ----------
    RGB : array_like
        *RGB* colourspace array.

    Returns
    -------
    ndarray
        *Prismatic* :math:`L\\rho\gamma\\beta` colourspace array.

    Examples
    --------
    >>> RGB = np.array([0.25, 0.50, 0.75])
    >>> RGB_to_Prismatic(RGB)  # doctest: +ELLIPSIS
    array([ 0.75...   ,  0.1666666...,  0.3333333...,  0.5...   ])

    Adjusting saturation of given *RGB* colourspace array:
    >>> saturation = 0.5
    >>> Lrgb = RGB_to_Prismatic(RGB)
    >>> Lrgb[..., 1:] = 1 / 3 + saturation * (Lrgb[..., 1:] - 1 / 3)
    >>> Prismatic_to_RGB(Lrgb)  # doctest: +ELLIPSIS
    array([ 0.45...,  0.6...,  0.75...])
    """

    RGB = np.asarray(RGB)

    L = np.max(RGB, axis=-1)
    s = 1 / np.sum(RGB, axis=-1)[..., np.newaxis]
    # Handling *NaNs* and *infs*.
    s = np.nan_to_num(s)
    r, g, b = tsplit(s * RGB)

    return tstack((L, r, g, b))


def Prismatic_to_RGB(Lrgb):
    """
    Converts from *Prismatic* :math:`L\\rho\gamma\\beta` colourspace array to
    *RGB* colourspace.

    Parameters
    ----------
    Lrgb : array_like
        *Prismatic* :math:`L\\rho\gamma\\beta` colourspace array.

    Returns
    -------
    ndarray
        *RGB* colourspace array.

    Examples
    --------
    >>> Lrgb = np.array([0.75000000, 0.16666667, 0.33333333, 0.50000000])
    >>> Prismatic_to_RGB(Lrgb)  # doctest: +ELLIPSIS
    array([ 0.25...   ,  0.4999999...,  0.75...  ])
    """

    Lrgb = np.asarray(Lrgb)

    rgb = Lrgb[..., 1:]
    RGB = (Lrgb[..., 0][..., np.newaxis] /
           np.max(rgb, axis=-1)[..., np.newaxis] * rgb)
    # Handling *NaNs* and *infs*.
    RGB = np.nan_to_num(RGB)

    return RGB
