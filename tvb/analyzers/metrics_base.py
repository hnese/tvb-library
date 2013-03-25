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
.. moduleauthor:: bogdan.neacsa <bogdan.neacsa@codemart.ro>
"""

import tvb.basic.traits.core as core


class BaseTimeseriesMetricAlgorithm(core.Type):
    """
    This is a base class for all metrics on timeSeries dataTypes.
    Metric means an algorithm computing a single value for an entire TimeSeries.
    """
    ### Make sure this "abstract" class does not get listed in UI.
    _base_classes = ['BaseTimeseriesMetricAlgorithm']
    
    accept_filter = None
    
    
    def evaluate(self):
        """
        This method needs to be implemented in each subclass.
        Will describe current algorithms.
        :return: single value
        """
        msg = " ".join(("Every metric algorithm should implement an 'evaluate'",
                        "method that returns the metric result."))
        raise Exception(msg)



