from WineQuality.config.configuration import ConfigurationManager
from WineQuality.components.data_transformation import DataTransformation
from pathlib import Path
from WineQuality import logger


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    
    def __init__(self):
        pass
    
    def main(self):
        
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
                
            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation_config = DataTransformation(config=data_transformation_config)
                data_transformation_config.train_test_spliting()
                
            else:
                raise Exception("Your data scheme is not valis")
            
        except Exception as e:
            print(e)