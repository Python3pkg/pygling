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

from Folder import Folder

# class Path
class Path:
	Headers     = 'Headers'
	Libraries   = 'Libraries'
	Frameworks  = 'Frameworks'

	# ctor
	def __init__( self, target, type, path ):
		self._target    = target
		self._path      = path
		self._type      = type

	# type
	@property
	def type( self ):
		return self._type

	# path
	@property
	def path( self ):
		return self._path

	# relativeToProject
	@property
	def pathRelativeToProject( self ):
		return Folder.relativeTo( self.path, self._target.projectPath )

	# isHeaders
	@property
	def isHeaders( self ):
		return self._type == Path.Headers

	# isLibraries
	@property
	def isLibraries( self ):
		return self._type == Path.Libraries

	# isFrameworks
	@property
	def isFrameworks( self ):
		return self._type == Path.Frameworks