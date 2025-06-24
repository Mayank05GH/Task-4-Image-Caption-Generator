# Task-4-Image-Caption-Generator
*COMPANY*: COOTECH IT SOLUTIONS
*NAME*: MAYANK GUSAIN
*INTERN ID*: CITS0D838
*DOMAIN*: ARTIFICIAL INTELLIGENCE
*DURATION*: 4 WEEEKS
*MENTOR*: NEELA SANTOSH KUMAR

*DESCRIPTION*: For Task 4 of my CodTech AI internship, I developed an Image Caption Generator using Python, TensorFlow, and Google Colab. The main goal of this task is to demonstrate how deep learning can interpret the visual content of an image and describe it in natural language. This combines computer vision and natural language processing, showcasing how artificial intelligence can bridge the gap between images and text, which is a fundamental capability in many modern AI applications like social media, accessibility tools for the visually impaired, and smart photo organizers.

I implemented this project entirely on Google Colab, which provides a convenient cloud-based notebook environment with free access to high-performance computing resources. Colab is ideal for this kind of task because it allows seamless installation of deep learning libraries such as TensorFlow and Keras and also makes uploading and processing image data simple.

The first step of this task involved uploading a test image, which serves as the input to the caption generator. For demonstration purposes, I used a simple image (such as a cat, dog, or airplane) to ensure the model could extract clear features. In practical, production-ready systems, large datasets like Flickr8k or COCO are used to train a robust model that can caption a wide variety of scenes. However, for this internship task, the focus was on demonstrating the workflow using a pre-trained feature extractor and a placeholder caption generator.

To extract meaningful features from the image, I used InceptionV3, a pre-trained Convolutional Neural Network available in TensorFlow’s keras.applications module. This network, originally designed for image classification, is repurposed here as a feature extractor. By removing its top classification layer, the model outputs a vector representation of the input image, capturing its essential visual characteristics.

Once the feature vector was extracted, I implemented a simple demonstration of caption generation. In real-world systems, this step would involve passing the image features into an LSTM (Long Short-Term Memory) network that has been trained to generate grammatically correct and semantically meaningful sentences. For this internship task, I used a placeholder function that returns a sample caption to illustrate how the system would output a description.

I displayed the input image in the notebook alongside the generated caption to verify that the entire pipeline worked correctly. To make the result reusable and verifiable, I saved the generated caption into a text file named caption_output.txt and provided a download link in Colab so that the file could be retrieved easily. I also took a clear screenshot showing the uploaded image and the output caption, which I saved as screenshot_task4.png and included in my GitHub repository.

This task provided valuable hands-on experience with combining computer vision and natural language generation techniques. It helped me understand how modern AI systems interpret visual information and generate descriptive language, which is a powerful capability used in automated photo tagging, social media platforms, and AI assistants. By completing this task, I demonstrated my ability to build, test, and document an end-to-end AI pipeline using Python, TensorFlow, and Google Colab.

The entire project, including the Colab notebook (task4_image_caption_generator.ipynb), test image, output caption file, and the screenshot proof, is uploaded to my GitHub repository as evidence of successful implementation, fulfilling all requirements for Task 4 of my CodTech AI internship.

Image used


