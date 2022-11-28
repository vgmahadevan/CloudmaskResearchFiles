# Cloudmask Research Files

This repository will contain outputs of cloudmask runs and other associated files.

**graphMaker.py** - scans output logs for training and validation loss and accuracy; creates a directory called 'graphs' to store png files graphing loss and accuracy against epochs.

**10_30_22** - This was an initial run of cloudmask. Cloudmask was run on all gpus and with the default hyperparameter configuration.

**11_20_22** - There were three runs done on this date, all on the a100 gpu only. 

The log and graphs directory labeled '100' had a 100-epoch run and a variable learning rate with the intent of finding an ideal one in an efficient manner--this did not come to be of much use.

For the log and graphs directory labeled 50 -- a learning rate of 0.0015 was used. It seems to have generated a lot of volatility in the graphs which may be expected with a higher learning rate. However, this is strange when considered with the next run.

For the log and graphs directory labeled lr_.008, a learning rate of 0.008 was used. I was intending to do a 0.0008 but mistakenly entered .008. However, this resulted in very smooth graphs, which is strange since the much smaller learning rate of 0.0015 had so much volatility. I will replicate both runs to see if there's something to this or not.

**11_27_22** - The run labeled '1' is a run with a learning rate of 0.0008. 

The run labeled '2' is a run with a learning rate of 0.008. There wasn't really a noticable difference between these two runs or the previous lr = 0.008 run.

