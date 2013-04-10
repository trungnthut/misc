#!/usr/bin/env python

import json
import Image
import os

def loadAtlasInfo(atlasFile):
	f = open(atlasFile, "r")
	data = f.readlines()
	atlasData = json.loads(data[0])
	return atlasData

def cropFile(sourceImage, fileName, geometry, height, subdir="."):
	''' This function will crop image from sourceImage with geometry and save to fileName '''
	if not os.path.exists(subdir):
		os.makedirs(subdir)
	dstPath = os.path.join(subdir, fileName)
	left = geometry[0]
	lower = height - geometry[1]
	top = lower - geometry[3]
	right = left + geometry[2]
	box = (left, top, right, lower)
	region = sourceImage.crop(box)
	print "Producing file .. ", dstPath, box, geometry, height, height - geometry[1]
	subImage = Image.new(sourceImage.mode, geometry[2:])
	subImage.paste(region, (0, 0))
	subImage.save(dstPath)
	

def produceFiles(atlasInfo):
	for sourceFile in atlasInfo.keys():
		packData = atlasInfo[sourceFile]
		sourceImage = Image.open(sourceFile)
		#print dir(sourceImage)
		h = sourceImage.size[1]
		for subFile in packData.keys():
			cropFile(sourceImage, subFile + ".png", packData[subFile], h, "theme")

if __name__ == "__main__":
	atlasFile = "defaulttheme.atlas"
	atlasInfo = loadAtlasInfo(atlasFile)
	produceFiles(atlasInfo)
