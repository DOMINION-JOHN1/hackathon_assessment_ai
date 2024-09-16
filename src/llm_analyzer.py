from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import logging


class LLMAnalyzer:
    def __init__(self, api_key):
        self.logger = logging.getLogger(__name__)
        self.model = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo")

    def _create_prompt(self, content):

        prompt = """
            Analyze the following Jupyter notebook content and provide scores (0-20) and detailed feedback for each of 
            these criteria:
            1. Technical accuracy
            2. Business understanding
            3. AI justification
            4. Code quality
            5. Documentation
            After which you should provide a total score  in percentage (which is a Total sum of all the scores for each
             criterion and please not the total average of the Total criteria score)
            For each criterion, explain why you gave that score and provide specific suggestions for improvement.

            Respond in the following JSON format that wil enable me to call a particular key:
            {{
            Technical accuracy (score):
            Explanation and suggestions
            Business understanding (score):
            Explanation and suggestions
            AI justification (score):
            Explanation and suggestions
            Code quality (score):
            Explanation and suggestions
            Documentation (score):
            Explanation and suggestions

            Total score: Total sum score in percentage
            Overall explanation: Overall explanation
             }}

            """
        prompt = PromptTemplate.from_template(prompt)

        formatted_prompt = prompt.format(context="Ensure to follow every instructions in prompt", question="Here is the notebook for review" + content)
        response = self.model.invoke(formatted_prompt)
        return response.content
