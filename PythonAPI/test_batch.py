from salicon.salicon import SALICON
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt



dataDir='data'
dataType='val2014'
annFile='%s/annotations/fixations_%s_clean.json'%(dataDir,dataType)
outDir = '{0}/gt/'.format(dataDir)
img_dir = '/media/ramin/monster/dataset/saliency/salicon/images/'
gt_dir = '/media/ramin/monster/dataset/saliency/salicon/gt/'


# initialize COCO api for instance annotations
salicon=SALICON(annFile)



batch = salicon.next_batch(32,img_dir,gt_dir)
