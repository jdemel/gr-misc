/* -*- c++ -*- */
/*
* Copyright 2013 Johannes Demel
*
* This is free software; you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation; either version 3, or (at your option)
* any later version.
*
* This software is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this software; see the file COPYING. If not, write to
* the Free Software Foundation, Inc., 51 Franklin Street,
* Boston, MA 02110-1301, USA.
*/

#ifndef INCLUDED_MISC_MUSIC_DOA_IMPL_H
#define INCLUDED_MISC_MUSIC_DOA_IMPL_H

#include <misc/music_doa.h>

namespace gr {
  namespace misc {

class music_doa_impl: public music_doa
{
private:
    typedef std::pair<double, double> doa_t;

    unsigned int d_m;
    unsigned int d_n;
    unsigned int d_nsamples;
    array_response_t d_array_response;
    unsigned int d_resolution;
//          gruel::mutex  d_mutex;

public:
    music_doa_impl(unsigned int m, unsigned int n, unsigned int nsamples,
            const array_response_t& array_response, unsigned int resolution);
    ~music_doa_impl();

    void set_array_response(const array_response_t& array_response);

    // Where all the action really happens
    int work(int noutput_items, gr_vector_const_void_star &input_items,
            gr_vector_void_star &output_items);
};

  } // namespace misc
} // namespace gr

#endif /* INCLUDED_MISC_MUSIC_DOA_IMPL_H */

