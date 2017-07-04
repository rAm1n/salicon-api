# SALICON API

[SALICON](http://salicon.net) is a large saliency dataset based on the [MS COCO](http://mscoco.org) image dataset. This package provides Python APIs that assists in loading, parsing and visualizing the saliency annotations in SALICON. Please visit http://salicon.net/ for more information including the data, paper, tutorials, and the exact format of the annotations. The code and data format follows the [COCO API](https://github.com/pdollar/coco). Please also refer to http://mscoco.org/ for other types of annotations.

In addition to this API, please download both the images (a subset of COCO images) and annotations in order to run the demos and use the API. Both are available on the SALICON website.

* Please download, unzip, and place the images in: `./images/`
* Please download and place the annotations in: `./annotations/`




UPDATE:

* you can use gt.py to create ground truth for whole dataset.

* next_batch function has been added. Fixations have been removed in annotation files. You can use them to acclerate loading batches.

