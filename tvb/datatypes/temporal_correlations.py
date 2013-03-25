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

The Temporal Correlation datatypes. This brings together the scientific and
framework methods that are associated with the Temporal Correlation datatypes.

.. moduleauthor:: Stuart A. Knock <Stuart@tvb.invalid>

"""

import tvb.datatypes.temporal_correlations_scientific as temporal_correlations_scientific
import tvb.datatypes.temporal_correlations_framework as temporal_correlations_framework
from tvb.basic.logger.builder import get_logger

LOG = get_logger(__name__)


class CrossCorrelation(temporal_correlations_scientific.CrossCorrelationScientific,
                       temporal_correlations_framework.CrossCorrelationFramework):
    """
    This class brings together the scientific and framework methods that are
    associated with the CrossCorrelation datatype.
    
    ::
        
                         CrossCorrelationData
                                  |
                                 / \\
        CrossCorrelationFramework   CrossCorrelationScientific
                                 \ /
                                  |
                           CrossCorrelation
        
    
    """
    pass




if __name__ == '__main__':
    # Do some stuff that tests or makes use of this module...
    LOG.info("Testing %s module..." % __file__)
    
    # Check that all default Temporal Correlation datatypes initialize without error.
    CROSS_CORRELATION = CrossCorrelation()
    
    LOG.info("Default Temporal Correlation datatypes initialized without error...")
