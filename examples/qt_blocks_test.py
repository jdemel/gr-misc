#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: new Qt GUI blocks test
# Generated: Wed Dec  4 17:42:54 2013
##################################################

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import misc
import sip
import sys

class qt_blocks_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "new Qt GUI blocks test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("new Qt GUI blocks test")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "qt_blocks_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.row_span = row_span = 2
        self.col_span = col_span = 2

        ##################################################
        # Blocks
        ##################################################
        self.tab1 = Qt.QTabWidget()
        self.tab1_widget_0 = Qt.QWidget()
        self.tab1_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab1_widget_0)
        self.tab1_grid_layout_0 = Qt.QGridLayout()
        self.tab1_layout_0.addLayout(self.tab1_grid_layout_0)
        self.tab1.addTab(self.tab1_widget_0, "")
        self.top_grid_layout.addWidget(self.tab1, 1, 0, 1, 2)
        self.tab0 = Qt.QTabWidget()
        self.tab0_widget_0 = Qt.QWidget()
        self.tab0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab0_widget_0)
        self.tab0_grid_layout_0 = Qt.QGridLayout()
        self.tab0_layout_0.addLayout(self.tab0_grid_layout_0)
        self.tab0.addTab(self.tab0_widget_0, "")
        self.top_grid_layout.addWidget(self.tab0, 0, 0, 1, 2)
        self.misc_numbersink_0 = misc.numbersink(complex, "Number Plot", "Units", samp_rate, -100.0, 100.0, 1.0, 10, 0.0, 15, False, 0, "Number Plot", False, True)
        self._misc_numbersink_0_win = self.misc_numbersink_0.get_pyqwidget()
        self.tab1_grid_layout_0.addWidget(self._misc_numbersink_0_win,  0, 0, 1, 1)
          
        self.misc_compass_0_0 = misc.compass(False, "nice", "simple", 15)
        self._misc_compass_0_0_win = self.misc_compass_0_0.get_pyqwidget()
        self.tab0_grid_layout_0.addWidget(self._misc_compass_0_0_win, 0, 1, 1, 2)
        self.misc_compass_0 = misc.compass(False, "nice", "simple", 15)
        self._misc_compass_0_win = self.misc_compass_0.get_pyqwidget()
        self.tab0_grid_layout_0.addWidget(self._misc_compass_0_win, 0, 0, 1, 2)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((180, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((180, ))
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_1, 0), (self.misc_numbersink_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_1, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.misc_compass_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.misc_compass_0_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "qt_blocks_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.misc_numbersink_0.set_samp_rate(self.samp_rate)

    def get_row_span(self):
        return self.row_span

    def set_row_span(self, row_span):
        self.row_span = row_span

    def get_col_span(self):
        return self.col_span

    def set_col_span(self, col_span):
        self.col_span = col_span

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    qapp = Qt.QApplication(sys.argv)
    tb = qt_blocks_test()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

