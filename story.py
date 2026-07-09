import gradio as gr
import requests
import os
FastAPI_URL = "http://localhost:8000/story"
def story(prompt):
    response = requests.post(FastAPI_URL, json={"prompt": prompt})
    if response.status_code == 200:
        return response.json()["answer"]
    else:
        return "Error connecting FastAPI."
demo = gr.Interface(fn=story, inputs=gr.Textbox(label="enter prompt"), outputs=gr.Textbox(label="answer here",lines=20))

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )

