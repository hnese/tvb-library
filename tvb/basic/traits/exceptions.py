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
.. moduleauthor:: Calin Pavel
"""

class TVBException(Exception):
    """
    Base class for all TVB exceptions.
    """
    def __init__(self, message, parent_exception=None):
        Exception.__init__(self, message, parent_exception)
        self.message = message

    def __repr__(self):
        return self.message


class ValidationException(TVBException):
    """
    Exception class for problems that occurs during MappedType 
    validation before storing it into DB.
    """
    def __init__(self, message):
        TVBException.__init__(self, message)


class MissingEntityException(TVBException):
    """
    Exception class used for cases when trying to load an entity
    from database by id or GID and none found.
    """
    def __init__(self, message):
        TVBException.__init__(self, message)
   
        
class StorageException(TVBException):
    """
    Exception class used for cases when trying to load an entity
    from database by id or GID and none found.
    """
    def __init__(self, message):
        TVBException.__init__(self, message)
        
        