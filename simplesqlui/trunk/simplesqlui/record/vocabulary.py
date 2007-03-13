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
"""The DS vocabulary class.

$Id$
"""
__author__  = "Arvid"
__license__	= "ZPL"
__version__ = "$Revision$"
__date__ = "$Date$"
__credits__ = """Arvid, based programmer"""

from zope.interface import classProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.app.component.vocabulary import UtilityVocabulary

from interfaces import IRecordBase

class RecordBaseVocabulary(UtilityVocabulary):
    classProvides(IVocabularyFactory)
    interface = IRecordBase
    nameOnly = True
