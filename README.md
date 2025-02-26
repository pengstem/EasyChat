# 🚀 EasyChat

A Python-based application for interacting with Google's Gemini AI models through both text and voice interfaces.

## ✨ Features

- 💬 Text-based communication with Gemini AI models
- 🎤 Voice communication capabilities for English practice
- 🤖 Multiple Gemini model options (gemini-2.0-flash, gemini-2.0-pro-exp, gemini-2.0-flash-thinking)
- 🌐 English speaking practice with pronunciation feedback
- 📝 Customizable system instructions

## 📋 Requirements

- Python 3.10+
- Google API key (obtainable from <https://aistudio.google.com/apikey>)
- Internet connection

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/EasyChat.git

# Navigate to project directory
cd EasyChat

# Install required packages
pip install google-generativeai websockets websockets-proxy rich elevenlabs pyaudio
```

## 🚀 Usage

Run the main script:

```bash
python gemini.py
```

### Text Communication Mode

1. When prompted, enter your Google API key
2. Select option "2" for Text Communication
3. Choose your preferred Gemini model
4. Optionally provide a system instruction
5. Start chatting with the AI

### Voice Communication Mode

1. When prompted, enter your Google API key
2. Select option "1" for Voice Communication
3. Use your microphone to practice English speaking
4. Receive pronunciation feedback and corrections

## 📱 Model Options

- **gemini-2.0-flash**: Fast, efficient model suitable for everyday conversations
- **gemini-2.0-pro-exp**: Advanced model with expanded capabilities for complex tasks
- **gemini-2.0-flash-thinking**: Specialized model with "thinking out loud" capabilities

## ❓ Troubleshooting

- **API Key Issues**: Ensure your Google API key is valid and has access to Gemini models
- **Audio Problems**: Check your microphone settings and permissions
- **Connection Issues**: Verify your internet connection and proxy settings if applicable
- **Package Errors**: Make sure all dependencies are correctly installed with the right versions

## 🤝 Contributing

Contributions are welcome! If you'd like to improve EasyChat:

1. Fork the repository
2. Create a feature branch: `git checkout -b new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin new-feature`
5. Submit a pull request

## 🎯 Purpose

EasyChat is designed for those who want to use free AI models for:

- English language practice with pronunciation feedback
- General AI assistance through text conversations
- Testing different capabilities of Google's Gemini models

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
