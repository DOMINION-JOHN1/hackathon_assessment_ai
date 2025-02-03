import os
import tempfile
import streamlit as st
import yaml
from src.feedback_system import AIFeedbackSystem

# Load configuration file
with open ('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Initialize the feedback system
feedback_system = AIFeedbackSystem(config)


def main():
    st.title("Jupyter Notebook Feedback App")
    st.write("Upload a Jupyter Notebook (.ipynb) file to receive feedback.")

    # File uploader for Jupyter Notebooks
    uploaded_file = st.file_uploader("Choose a Jupyter Notebook file", type="ipynb")

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
            temp_file.write(uploaded_file.read())
            notebook_path = temp_file.name

        st.write("Evaluating notebook...")
        st.write(notebook_path)

        try:
            # Evaluate the notebook and get feedback
            feedback = feedback_system.evaluate_notebook(notebook_path)

            # Display feedback
            st.success("Evaluation completed!")
            st.markdown(feedback)
        except Exception as e:
            st.error(f"An error occurred: {e}")
        finally:
            # Clean up the temporary file
            os.remove(notebook_path)

if __name__ == "__main__":
    main()
