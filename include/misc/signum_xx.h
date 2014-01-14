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

#ifndef INCLUDED_MISC_SIGNUM_XX_H
#define INCLUDED_MISC_SIGNUM_XX_H

#include <misc/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace misc {
      typedef enum {SHORT = 0, INT = 1,FLOAT = 2} io_type;
    /*!
     * \brief Signum function
     * \ingroup misc
     * returns 1 for in > 0 and -1 for in < 0 and 0 for in == 0
     * http://en.wikipedia.org/wiki/Signum_function
     * Only Short, Int and Float are reasonable.
     * Char is unsigned and Complex doesn't have a greater/smaller than relation.
     */
    class MISC_API signum_xx : virtual public gr::sync_block
    {
     public:

      typedef boost::shared_ptr<signum_xx> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of misc::signum_xx.
       *
       * To avoid accidental use of raw pointers, misc::signum_xx's
       * constructor is in a private implementation
       * class. misc::signum_xx::make is the public interface for
       * creating new instances.
       */
      static sptr make(io_type type, int vlen);
    };

  } // namespace misc
} // namespace gr

#endif /* INCLUDED_MISC_SIGNUM_XX_H */

