import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os
# import importlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Yolo = importlib.import_module("ultralytics.models.yolo.model").Yolo

model = YOLO("best.pt")

label_map = {
    0: "scissors",
    1: "unidentified",
    2: "knife",
    3: "cutter",
    4: "swiss knife",
}

def app():
    # st.title("AI SEE YOU")
    
    st.title("AI SEE YOU")
    st.title('🔍 Waste Classification Prediction')

    # Example images
    example_images = ['test1.jpg', 'test2.jpg', 'test3.jpg', 'test4.jpg', 'test5.jpg', 'test6.jpg', 'test7.jpg','test8.jpg']
    example_path = './visualization'  # Set the path

    st.subheader("Choose an example image or upload your own:")

    # Initialize session state for the selected image
    if 'selected_image' not in st.session_state:
        st.session_state.selected_image = None

    # Create columns for example images
    cols = st.columns(4)
    for i, img_name in enumerate(example_images):
        with cols[i % 4]:
            img_path = os.path.join(example_path, img_name)
            
            # Display the preview image under the button
            st.image(img_path, width=100, caption=f'Example {i+1}')
            
            # Create the button for each example
            if st.button(f"Example {i+1}", key=f"example_{i}"):
                st.session_state.selected_image = img_path

    
            


# Predict berdasarkan uploaded image
    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if file is not None:
        img = Image.open(file).convert("RGB")
        st.image(img, caption="Uploaded Image")
        
        results = model.predict(source=img, conf=0.25, save=False)
        
        if results:
            st.write("Results:")
            for result in results:
                if result.boxes.cls.numel() > 0:

                    fig, ax = plt.subplots()
                    ax.imshow(img)

                    x1, y1, x2, y2 = result.boxes.xyxy[0]
                    rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=1, edgecolor="r", facecolor="none")
                    ax.add_patch(rect)

                    ax.text(x1, y1, f"{label_map[int(result.boxes.cls[0])]} {result.boxes.conf[0]:.2f}", fontsize=12, color="white", bbox=dict(facecolor="red", alpha=0.5))
                    ax.axis("off")

                    st.pyplot(fig)
                else:
                    st.write("No objects detected.")
    
    # Predict Berdasarkan example image
    image = None
    if st.session_state.selected_image is not None:
        if isinstance(st.session_state.selected_image, str):  # Example image case
            image = Image.open(st.session_state.selected_image).convert('RGB')
        else:  # Uploaded image case
            image = Image.open(st.session_state.selected_image).convert('RGB')

    if image:
        # Create two columns for images
        col1, col2 = st.columns(2)

        # Display original image in the left column
        with col1:
            st.subheader("Selected Image")
            st.image(image, caption='Selected Image')

    if image:
        img = image
        results = model.predict(source=img, conf=0.25, save=False)
        
        if results:
            st.write("Results:")
            for result in results:
                if result.boxes.cls.numel() > 0:

                    fig, ax = plt.subplots()
                    ax.imshow(img)

                    x1, y1, x2, y2 = result.boxes.xyxy[0]
                    rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=1, edgecolor="r", facecolor="none")
                    ax.add_patch(rect)

                    ax.text(x1, y1, f"{label_map[int(result.boxes.cls[0])]} {result.boxes.conf[0]:.2f}", fontsize=12, color="white", bbox=dict(facecolor="red", alpha=0.5))
                    ax.axis("off")

                    st.pyplot(fig)
                else:
                    st.write("No objects detected.")

if __name__ == "__main__":
    app()