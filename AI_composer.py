# Asumptions:
# Vector Algorithm is used in it
# 1. Melody is monophonic
# 2. Define time class into deferent core class
# Sequence learning Models is a model for it 
# Have both Long and Short term memory storage thing in it 
# 
#	Train it until You get
#	Best Loss so far encountered, Saving Model....
#	
#	After that type in 
#	python rnn_sample --config_file model/folder/x.config



import urllib
import zipfile
import nottingham_util
import rnn

url = "www-etud.iro.umontreal.ca/~boulanni/Nottingham.zip"
urllib.urlretrive(url, 'dataset.zip')

zip = zipfile.ZipFile(r'dataset.zip')
zip.extractall('data')

nottingham_util.create_model()
rnn.train_model()

