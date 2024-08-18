# PathfinderAI

**PathfinderAI** is a web application that generates a comprehensive learning roadmap for any topic from beginner to advanced levels. The roadmap includes suggested blog articles and YouTube videos, structured in clear stages (Beginner, Intermediate, Advanced). The application is built using Streamlit and leverages Google's generative AI to create the roadmap. Additionally, users can download the roadmap as a PDF.

This project was developed as part of the **Global AI Fest and Future Hackathon** competition. The problem statement for the hackathon was to **"Create a Useful Bot."** PathfinderAI addresses this by offering an AI-powered bot that helps users generate tailored learning paths, making education more accessible and organized.

## Features

- **Interactive Web Interface:** Enter a topic and get a detailed learning roadmap instantly.
- **AI-Powered Content Generation:** Utilizes Google's generative AI to create custom roadmaps.
- **PDF Download:** Allows users to download the generated roadmap as a PDF for offline use.

## Installation

### Prerequisites

- Python 3.8 or higher
- Streamlit
- FPDF
- Python-dotenv

### Steps

1. **Clone this repository:**

    ```bash
    git clone https://github.com/imsuryya/PathfinderAI.git
    cd PathfinderAI
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables:**

    - Rename the `.env.example` file to `.env`.
    - Open the `.env` file and replace `YOUR_API_KEY` with your actual Google Generative AI API key:

      ```env
      api_key=your_actual_api_key_here
      ```

4. **Run the application:**

    ```bash
    streamlit run main.py
    ```

## Usage

- Open the application in your browser (it will usually run at `http://localhost:8501`).
- Enter the topic you want to learn about in the input field.
- The app will generate a learning roadmap with resources organized by level.
- You can download the roadmap as a PDF by clicking the "Download Roadmap as PDF" button.

## Dependencies

- Streamlit
- FPDF
- Python-dotenv
- Google Gemini AI

## Contributors

<div style="display: flex; gap: 10px;">
    <a href="https://github.com/imsuryya">
        <img src="https://github.com/imsuryya.png" alt="Suryya" style="width: 50px; height: 50px; border-radius: 50%;"/>
    </a>
    <a href="https://github.com/Venuchander">
        <img src="https://github.com/Venuchander.png" alt="Venuchander" style="width: 50px; height: 50px; border-radius: 50%;"/>
    </a>
</div>
