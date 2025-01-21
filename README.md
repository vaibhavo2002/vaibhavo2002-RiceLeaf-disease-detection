
# Rice Leaf Disease Detection

## Introduction

Rice plants are highly susceptible to various bacterial, viral, and fungal diseases, which significantly impact global rice production. Early detection of these diseases is critical to ensuring the healthy growth of rice plants, safeguarding food security, and supporting farmers worldwide. This project focuses on detecting infections in rice leaves using a machine learning-based approach.

## Dataset Summary

The dataset contains 120 images of rice leaves classified into three disease categories:
- **Leaf Smut**
- **Brown Spot**
- **Bacterial Leaf Blight**

Each category has 40 images. The dataset is divided into training, validation, and testing subsets for model development and evaluation.

## Project Workflow

The project consists of the following steps:

1. **Importing Libraries**: Loading necessary Python libraries for data processing and model building.
2. **Data Loading**: Dividing the dataset into training, testing, and validation subsets using the `split-folders` library.
3. **Data Preparation**: 
   - Generating batches for efficient memory usage.
   - Preprocessing images through resizing, normalization, and augmentation.
4. **Model Building**: 
   - Developing a Convolutional Neural Network (CNN) architecture with convolutional, pooling, and fully connected layers.
   - Compiling the model and visualizing its structure.
   - Training the model with the prepared dataset.
5. **Model Evaluation**: Assessing the model's performance using accuracy and loss metrics.
   - Validation Accuracy: 91.67%
   - Overall Accuracy: 84.38%
6. **Model Testing**: Creating a function to test multiple images from the test dataset.
7. **Saving the Model**: Exporting the trained model for future use.

## Results

- **Training and Validation Accuracy**: Graphical visualization of training and validation accuracy.
- **Training and Validation Loss**: Analysis of training and validation loss.
- **Final Metrics**: 
  - Loss: 0.53
  - Accuracy: 91.66%

## Tools and Technologies

- **Programming Language**: Python
- **Libraries**: TensorFlow/Keras, NumPy, Matplotlib, Seaborn
- **Techniques**: Image Augmentation, CNN Architecture
