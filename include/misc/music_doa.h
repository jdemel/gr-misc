/* -*- c++ -*- */
/*
* Copyright 2013 Ettus Research LLC
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

#ifndef INCLUDED_MISC_MUSIC_DOA_H
#define INCLUDED_MISC_MUSIC_DOA_H

#include <misc/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace misc {

/*!
 * \brief MUSIC (Multiple Signal Classification) is a subspace oriented parametric spectrum estimator.
 * \ingroup baz
 *
 * \details
 * \param n: number of expected sinusoids,n&lt;m. (number of targets)
 * \param m: dimension of the correlation matrix. Governs the quality of the estimate. (number of antennas)
 * \param nsamples: considered samples per estimate.

    It works primarily by correlating a series of samples in a correlation matrix,
    decomposing it into orthogonal eigenvectors, building a noise subspace from the
    eigenvectors belonging to the (m-n) smallest eigenvalues, and finding the sinusoid
    frequencies, for which the projection length into this subspace equals zero.

    For this method to work, it is necessary that n&lt;m.
 *
 *
 */
class MISC_API music_doa: virtual public gr::sync_block
{
public:
    typedef boost::shared_ptr<music_doa> sptr;
    typedef std::vector<gr_complex> antenna_response_t;
    typedef std::vector<antenna_response_t> array_response_t;

    virtual void set_array_response(const array_response_t& array_response) = 0;

    /*!
     * \brief Return a shared_ptr to a new instance of misc::music_doa.
     *
     * To avoid accidental use of raw pointers, misc::music_doa's
     * constructor is in a private implementation
     * class. misc::music_doa::make is the public interface for
     * creating new instances.
     */
    static sptr make(unsigned int m, unsigned int n, unsigned int nsamples,
            const array_response_t& array_response, unsigned int resolution);
};

  } // namespace misc
} // namespace gr

#endif /* INCLUDED_MISC_MUSIC_DOA_H */

