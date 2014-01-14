/* -*- c++ -*- */
// Copyright 2014 Ettus Research LLC
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "signum_xx_impl.h"

namespace gr {
  namespace misc {

    signum_xx::sptr
    signum_xx::make(io_type type, int vlen)
    {
        if(type == SHORT){
            return gnuradio::get_initial_sptr
                    (new signum_xx_impl<short>(vlen));
        }
        else if(type == INT){
            return gnuradio::get_initial_sptr
                    (new signum_xx_impl<int>(vlen));
        }

        else if(type == FLOAT){
            return gnuradio::get_initial_sptr
                    (new signum_xx_impl<float>(vlen));
        }
        return gnuradio::get_initial_sptr
                (new signum_xx_impl<float>(vlen));
    }

    /*
     * The private constructor
     */
    template <typename T>
    signum_xx_impl<T>::signum_xx_impl(int vlen)
      : gr::sync_block("signum_xx",
              gr::io_signature::make(vlen, vlen, sizeof(T)),
              gr::io_signature::make(vlen, vlen, sizeof(T)))
    {}

    /*
     * Our virtual destructor.
     */
    template <typename T>
    signum_xx_impl<T>::~signum_xx_impl()
    {
    }

    template <typename T>
    int
    signum_xx_impl<T>::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const T *in = (const T *) input_items[0];
        T *out = (T *) output_items[0];

        for(int i = 0; i < noutput_items; i++){
            *out = (0.0 < (*in)) - ((*in) < 0.0);
            in++;
            out++;
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace misc */
} /* namespace gr */

