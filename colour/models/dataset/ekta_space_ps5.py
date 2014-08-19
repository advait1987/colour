#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ekta Space PS 5 Colourspace
===========================

Defines the *Ekta Space PS 5* colourspace:

-   :attr:`EKTA_SPACE_PS_5_COLOURSPACE`.

References
----------
.. [1]  http://www.josephholmes.com/Ekta_Space.zip
        (Last accessed 13 April 2014)
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.colorimetry import ILLUMINANTS
from colour.models import RGB_Colourspace, get_normalised_primary_matrix

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2014 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['EKTA_SPACE_PS_5_PRIMARIES',
           'EKTA_SPACE_PS_5_WHITEPOINT',
           'EKTA_SPACE_PS_5_TO_XYZ_MATRIX',
           'XYZ_TO_EKTA_SPACE_PS_5_MATRIX',
           'EKTA_SPACE_PS_5_TRANSFER_FUNCTION',
           'EKTA_SPACE_PS_5_INVERSE_TRANSFER_FUNCTION',
           'EKTA_SPACE_PS_5_COLOURSPACE']

EKTA_SPACE_PS_5_PRIMARIES = np.array(
    [[0.6947368421052631, 0.30526315789473685],
     [0.26000000000000001, 0.69999999999999996],
     [0.10972850678733032, 0.0045248868778280547]])
"""
*Ekta Space PS 5* colourspace primaries.

EKTA_SPACE_PS_5_PRIMARIES : ndarray, (3, 2)
"""

EKTA_SPACE_PS_5_WHITEPOINT = ILLUMINANTS.get(
    'CIE 1931 2 Degree Standard Observer').get('D50')
"""
*Ekta Space PS 5* colourspace whitepoint.

EKTA_SPACE_PS_5_WHITEPOINT : tuple
"""

EKTA_SPACE_PS_5_TO_XYZ_MATRIX = get_normalised_primary_matrix(
    EKTA_SPACE_PS_5_PRIMARIES, EKTA_SPACE_PS_5_WHITEPOINT)
"""
*Ekta Space PS 5* colourspace to *CIE XYZ* colourspace matrix.

EKTA_SPACE_PS_5_TO_XYZ_MATRIX : array_like, (3, 3)
"""

XYZ_TO_EKTA_SPACE_PS_5_MATRIX = np.linalg.inv(EKTA_SPACE_PS_5_TO_XYZ_MATRIX)
"""
*CIE XYZ* colourspace to *Ekta Space PS 5* colourspace matrix.

XYZ_TO_EKTA_SPACE_PS_5_MATRIX : array_like, (3, 3)
"""

EKTA_SPACE_PS_5_TRANSFER_FUNCTION = lambda x: x ** (1 / 2.2)
"""
Transfer function from linear to *Ekta Space PS 5* colourspace.

EKTA_SPACE_PS_5_TRANSFER_FUNCTION : object
"""

EKTA_SPACE_PS_5_INVERSE_TRANSFER_FUNCTION = lambda x: x ** 2.2
"""
Inverse transfer function from *Ekta Space PS 5* colourspace to linear.

EKTA_SPACE_PS_5_INVERSE_TRANSFER_FUNCTION : object
"""

EKTA_SPACE_PS_5_COLOURSPACE = RGB_Colourspace(
    'Ekta Space PS 5',
    EKTA_SPACE_PS_5_PRIMARIES,
    EKTA_SPACE_PS_5_WHITEPOINT,
    EKTA_SPACE_PS_5_TO_XYZ_MATRIX,
    XYZ_TO_EKTA_SPACE_PS_5_MATRIX,
    EKTA_SPACE_PS_5_TRANSFER_FUNCTION,
    EKTA_SPACE_PS_5_INVERSE_TRANSFER_FUNCTION)
"""
*Ekta Space PS 5* colourspace.

EKTA_SPACE_PS_5_COLOURSPACE : RGB_Colourspace
"""