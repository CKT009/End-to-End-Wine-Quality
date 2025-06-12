from WineQuality.config.configuration import ConfigurationManager
from WineQuality.components.model_evaluation import ModelEvaluation
from pathlib import Path
from WineQuality import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass 
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()