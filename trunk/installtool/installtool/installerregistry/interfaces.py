### -*- coding: utf-8 -*- #############################################
# Разработано компанией Ключевые Решения (http://keysolutions.ru/) 
# Все права защищены, 2006-2007
#
# Developed by Key Solutions (http://keysolutions.ru/)
# All right reserved, 2006-2007
#######################################################################
# Licensed under the Zope Public License, Version 2.1 (the "License"); you
# may not use this file except in compliance with the License. A copy of the
# License should accompany this distribution.
#
# This software distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
#######################################################################
"""Interfaces for the Zope 3 based installerregistry package

$Id$
"""
__author__  = "Andrey Orlov, 2007 02 14"
__license__	= "ZPL"
__version__ = "$Revision$"
__date__ = "$Date$"
 
from zope.interface import Interface

from zope.schema import Text, TextLine, Field, Bool, Datetime
                
class IInstallerRegistry(Interface) :
    
    def registerScript(script,factory) :
        """ Register script for factory """
        
    def queryScript(factory) :
        """ Return all scripts for this factory """
    
                