# -*- coding: utf-8 -*-
"""
ALEXA Wide Gamut Colourspace
============================

Defines the *ALEXA Wide Gamut* colourspace:

-   :attr:`colour.models.ALEXA_WIDE_GAMUT_COLOURSPACE`.

See Also
--------
`RGB Colourspaces Jupyter Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/models/rgb.ipynb>`_

References
----------
-   :cite:`ARRI2012a` : ARRI. (2012). ALEXA - Log C Curve - Usage in VFX.
    Retrieved from http://www.arri.com/?eID=registration&file_uid=8026
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.colorimetry import ILLUMINANTS
from colour.models.rgb import (RGB_Colourspace, log_encoding_ALEXALogC,
                               log_decoding_ALEXALogC)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'ALEXA_WIDE_GAMUT_PRIMARIES', 'ALEXA_WIDE_GAMUT_ILLUMINANT',
    'ALEXA_WIDE_GAMUT_WHITEPOINT', 'ALEXA_WIDE_GAMUT_TO_XYZ_MATRIX',
    'XYZ_TO_ALEXA_WIDE_GAMUT_MATRIX', 'ALEXA_WIDE_GAMUT_COLOURSPACE'
]

ALEXA_WIDE_GAMUT_PRIMARIES = np.array([
    [0.6840, 0.3130],
    [0.2210, 0.8480],
    [0.0861, -0.1020],
])
"""
*ALEXA Wide Gamut* colourspace primaries.

ALEXA_WIDE_GAMUT_PRIMARIES : ndarray, (3, 2)
"""

ALEXA_WIDE_GAMUT_ILLUMINANT = 'D65'
"""
*ALEXA Wide Gamut* colourspace whitepoint name as illuminant.

ALEXA_WIDE_GAMUT_WHITEPOINT : unicode
"""

ALEXA_WIDE_GAMUT_WHITEPOINT = (ILLUMINANTS[
    'CIE 1931 2 Degree Standard Observer'][ALEXA_WIDE_GAMUT_ILLUMINANT])
"""
*ALEXA Wide Gamut* colourspace whitepoint.

ALEXA_WIDE_GAMUT_WHITEPOINT : ndarray
"""

ALEXA_WIDE_GAMUT_TO_XYZ_MATRIX = np.array([
    [0.638008, 0.214704, 0.097744],
    [0.291954, 0.823841, -0.115795],
    [0.002798, -0.067034, 1.153294],
])
"""
*ALEXA Wide Gamut* colourspace to *CIE XYZ* tristimulus values matrix.

ALEXA_WIDE_GAMUT_TO_XYZ_MATRIX : array_like, (3, 3)
"""

XYZ_TO_ALEXA_WIDE_GAMUT_MATRIX = np.array([
    [1.789066, -0.482534, -0.200076],
    [-0.639849, 1.396400, 0.194432],
    [-0.041532, 0.082335, 0.878868],
])
"""
*CIE XYZ* tristimulus values to *ALEXA Wide Gamut* colourspace matrix.

XYZ_TO_ALEXA_WIDE_GAMUT_MATRIX : array_like, (3, 3)
"""

ALEXA_WIDE_GAMUT_COLOURSPACE = RGB_Colourspace(
    'ALEXA Wide Gamut',
    ALEXA_WIDE_GAMUT_PRIMARIES,
    ALEXA_WIDE_GAMUT_WHITEPOINT,
    ALEXA_WIDE_GAMUT_ILLUMINANT,
    ALEXA_WIDE_GAMUT_TO_XYZ_MATRIX,
    XYZ_TO_ALEXA_WIDE_GAMUT_MATRIX,
    log_encoding_ALEXALogC,
    log_decoding_ALEXALogC, )
ALEXA_WIDE_GAMUT_COLOURSPACE.__doc__ = """
*ALEXA Wide Gamut* colourspace.

References
----------
-   :cite:`ARRI2012a`

ALEXA_WIDE_GAMUT_COLOURSPACE : RGB_Colourspace
"""
