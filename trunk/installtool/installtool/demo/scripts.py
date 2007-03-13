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
"""Sample scripts class for the Zope 3 based installtool package

$Id$
"""
__author__  = "Andrey Orlov"
__license__	= "ZPL"
__version__ = "$Revision$"
__date__ = "$Date$"
 
 
from zope.app.folder.folder import Folder 
def scriptA(context,**kw) :
    print "A:",context,kw                    
    for i in xrange(0,20) :
        print "Create folder",i
        context["name%03i" % i] = Folder()    

    return "OK"

def scriptB(context,**kw) :
    print "B:",context,kw                    
    return "OK"

def scriptC(context,**kw) :
    print "C:",context,kw                    
    return "OK"

def scriptD(context,**kw) :
    print "D:",context,kw                    
    return "OK"

def scriptE(context,**kw) :
    print "E:",context,kw                    
    return "OK"

