#!/usr/bin/env python
# Copyright 2014 Ettus Research LLC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gnuradio import gr, gr_unittest, blocks
from gnuradio import blocks
import misc_swig as misc

class qa_signum_xx(gr_unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_short(self):
        tb = gr.top_block()

        data = [5, 0, 0, -1, -3, -10]
        exp = [1, 0, 0, -1, -1, -1]
        vlen = 1
        src = blocks.vector_source_s(data, False, vlen)
        sign = misc.signum_xx(misc.SHORT, vlen)
        snk = blocks.vector_sink_s(vlen)
        tb.connect(src, sign, snk)
        tb.run()
        res = snk.data()
        self.assertTupleEqual(res, tuple(exp))

    def test_002_int(self):
        tb = gr.top_block()

        data = [5, 0, 0, -1, -3, -10]
        exp = [1, 0, 0, -1, -1, -1]
        vlen = 1
        src = blocks.vector_source_i(data, False, vlen)
        sign = misc.signum_xx(misc.INT, vlen)
        snk = blocks.vector_sink_i(vlen)
        tb.connect(src, sign, snk)
        tb.run()
        res = snk.data()
        self.assertTupleEqual(res, tuple(exp))

    def test_003_float(self):
        tb = gr.top_block()

        data = [0.5, 0, 0, -0.1, -30.0, -10]
        exp = [1, 0, 0, -1, -1, -1]
        vlen = 1
        src = blocks.vector_source_f(data, False, vlen)
        sign = misc.signum_xx(misc.FLOAT, vlen)
        snk = blocks.vector_sink_f(vlen)
        tb.connect(src, sign, snk)
        tb.run()
        res = snk.data()
        self.assertTupleEqual(res, tuple(exp))



if __name__ == '__main__':
    gr_unittest.run(qa_signum_xx)
