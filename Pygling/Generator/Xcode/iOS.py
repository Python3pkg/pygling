#################################################################################
#
# The MIT License (MIT)
#
# Copyright (c) 2015 Dmitry Sovetov
#
# https://github.com/dmsovetov
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#################################################################################

import os

from .Xcode5 	import Xcode5
from ..Template import Template

# class iOS
class iOS( Xcode5 ):
	# ctor
	def __init__( self, platform ):
		Xcode5.__init__( self )

	# getPlatformId
	def getPlatformId( self ):
		return 'ios'

	# commandLineToolsSupported
	@property
	def commandLineToolsSupported( self ):
		return False

	# getProjectSettings
	def getProjectSettings( self ):
		if not self.makefile.get( 'SDK' ):
			self.makefile.set( 'SDK', self.makefile.platform.list_sdks( 'iPhoneOS' )[0].name )

		return {
			'Debug': {
				'ARCHS':                        'armv7',
				'SDKROOT':                      self.makefile.get( 'SDK' ),
		        'TARGETED_DEVICE_FAMILY':       '"1,2"',
			    'ALWAYS_SEARCH_USER_PATHS':     'NO',
			    'CODE_SIGN_IDENTITY':           '"iPhone Developer"',
		        'IPHONEOS_DEPLOYMENT_TARGET':   '6.0'
			},
		    'Release': {
				'ARCHS':                        'armv7',
				'SDKROOT':                      self.makefile.get( 'SDK' ),
		        'TARGETED_DEVICE_FAMILY':       '"1,2"',
			    'ALWAYS_SEARCH_USER_PATHS':     'NO',
		        'CODE_SIGN_IDENTITY':           '"iPhone Developer"',
		        'IPHONEOS_DEPLOYMENT_TARGET':   '6.0'
		    }
		}