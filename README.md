# 🚘 License Plate Recognition using OpenCV and Tesseract OCR

This project detects and reads a vehicle's license plate from an image using **OpenCV** for image processing and **Tesseract OCR** for character recognition.

---

## 📸 Project Overview

The code performs the following steps:

1. Loads and displays the input image.
2. Converts it to grayscale for easier processing.
3. Applies **Canny Edge Detection** to highlight edges.
4. Finds and sorts contours to locate the license plate region.
5. Crops and filters the license plate region.
6. Uses **Tesseract OCR** to extract text from the cropped plate.
7. Displays the result with the recognized number and bounding box.

---

## 🧰 Technologies Used

- **Python**
- **OpenCV**
- **Tesseract OCR**
- **NumPy**

---

## 🛠️ Setup Instructions

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/your-username/license-plate-recognition.git
cd license-plate-recognition
