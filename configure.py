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

import argparse, os

from Makefile import Makefile
from Makefile import Target

# Entry point
if __name__ == "__main__":
	# Parse arguments
	parser = argparse.ArgumentParser( description = 'Yet Another Project Generator' )
	
	parser.add_argument( 'src', type = str, help = 'Source Path' )
	parser.add_argument( 'dst', type = str, help = 'Binary Path' )
	parser.add_argument( 'name', type = str, help = 'Solution Name' )
	parser.add_argument( 'target', type = str, help = 'Target' )

	args = parser.parse_args()

	# Generate project
	Makefile.setPaths( os.path.abspath( args.src ), os.path.abspath( args.dst ) )
	Makefile.Initialize( args.name, args.target, (lambda fileName: execfile( fileName )) )

	# Build config
	platform	= args.target
	scripting 	= 'Lua'
	sound		= 'OpenAL'
	stage		= True
	ui			= True
	network		= False
	rendering	= 'OpenGL'
	xml			= True
	identifier	= ''

	execfile( Makefile.SourceDir + '/Makefile.py' )

	Makefile.Generate()
