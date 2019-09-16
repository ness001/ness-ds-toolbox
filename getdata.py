import os
import tarfile
from six.moves import urllib # for the sake of compatibility of py2 and py3

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
data_URL = DOWNLOAD_ROOT + "datasets/data/data.tgz"

data_PATH = os.path.join("datasets", "data") #local path please use os.path.join

def fetch_data_data(data_url=data_URL, data_path=data_PATH):
    os.makedirs(data_path, exist_ok=True)
    tgz_path = os.path.join(data_path, "data.tgz")
    #pull from server
    urllib.request.urlretrieve(data_url, tgz_path)
    #local
    data_tgz = tarfile.open(tgz_path)
    data_tgz.extractall(path=data_path)
    data_tgz.close()