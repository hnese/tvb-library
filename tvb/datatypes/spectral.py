# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Scientific Package. This package holds all simulators, and 
# analysers necessary to run brain-simulations. You can use it stand alone or
# in conjunction with TheVirtualBrain-Framework Package. See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2013, Baycrest Centre for Geriatric Care ("Baycrest")
#
# This program is free software; you can redistribute it and/or modify it under 
# the terms of the GNU General Public License version 2 as published by the Free
# Software Foundation. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details. You should have received a copy of the GNU General 
# Public License along with this program; if not, you can download it here
# http://www.gnu.org/licenses/old-licenses/gpl-2.0
#
#

"""

The Spectral datatypes. This brings together the scientific and framework
methods that are associated with the Spectral datatypes.

.. moduleauthor:: Stuart A. Knock <Stuart@tvb.invalid>

"""

import tvb.datatypes.spectral_scientific as spectral_scientific
import tvb.datatypes.spectral_framework as spectral_framework
from tvb.basic.logger.builder import get_logger

LOG = get_logger(__name__)


class FourierSpectrum(spectral_scientific.FourierSpectrumScientific,
                      spectral_framework.FourierSpectrumFramework):
    """
    This class brings together the scientific and framework methods that are
    associated with the FourierSpectrum datatype.
    
    ::
        
                        FourierSpectrumData
                                 |
                                / \\
        FourierSpectrumFramework   FourierSpectrumScientific
                                \ /
                                 |
                          FourierSpectrum
        
    
    """
    pass


class WaveletCoefficients(spectral_scientific.WaveletCoefficientsScientific,
                          spectral_framework.WaveletCoefficientsFramework):
    """
    This class brings together the scientific and framework methods that are
    associated with the WaveletCoefficients datatype.
    
    ::
        
                          WaveletCoefficientsData
                                     |
                                    / \\
        WaveletCoefficientsFramework   WaveletCoefficientsScientific
                                    \ /
                                     |
                            WaveletCoefficients
        
    
    """
    pass



class CoherenceSpectrum(spectral_scientific.CoherenceSpectrumScientific,
                        spectral_framework.CoherenceSpectrumFramework):
    """
    This class brings together the scientific and framework methods that are
    associated with the CoherenceSpectrum datatype.
    
    ::
        
                          CoherenceSpectrumData
                                   |
                                  / \\
        CoherenceSpectrumFramework   CoherenceSpectrumScientific
                                  \ /
                                   |
                            CoherenceSpectrum
        
    
    """
    pass
    
class ComplexCoherenceSpectrum(spectral_scientific.ComplexCoherenceSpectrumScientific,
                               spectral_framework.ComplexCoherenceSpectrumFramework):
    """
    This class brings together the scientific and framework methods that are
    associated with the ComplexCoherenceSpectrum datatype.
    
    ::
        
                          ComplexCoherenceSpectrumData
                                   |
                                  / \\
 ComplexCoherenceSpectrumFramework   ComplexCoherenceSpectrumScientific
                                  \ /
                                   |
                            ComplexCoherenceSpectrum
        
    
    """
    pass




if __name__ == '__main__':
    # Do some stuff that tests or makes use of this module...
    LOG.info("Testing %s module..." % __file__)
    
    # Check that all default Spectral datatypes initialize without error.
    FOURIER_SPECTRUM           = FourierSpectrum()
    COHERENCE_SPECTRUM         = CoherenceSpectrum()
    COMPLEX_COHERENCE_SPECTRUM = ComplexCoherenceSpectrum()
    WAVELET_COEFFICIENTS       = WaveletCoefficients()
    
    LOG.info("Default Spectral datatypes initialized without error...")
