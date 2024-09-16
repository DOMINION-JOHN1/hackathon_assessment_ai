# pylint: disable=import-error
import logging
from src.notebook_reader import NotebookReader
from src.llm_analyzer import LLMAnalyzer


class AIFeedbackSystem:
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)
        self.notebook_reader = NotebookReader()
        self.llm_analyzer = LLMAnalyzer(config['openai_api_key'])

    def evaluate_notebook(self, notebook_path):
        try:
            notebook_content = self.notebook_reader.read_notebook(notebook_path)
            llm_analysis = self.llm_analyzer._create_prompt(notebook_content)
            return llm_analysis
        except Exception as e:
            self.logger.error(f"Error evaluating notebook: {str(e)}")
            raise
