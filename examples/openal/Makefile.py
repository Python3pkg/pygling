StaticLibrary( 'openal', sources = [ 'Alc', 'OpenAL32' ], paths = [ 'include', 'OpenAL32/Include' ], defines = [ 'AL_BUILD_LIBRARY', 'AL_ALEXT_PROTOTYPES' ] )