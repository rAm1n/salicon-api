


""" run this file to create ground truth for the whole dataset"""


from salicon.salicon import SALICON
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt



dataDir='data'
dataType='val2014'
annFile='%s/annotations/fixations_%s.json'%(dataDir,dataType)
outDir = '{0}/gt/'.format(dataDir)


# initialize COCO api for instance annotations
salicon=SALICON(annFile)


# In[4]:

# get all images 
imgIds = salicon.getImgIds();


for Id in imgIds:
	continue 
	img = salicon.loadImgs(Id)[0]
	I = io.imread('%s/images/%s'%(dataDir, img['file_name']))
	annIds = salicon.getAnnIds(imgIds=img['id'])
	anns = salicon.loadAnns(annIds)	
	gt = salicon.buildFixMap(anns)
	io.imsave(outDir+ img['file_name'], gt)	
	print(Id)

