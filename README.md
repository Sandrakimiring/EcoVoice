
# EcoVoice - Sustainable Living Assistant

EcoVoice is a sustainable living assistant that empowers users to make eco-friendly choices by providing personalized tips through a modern chat interface. Leveraging Azure AI services and GitHub Copilot, it supports text, voice, and image inputs to promote a greener lifestyle.

## Inspiration

The idea for EcoVoice was born from a passion to combat climate change and make sustainability approachable. Inspired by the Azure AI Developer Hackathon, I aimed to harness AI to simplify eco-conscious decisions, turning everyday queries into actionable advice.

## What It Does

EcoVoice engages users via a chat-style UI, accepting text questions, voice commands, and image uploads. It responds with tailored sustainability tips—like recycling advice or repurposing ideas—using Azure’s Speech-to-Text, Computer Vision, and OpenAI services.

## How I Built It

- **Frontend:** A sleek, green-themed chat interface built with HTML, CSS, and JavaScript, featuring smooth animations and inputs for text, voice, and images.
- **Backend:** Azure Functions in Python handle core logic, integrating Azure Speech-to-Text for voice processing, with plans to add Computer Vision and OpenAI for image analysis and responses.
- **Tools:** GitHub Copilot accelerated coding by suggesting snippets, while Azure App Service is set for deployment. Environment variables secure API keys.

## Challenges I Ran Into

Integrating Azure Functions with the frontend was tricky—local testing required debugging dependency issues. Building a responsive UI without frameworks demanded precise CSS tweaks, and time constraints limited full AI integration, though mock responses kept progress on track.

## Accomplishments I am  Proud Of

We’re thrilled to have created a functional, user-friendly assistant that blends voice and text inputs seamlessly. Overcoming technical hurdles to leverage Azure AI and Copilot, while designing an intuitive green UI, feels like a big win for both tech and sustainability.

## What I Learned

This project deepened my understanding of Azure’s AI suite, asynchronous JavaScript, and pure front-end design. I learned how Copilot boosts productivity and gained insights into sustainable living, reinforcing the impact of tech on real-world problems.

## What’s Next for EcoVoice

- **Full AI Integration:** Connect Computer Vision and OpenAI for image processing and smarter responses.
- **Feature Expansion:** Add eco-action tracking and gamification with points.
- **Deployment:** Host on Azure App Service for scalability.
- **Mobile Access:** Explore a mobile-friendly version.
- **Community:** Foster a user community to share eco-tips.

EcoVoice aspires to be a go-to tool for sustainable living, making green choices simple and impactful.

## Built With

- **Frontend:** The user interface is created with HTML, CSS, and JavaScript. It includes a chat interface where users can type their questions or use the microphone button to speak.
- **Backend:** The backend consists of two main components:
  - **Flask API:** Handles text-based interactions. It receives user messages, processes them using OpenAI's GPT-4, and returns the responses.
  - **FastAPI:** Manages speech-to-text conversion using Azure Cognitive Services. It processes audio files uploaded by users and returns the transcribed text.
- **Environment Variables:** Sensitive information such as API keys is stored securely using environment variables.


## Getting Started

### Prerequisites

- Python 3.9+
- Azure Functions Core Tools (`npm install -g azure-functions-core-tools@4`)
- Git

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Sandrakimiring/EcoVoice
   cd EcoVoice
   ```

2. **Set Up the Backend:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   Create a `.env` file in the root directory:
   ```bash
   SPEECH_KEY=your_azure_speech_key
   SPEECH_REGION=your_azure_speech_region
   ```

4. **Run Locally:**
   - Start Azure Functions:
     ```bash
     func start
     ```
   - Open `index.html` in a browser to use the UI.

## Contributing

Contributions are welcome! Fork the repo and submit pull requests with enhancements or fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Gratitude to Microsoft Azure for powerful AI services.
- Shoutout to GitHub Copilot for coding support.

---


