# -*- coding: utf-8 -*-
# Copyright 2023 WebEye
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
#

import sys

from libs.kodion.gui_manager import *
from libs.kodion.addon import Addon
from libs.kodion.utils import Utils as kodionUtils



class service:

    def __init__(self):
        self._ADDON_ID = 'service.automated.media.player'
        self._addon = Addon(self._ADDON_ID)
        self._FANART = ''
        self._DEFAULT_IMAGE_URL = ''

        self._tmpDirectory = 'special://masterprofile/addon_data/service.automated.media.player/temp'

        self._guiManager = GuiManager(0, self._ADDON_ID, self._DEFAULT_IMAGE_URL, self._FANART)

        self._MONITOR = self._guiManager.getMonitor()

        if not kodionUtils.exists(self._tmpDirectory):
            kodionUtils.mkdir(self._tmpDirectory)

    def showMedia(self):
        if kodionUtils.exists(self._tmpDirectory):
            pass

    def DoSome(self):

        if self._addon.getSetting('enabled') == 'true':
            # TODO: search for new media

            self.showMedia()

        while not self._MONITOR.abortRequested():

            if self._addon.getSetting('enabled') == 'true':
                pass
                # TODO: search for new media

                # xbmc.executebuiltin('ShowPicture(https://images.pexels.com/photos/16226606/pexels-photo-16226606/free-photo-of-sonnenuntergang-wolkenkratzer-reflektierung-dammerung.jpeg?auto=compress&cs=tinysrgb&w=1600&lazy=load)')

            if self._MONITOR.waitForAbort(10):
                break


