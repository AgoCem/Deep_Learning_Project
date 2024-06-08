import urllib.request as request
import zipfile
import os
from pathlib import Path
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        file_path: str
        Download, if it doesn't already exists, the zip file with data, don't need a return, just to save the Data
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file
            )

            logger.info(f"{filename} is downloading with the following info: \n{headers}")
        else:
            logger.info(f"The file has already been downloaded and has {get_size(Path(self.config.local_data_file))} size")
        
        return None

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extract the downloaded zip file, don't need a return, just to save the Data
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        return None
