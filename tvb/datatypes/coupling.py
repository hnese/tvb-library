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

The Coupling datatypes. This brings together the scientific and framework 
methods that are associated with the Coupling datatypes.

.. moduleauthor:: Paula Sanz Leon <paula@tvb.invalid>

"""

from tvb.basic.logger.builder import get_logger
import tvb.datatypes.coupling_scientific as coupling_scientific
import tvb.datatypes.coupling_framework as coupling_framework


LOG = get_logger(__name__)


class Coupling(coupling_scientific.CouplingScientific, coupling_framework.CouplingFramework):
    """
    This class brings together the scientific and framework methods that are
    associated with the Coupling datatypes.
    
    ::
        
                           CouplingData
                                 |
                                / \\
               CouplingFramework   CouplingScientific
                                \ /
                                 |
                              Coupling
        
    
    """
    #_is_base = True
    pass


class LinearCoupling(coupling_scientific.LinearCouplingScientific,
                     coupling_framework.LinearCouplingFramework, Coupling):
    """
    This class brings together the scientific and framework methods that are
    associated with the Coupling datatypes.
    
    ::
        
                        LinearCouplingData
                                 |
                                / \\
        LinearCouplingFramework    LinearCouplingScientific
                                \ /
                                 |
                          LinearCoupling
        
    
    """
    pass


class SigmoidalCoupling(coupling_scientific.SigmoidalCouplingScientific,
                        coupling_framework.SigmoidalCouplingFramework, Coupling):
    """
    This class brings together the scientific and framework methods that are
    associated with the Coupling datatypes.
    
    ::
        
                        SigmoidalCouplingData
                                 |
                                / \\
     SigmoidalCouplingFramework     SigmoidalCouplingScientific
                                \ /
                                 |
                          SigmoidalCoupling
        
    
    """
    pass
    
    
if __name__ == '__main__':
    # Do some stuff that tests or makes use of this module...
    LOG.info("Testing %s module..." % __file__)
    
    # Check that all default Coupling datatypes initialize without error.
    LINEAR_COUPLING = LinearCoupling()
    SIGMOIDAL_COUPLING = SigmoidalCoupling()

    LOG.info("Default Coupling datatypes initialized without error...")