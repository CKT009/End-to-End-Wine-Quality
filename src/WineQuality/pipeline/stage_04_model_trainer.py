from WineQuality.config.configuration import ConfigurationManager
from WineQuality.components.model_trainer import ModelTrainer
from pathlib import Path
from WineQuality import logger


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass 
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()