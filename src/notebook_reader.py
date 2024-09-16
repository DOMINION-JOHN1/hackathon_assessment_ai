import nbformat
import logging

class NotebookReader:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def read_notebook(self, notebook_path):
        try:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)
            
            content = ""
            for cell in nb.cells:
                if cell.cell_type == 'markdown':
                    content += cell.source + "\n\n"
                elif cell.cell_type == 'code':
                    content += f"```python\n{cell.source}\n```\n\n"
            
            return content
        except Exception as e:
            self.logger.error(f"Error reading notebook: {str(e)}")
            raise