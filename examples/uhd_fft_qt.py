#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: UHD FFT Qt
# Author: Johannes Demel
# Generated: Fri Dec  6 16:25:59 2013
##################################################

from PyQt4 import Qt
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import sip
import sys
import time

class uhd_fft_qt(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "UHD FFT Qt")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("UHD FFT Qt")
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

        self.settings = Qt.QSettings("GNU Radio", "uhd_fft_qt")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.info = info = {"mboard_id":"id","mboard_serial":"serial","rx_serial":"rx","rx_subdev_name":"subname"}
        self.usrp_serial = usrp_serial = info["mboard_serial"]
        self.usrp_id = usrp_id = info["mboard_id"]
        self.db_spec = db_spec = "spec"
        self.db_serial = db_serial = info["rx_serial"]
        self.db_name = db_name = info["rx_subdev_name"]
        self.db_antenna = db_antenna = "antenna"
        self.catch_tune = catch_tune = uhd.tune_result()
        self.usrp_text = usrp_text = usrp_id + " (" + usrp_serial + ")"
        self.db_text = db_text = db_name + " (" + db_serial  + " ," + db_spec + " ," + db_antenna + ")"
        self.actual_rf = actual_rf = catch_tune.actual_rf_freq
        self.actual_dsp = actual_dsp = catch_tune.actual_dsp_freq
        self.usrp = usrp = usrp_text
        self.uhd_version = uhd_version = uhd.get_version_string()
        self.samp_rate = samp_rate = 10e6
        self.rf_label = rf_label = actual_rf
        self.gain = gain = 50
        self.dsp_label = dsp_label = actual_dsp
        self.dev_args_b200 = dev_args_b200 = "type=b200, master_clock_rate=40e6"
        self.db_label = db_label = db_text
        self.center_freq = center_freq = 900e6

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel("Sample Rate"+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(self._samp_rate_line_edit.text().toAscii())))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 4, 0, 1, 3)
        self._gain_layout = Qt.QVBoxLayout()
        self._gain_tool_bar = Qt.QToolBar(self)
        self._gain_layout.addWidget(self._gain_tool_bar)
        self._gain_tool_bar.addWidget(Qt.QLabel("Gain"+": "))
        self._gain_counter = Qwt.QwtCounter()
        self._gain_counter.setRange(0, 100, 1)
        self._gain_counter.setNumButtons(2)
        self._gain_counter.setValue(self.gain)
        self._gain_tool_bar.addWidget(self._gain_counter)
        self._gain_counter.valueChanged.connect(self.set_gain)
        self._gain_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._gain_slider.setRange(0, 100, 1)
        self._gain_slider.setValue(self.gain)
        self._gain_slider.setMinimumWidth(200)
        self._gain_slider.valueChanged.connect(self.set_gain)
        self._gain_layout.addWidget(self._gain_slider)
        self.top_grid_layout.addLayout(self._gain_layout, 5, 0, 1, 5)
        self._center_freq_tool_bar = Qt.QToolBar(self)
        self._center_freq_tool_bar.addWidget(Qt.QLabel("Center Frequency"+": "))
        self._center_freq_line_edit = Qt.QLineEdit(str(self.center_freq))
        self._center_freq_tool_bar.addWidget(self._center_freq_line_edit)
        self._center_freq_line_edit.returnPressed.connect(
        	lambda: self.set_center_freq(eng_notation.str_to_num(self._center_freq_line_edit.text().toAscii())))
        self.top_grid_layout.addWidget(self._center_freq_tool_bar, 4, 3, 1, 2)
        self.usrp_dev = uhd.usrp_source(
        	device_addr=dev_args_b200,
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.usrp_dev.set_samp_rate(samp_rate)
        self.usrp_dev.set_center_freq(center_freq, 0)
        self.usrp_dev.set_gain(gain, 0)
        self.usrp_dev.set_antenna("RX2", 0)
        self._usrp_tool_bar = Qt.QToolBar(self)
        self._usrp_tool_bar.addWidget(Qt.QLabel("USRP"+": "))
        self._usrp_label = Qt.QLabel(str(self.usrp))
        self._usrp_tool_bar.addWidget(self._usrp_label)
        self.top_grid_layout.addWidget(self._usrp_tool_bar, 3, 1, 1, 1)
        self._uhd_version_tool_bar = Qt.QToolBar(self)
        self._uhd_version_tool_bar.addWidget(Qt.QLabel("UHD"+": "))
        self._uhd_version_label = Qt.QLabel(str(self.uhd_version))
        self._uhd_version_tool_bar.addWidget(self._uhd_version_label)
        self.top_grid_layout.addWidget(self._uhd_version_tool_bar, 3, 0, 1, 1)
        self._rf_label_tool_bar = Qt.QToolBar(self)
        self._rf_label_tool_bar.addWidget(Qt.QLabel("RF Freq"+": "))
        self._rf_label_label = Qt.QLabel(str(self.rf_label))
        self._rf_label_tool_bar.addWidget(self._rf_label_label)
        self.top_grid_layout.addWidget(self._rf_label_tool_bar, 3, 3, 1, 1)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	"QT GUI Plot", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win, 0, 0, 3, 5)
        
        
        self._dsp_label_tool_bar = Qt.QToolBar(self)
        self._dsp_label_tool_bar.addWidget(Qt.QLabel("DSP Freq"+": "))
        self._dsp_label_label = Qt.QLabel(str(self.dsp_label))
        self._dsp_label_tool_bar.addWidget(self._dsp_label_label)
        self.top_grid_layout.addWidget(self._dsp_label_tool_bar, 3, 4, 1, 1)
        self._db_label_tool_bar = Qt.QToolBar(self)
        self._db_label_tool_bar.addWidget(Qt.QLabel("Daugherboard"+": "))
        self._db_label_label = Qt.QLabel(str(self.db_label))
        self._db_label_tool_bar.addWidget(self._db_label_label)
        self.top_grid_layout.addWidget(self._db_label_tool_bar, 3, 2, 1, 1)
        self.catch_result_0_0_0 = self.usrp_dev.get_antenna(0)
        self.set_db_antenna(self.catch_result_0_0_0)
        self.catch_result_0_0 = self.usrp_dev.get_subdev_spec(0)
        self.set_db_spec(self.catch_result_0_0)
        self.catch_result_0 = self.usrp_dev.get_usrp_info(0)
        self.set_info(self.catch_result_0)
        self.catch_result = self.usrp_dev.set_center_freq(center_freq, 0)
        self.set_catch_tune(self.catch_result)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.usrp_dev, 0), (self.qtgui_sink_x_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "uhd_fft_qt")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info
        self.set_db_serial(self.info["rx_serial"])
        self.set_db_name(self.info["rx_subdev_name"])
        self.set_usrp_id(self.info["mboard_id"])
        self.set_usrp_serial(self.info["mboard_serial"])

    def get_usrp_serial(self):
        return self.usrp_serial

    def set_usrp_serial(self, usrp_serial):
        self.usrp_serial = usrp_serial
        self.set_usrp_text(self.usrp_id + " (" + self.usrp_serial + ")")

    def get_usrp_id(self):
        return self.usrp_id

    def set_usrp_id(self, usrp_id):
        self.usrp_id = usrp_id
        self.set_usrp_text(self.usrp_id + " (" + self.usrp_serial + ")")

    def get_db_spec(self):
        return self.db_spec

    def set_db_spec(self, db_spec):
        self.db_spec = db_spec
        self.set_db_text(self.db_name + " (" + self.db_serial  + " ," + self.db_spec + " ," + self.db_antenna + ")")

    def get_db_serial(self):
        return self.db_serial

    def set_db_serial(self, db_serial):
        self.db_serial = db_serial
        self.set_db_text(self.db_name + " (" + self.db_serial  + " ," + self.db_spec + " ," + self.db_antenna + ")")

    def get_db_name(self):
        return self.db_name

    def set_db_name(self, db_name):
        self.db_name = db_name
        self.set_db_text(self.db_name + " (" + self.db_serial  + " ," + self.db_spec + " ," + self.db_antenna + ")")

    def get_db_antenna(self):
        return self.db_antenna

    def set_db_antenna(self, db_antenna):
        self.db_antenna = db_antenna
        self.set_db_text(self.db_name + " (" + self.db_serial  + " ," + self.db_spec + " ," + self.db_antenna + ")")

    def get_catch_tune(self):
        return self.catch_tune

    def set_catch_tune(self, catch_tune):
        self.catch_tune = catch_tune
        self.set_actual_rf(self.catch_tune.actual_rf_freq)
        self.set_actual_dsp(self.catch_tune.actual_dsp_freq)

    def get_usrp_text(self):
        return self.usrp_text

    def set_usrp_text(self, usrp_text):
        self.usrp_text = usrp_text
        self.set_usrp(self.usrp_text)

    def get_db_text(self):
        return self.db_text

    def set_db_text(self, db_text):
        self.db_text = db_text
        self.set_db_label(self.db_text)

    def get_actual_rf(self):
        return self.actual_rf

    def set_actual_rf(self, actual_rf):
        self.actual_rf = actual_rf
        self.set_rf_label(self.actual_rf)

    def get_actual_dsp(self):
        return self.actual_dsp

    def set_actual_dsp(self, actual_dsp):
        self.actual_dsp = actual_dsp
        self.set_dsp_label(self.actual_dsp)

    def get_usrp(self):
        return self.usrp

    def set_usrp(self, usrp):
        self.usrp = usrp
        self._usrp_label.setText(repr(self.usrp))

    def get_uhd_version(self):
        return self.uhd_version

    def set_uhd_version(self, uhd_version):
        self.uhd_version = uhd_version
        self._uhd_version_label.setText(str(self.uhd_version))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self._samp_rate_line_edit.setText(eng_notation.num_to_str(self.samp_rate))
        self.usrp_dev.set_samp_rate(self.samp_rate)

    def get_rf_label(self):
        return self.rf_label

    def set_rf_label(self, rf_label):
        self.rf_label = rf_label
        self._rf_label_label.setText(eng_notation.num_to_str(self.rf_label))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self._gain_counter.setValue(self.gain)
        self._gain_slider.setValue(self.gain)
        self.usrp_dev.set_gain(self.gain, 0)

    def get_dsp_label(self):
        return self.dsp_label

    def set_dsp_label(self, dsp_label):
        self.dsp_label = dsp_label
        self._dsp_label_label.setText(eng_notation.num_to_str(self.dsp_label))

    def get_dev_args_b200(self):
        return self.dev_args_b200

    def set_dev_args_b200(self, dev_args_b200):
        self.dev_args_b200 = dev_args_b200

    def get_db_label(self):
        return self.db_label

    def set_db_label(self, db_label):
        self.db_label = db_label
        self._db_label_label.setText(str(self.db_label))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.qtgui_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.usrp_dev.set_center_freq(self.center_freq, 0)
        self._center_freq_line_edit.setText(eng_notation.num_to_str(self.center_freq))
        self.set_catch_tune(self.usrp_dev.set_center_freq(self.center_freq, 0))

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
    tb = uhd_fft_qt()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

