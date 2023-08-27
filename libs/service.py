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
import os.path
import pathlib

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
        self._watchedDirectory = self._addon.getSetting('watched_folder')

        self._guiManager = GuiManager(0, self._ADDON_ID, self._DEFAULT_IMAGE_URL, self._FANART)

        self._MONITOR = self._guiManager.getMonitor()

        if not kodionUtils.exists(self._tmpDirectory):
            kodionUtils.mkdir(self._tmpDirectory)


    @staticmethod
    def showPicture(media):
        xbmc.executebuiltin('ShowPicture(' + media + ')')

    @staticmethod
    def showVideo(media):
        pass

    @staticmethod
    def getMediaType(media):
        suffix = pathlib.Path(media).suffix.lower()
        if suffix in ['.apng', '.bmp', '.cbz', '.gif', '.ico', '.jp2', '.jpg', '.jpeg', '.pcx', '.png', '.rs0s', '.tga',
                      '.tif', '.tiff', '.webp', '.zip', '.arw', '.cr2', '.dng', '.nef', '.mpo']:
            return 1
        elif suffix in ['.avi', '.mpeg', '.wmv', '.asf', '.flv', '.mkv', '.mka', '.mp4', '.m4a', '.aac', '.nut', '.ogg',
                        '.ogm', '.3gp', '.vivo', '.pva', '.nuv', '.nsv', '.nsa', '.fli', '.flc', '.wtv', '.trp' '.f4v']:
            return 2

        return 0

    def getCatchedMedia(self):
        return self._addon.getSetting('catched_media')

    def showMedia(self, media):
        if bool(media) and kodionUtils.exists(media):
            mediaType = self.getMediaType(media)
            {
                1: self.showPicture,
                2: self.showVideo
            }[mediaType](media)

    def getNewMedia(self, default):
        dirs, files = kodionUtils.listdir(self._watchedDirectory)

        if files is not None and len(files) > 0:
            for file in files:
                srcFile = os.path.join(self._watchedDirectory, file)
                if kodionUtils.exists(srcFile) and self.getMediaType(srcFile) != 0:
                    dstFile = os.path.join(self._tmpDirectory, file)
                    # TODO: check if old media has the same filename
                    if kodionUtils.copy(srcFile, dstFile):
                        kodionUtils.delete(srcFile)
                        self._addon.setSetting('catched_media', dstFile)
                        return dstFile

        return default

    def DoSome(self):

        media = self.getCatchedMedia()

        if self._addon.getSetting('enabled') == 'true':
            media = self.getNewMedia(media)
            self.showMedia(media)
            # TODO: DELETE old catched files

        while not self._MONITOR.abortRequested():

            if self._addon.getSetting('enabled') == 'true':
                media = self.getNewMedia(None)
                self.showMedia(media)
                # TODO: DELETE old catched files

            if self._MONITOR.waitForAbort(10):
                break


