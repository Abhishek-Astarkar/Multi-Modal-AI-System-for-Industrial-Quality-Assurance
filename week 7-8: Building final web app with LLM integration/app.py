import streamlit as st
from PIL import Image
from ultralytics import YOLO
import ollama
from datetime import date

st.title("Web app for Steel sheets inspection")
st.subheader("Upload the steel image here")

model = YOLO("data/best.pt")

def generate_report(results):
    boxes = results[0].boxes
    class_names = results[0].names

    detections = []
    for box in boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        detections.append((class_names[cls_id], conf))

    if not detections:
        return "No defects detected. Surface appears clean."

    defect_lines = "\n".join([f"- {name} (confidence: {conf:.0%})" for name, conf in detections])
    today = date.today().strftime("%d %B %Y")

    prompt = f"""You are an industrial quality inspector generating a steel surface inspection report.

Detected defects:
{defect_lines}

Generate a report in EXACTLY this format:

Inspection Date: {today}
Detected Defects:
(list each defect with its confidence as a bullet point)
Summary: (2-3 sentences describing the overall condition)
Severity: (Low, Medium, or High based on defect types/count)
Recommended Action:
(3-4 bullet points of specific recommended actions)
"""

    response = ollama.chat(
        model='llama3.2',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['message']['content']


uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    results = model([image])
    annotated_image = results[0].plot()
    st.image(annotated_image, caption="Detected Defects")

    if st.button("Generate Inspection Report"):
        with st.spinner("Generating report..."):
            report = generate_report(results)
        st.subheader("Inspection Report")
        st.text(report)