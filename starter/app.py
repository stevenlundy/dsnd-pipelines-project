import os
from pathlib import Path

import gradio as gr
import joblib
import pandas as pd

# Get model from pickle file
current_dir = os.path.dirname(__file__)
model = joblib.load(open(Path(current_dir) / "model.pkl", "rb"))


def predict(
    Clothing_ID,
    Age,
    Title,
    Review_Text,
    Positive_Feedback_Count,
    Division_Name,
    Department_Name,
    Class_Name,
):
    # Create input data
    input_data = pd.DataFrame(
        {
            "Clothing ID": [Clothing_ID],
            "Age": [Age],
            "Title": [Title],
            "Review Text": [Review_Text],
            "Positive Feedback Count": [Positive_Feedback_Count],
            "Division Name": [Division_Name],
            "Department Name": [Department_Name],
            "Class Name": [Class_Name],
        }
    )

    # Predict
    prediction = model.predict(input_data)

    # Return prediction
    return prediction[0]


# Create interface
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Clothing ID", minimum=0, maximum=1205),
        gr.Number(label="Age", value=40, minimum=18, maximum=99),
        gr.Textbox(label="Title"),
        gr.Textbox(label="Review Text"),
        gr.Number(label="Positive Feedback Count"),
        gr.Radio(
            label="Division Name",
            choices=["General", "General Petite"],
            value="General",
        ),
        gr.Radio(
            label="Department Name",
            choices=["Bottoms", "Dresses", "Intimate", "Jackets", "Tops", "Trend"],
            value="Dresses",
        ),
        gr.Radio(
            label="Class Name",
            choices=[
                "Dresses",
                "Knits",
                "Blouses",
                "Sweaters",
                "Pants",
                "Jeans",
                "Fine gauge",
                "Skirts",
                "Jackets",
                "Outerwear",
                "Shorts",
                "Lounge",
                "Trend",
                "Casual bottoms",
            ],
            value="Dresses",
        ),
    ],
    outputs="text",
)


if __name__ == "__main__":
    iface.launch()
