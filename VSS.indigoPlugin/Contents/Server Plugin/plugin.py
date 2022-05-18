#! /usr/bin/env python
# -*- coding: utf-8 -*-
####################
# Copyright (c) 2014, Perceptive Automation, LLC. All rights reserved.
# http://www.indigodomo.com

import indigo

import os
import sys
import random
import struct
import json
import select

# Note the "indigo" module is automatically imported and made available inside
# our global name space by the host process.

################################################################################
class Plugin(indigo.PluginBase):
	########################################
	def __init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs):
		super(Plugin, self).__init__(pluginId, pluginDisplayName, pluginVersion, pluginPrefs)
		self.debug = True

	def startup(self):
		self.debugLog(u"startup called")

	def shutdown(self):
		self.debugLog(u"shutdown called")

	########################################
	def runConcurrentThread(self):
		try:
			while True:
				self.sleep(.5)
		except self.StopThread:
			pass	# Optionally catch the StopThread exception and do any needed cleanup.

	########################################
	def validateDeviceConfigUi(self, valuesDict, typeId, devId):
		return (True, valuesDict)

	########################################
	def deviceStartComm(self, dev):
		# Called when communication with the hardware should be started.

		# subModel is set in UI so it is inside pluginProps, but we want to push the value
		# down into the actual dev.subModel attribute:
        
		subModel = dev.pluginProps.get("subModel", "")
		if dev.subModel != subModel:
			dev.subModel = subModel
			dev.replaceOnServer()

#		if dev.enabled and dev.configured:
#			tag = dev.pluginProps.get("tag", "")
#			self.processTag(dev, tag, parsed_json)

	########################################
	def deviceStopComm(self, dev):
		# Called when communication with the hardware should be shutdown.
		pass

	########################################
	# General Action callback
	######################
	def actionControlGeneral(self, action, dev):
		###### BEEP ######
		if action.deviceAction == indigo.kDeviceGeneralAction.Beep:
			# Beep the hardware module (dev) here:
			# ** IMPLEMENT ME **
			indigo.server.log(u"sent \"%s\" %s" % (dev.name, "beep request"))

	########################################
	# Custom Plugin Action callbacks (defined in Actions.xml)
	######################
	def setSecuritySystemState(self, pluginAction, dev):
		try:
			newState = pluginAction.props.get(u"securitySystemState", "disarm")
		except ValueError:
			indigo.server.log(u"set alarm state action to device \"%s\" -- invalid alarm state value %s" % (dev.name,), isError=True)
			return

		# Command hardware module (dev) to set alarm state here:
		# ** IMPLEMENT ME **
		sendSuccess = True		# Set to False if it failed.

		if sendSuccess:
			# If success then log that the command was successfully sent.
			indigo.server.log("Setting security system state to " + newState)
			if newState == "0":
				uiv = "stay arm"
				imageRef = indigo.kStateImageSel.SensorOn
			elif newState == "1":
				uiv = "away arm"
				imageRef = indigo.kStateImageSel.SensorOn
			elif newState == "2":
				uiv = "night arm"
				imageRef = indigo.kStateImageSel.SensorOn
			elif newState == "3":
				uiv = "disarm"
				imageRef = indigo.kStateImageSel.SensorOff
			else:
				uiv = "triggered"
				imageRef = indigo.kStateImageSel.SensorTripped
			dev.updateStateImageOnServer(imageRef)
			dev.updateStateOnServer("securitySystemState", newState, uiValue=uiv)
		else:
			# Else log failure but do NOT update state on Indigo Server.
			indigo.server.log(u"send \"%s\" %s to %s failed" % (dev.name, "security system state mode", newState), isError=True)

