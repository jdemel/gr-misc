//* -*- c++ -*- */
/* 
 * Copyright 2013 Johannes Demel.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "music_doa_impl.h"
#include <armadillo>
#include <volk/volk.h>

namespace gr {
  namespace misc {

music_doa::sptr
    music_doa::make(unsigned int m, unsigned int n, unsigned int nsamples, const array_response_t& array_response, unsigned int resolution)
    {
      return gnuradio::get_initial_sptr
        (new music_doa_impl(m, n, nsamples, array_response, resolution));
    }

    /*
     * The private constructor
     */
    music_doa_impl::music_doa_impl(unsigned int m, unsigned int n, unsigned int nsamples, const array_response_t& array_response, unsigned int resolution)
      : gr::sync_block("music_doa",
              gr::io_signature::make(1, 1, nsamples * sizeof(gr_complex)),
              gr::io_signature::make3(1, 3, n * sizeof(float), n * sizeof(float), resolution * sizeof(float) )),
              d_m(m),
                  d_n(n),
                  d_nsamples(nsamples),
                  d_array_response(array_response),
                  d_resolution(resolution)
    {
        assert(m > 0);
        assert(m >= n);
        assert((nsamples > 0) && ((nsamples % m) == 0));
        assert(resolution > 0);
        assert(array_response.size() == resolution);
        assert(array_response[0].size() == m);

        fprintf(stderr, "[%s<%ld>] MUSIC DOA: M: %d, N: %d, # samples: %d, angular resolution: %d\n", name().c_str(), unique_id(), m, n, nsamples, resolution);
    }

    /*
     * Our virtual destructor.
     */
    music_doa_impl::~music_doa_impl()
    {
    }

    int
    music_doa_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
        const gr_complex* in = static_cast<const gr_complex*>(input_items[0]);
        gr_complexd* data = new gr_complexd[d_nsamples];    // FIXME: Move outside
        volk_32f_convert_64f((double*)data, (float*)in, d_nsamples*2);

        // Correlation estimation
        arma::cx_mat x(arma::cx_rowvec(data, d_nsamples));
        unsigned int average_over = d_nsamples / d_m;
        x.reshape(d_m, average_over);   // (n_rows, n_cols)
        arma::cx_mat R = x * x.t() / (double) average_over;

        // Eigendecomposition
        arma::colvec eigvals;
        arma::cx_mat eigvec;
        arma::eig_sym(eigvals, eigvec, R);

        // Generate a base for the noise subspace
        arma::cx_mat G = eigvec.cols(0, d_m - d_n - 1);

        std::vector<doa_t> vDOAs(d_n, std::make_pair(0, 0));

        float* out_spectrum = NULL;
        if (output_items.size() > 2){
            out_spectrum = static_cast<float*>(output_items[2]);
        }

        { // Create a sub scope for lock (Currently not used)
//            gruel::scoped_lock guard(d_mutex);

            // Go through every specified angle and calculate the correlation between input and expected response
            for (unsigned int step = 0; step < d_resolution; step++) {
                const antenna_response_t& antenna_response = d_array_response[step];
                //arma::cx_mat a(arma::cx_rowvec(&antenna_response.begin(), antenna_response.size());
                //arma::cx_mat c = a * G;
                //arma::cx_mat d = c * c.t();

                // Convert antenna response to Armadillo
                arma::cx_vec a(d_m);
                for (int t = 0; t < d_m; t++)
                    a[t] = antenna_response[t];

                double strength = 1.0 / pow((arma::norm(arma::trans (G) * a, 2)),2);

                if (out_spectrum != NULL)
                    out_spectrum[step] = strength;
//                static bool bFirst = false;
//                if (bFirst == false) {
//                    //fprintf(stderr, "%03i = %f\n", step, strength);
//                    if (step == (d_resolution - 1))
//                        bFirst = true;
//                }
                // Check if current strength is greater former maximum.
                for (int i = 0; i < d_n; i++) {
                    const doa_t& doa = vDOAs[i];
                    if (strength > doa.second) {
                        double angle = (double) step * 360.0
                                / (double) d_resolution;
                        //vDOAs[i] = std::make_pair(angle, strength);
                        vDOAs.insert(vDOAs.begin() + i,
                                std::make_pair(angle, strength));
                        vDOAs.pop_back();
                        //fprintf(stderr, "Angle = %f\n", angle);
                        break;
                    }
                }
            }

        }   // Lock

        float* out = static_cast<float*>(output_items[0]);
        float* lvl = NULL;
        if (output_items.size() > 1)
            lvl = static_cast<float*>(output_items[1]);
        for (int i = 0; i < d_n; i++) {
            //fprintf(stderr, "Max = %f\n", vDOAs[i].first);
            out[i] = vDOAs[i].first;    //float(tmpout[i]);
            lvl[i] = vDOAs[i].second;
        }
        //delete[] tmpout;

        delete[] data;

        return 1;
    }

    void
    music_doa_impl::set_array_response(const array_response_t& array_response)
    {
        assert(array_response.size() == d_resolution);
        assert(array_response[0].size() == d_m);

        fprintf(stderr, "[%s<%ld>] Updating array response\n", name().c_str(), unique_id());

//        gruel::scoped_lock guard(d_mutex);

        d_array_response = array_response;
    }

  } /* namespace misc */
} /* namespace gr */

