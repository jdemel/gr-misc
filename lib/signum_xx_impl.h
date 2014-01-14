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

#ifndef INCLUDED_MISC_SIGNUM_XX_IMPL_H
#define INCLUDED_MISC_SIGNUM_XX_IMPL_H

#include <misc/signum_xx.h>

namespace gr {
  namespace misc {

    template <typename T>
    class signum_xx_impl : public signum_xx
    {
     private:
      // Nothing to declare in this block.

     public:
      signum_xx_impl(int vlen);
      ~signum_xx_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace misc
} // namespace gr

#endif /* INCLUDED_MISC_SIGNUM_XX_IMPL_H */

