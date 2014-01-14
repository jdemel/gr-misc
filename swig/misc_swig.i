/* -*- c++ -*- */

#define MISC_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "misc_swig_doc.i"

%{
#include "misc/music_doa.h"
#include "misc/signum_xx.h"
%}


%include "misc/music_doa.h"
GR_SWIG_BLOCK_MAGIC2(misc, music_doa);
%include "misc/signum_xx.h"
GR_SWIG_BLOCK_MAGIC2(misc, signum_xx);
