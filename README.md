    
# 🔐 TLS Handshake Simulator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Status](https://img.shields.io/badge/Status-Active-success)

An interactive, visual educational tool built with **Python** and **Streamlit** to demonstrate how the **TLS 1.3 Handshake** protocol works. This project breaks down the complex cryptographic "dance" between a Client (Browser) and a Server into clear, understandable steps.

## 📸 Screenshot
![Project Screenshot](screenshot.png)
*(Note: Add your screenshot file to the project folder and name it screenshot.png)*

## 🚀 Features

*   **Step-by-Step Simulation:** Watch the handshake happen in real-time, pausing at every stage (Client Hello, Server Hello, Key Exchange).
*   **Packet Inspection:** View the actual JSON data structures being sent (Session IDs, Cipher Suites, Nonces).
*   **Cryptographic Simulation:** Generates real random hex values and simulates Public/Private key generation using Python's `cryptography` library.
*   **Secure Chat Demo:** Once the connection is established, type messages to see how they look in "Plain Text" vs "Encrypted Network Traffic."
*   **Modern UI:** Clean, dark-themed interface using Streamlit.

## 🛠️ Project Structure

```text
tls_handshake_sim/
│
├── logic/
│   ├── client.py          # Simulates Browser behavior
│   ├── server.py          # Simulates Website behavior
│   └── utils.py           # Cryptographic helper functions
│
├── main.py                # The Frontend UI (Streamlit)
├── requirements.txt       # Dependencies
└── README.md              # Documentation

  

⚙️ Installation & Setup

Follow these steps to run the simulator on your local machine.
1. Clone the Repository
code Bash

    
git clone https://github.com/YOUR_USERNAME/tls-handshake-simulator.git
cd tls-handshake-simulator

  

2. Create a Virtual Environment (Recommended)
code Bash

    
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

  

3. Install Dependencies
code Bash

    
pip install -r requirements.txt

  

4. Run the Application
code Bash

    
streamlit run main.py

  

The app will automatically open in your web browser at http://localhost:8501.
🧠 How It Works ( The Logic )

This simulator mimics the TLS 1.3 flow:

    Client Hello: The browser generates a random number (Nonce) and sends supported Cipher Suites.

    Server Hello: The server picks a Cipher Suite, sends its own random number, and provides its Digital Certificate.

    Key Exchange: The client verifies the certificate and generates a Pre-Master Secret (session key).

    Secure Connection: Both sides verify keys. The UI unlocks a "Chat Box" where data is visually encrypted before being "sent."

📦 Tech Stack

    Python: Core logic.

    Streamlit: Web interface and state management.

    Cryptography: Library used to generate fake keys and certs.

🤝 Contributing

    Fork the project.

    Create your feature branch (git checkout -b feature/AmazingFeature).

    Commit your changes (git commit -m 'Add some AmazingFeature').

    Push to the branch (git push origin feature/AmazingFeature).

    Open a Pull Request.

📝 License

Distributed under the MIT License. See LICENSE for more information.

Built with ❤️ by [Your Name]
code Code

    
---

### 💡 Pro Tip for the Screenshot
Since you already have a great screenshot:
1.  Rename that image file to `screenshot.png`.
2.  Move it into your **root** folder (next to `main.py` and `README.md`).
3.  When you push your code to GitHub (`git add .`, `git commit`, `git push`), the image will automatically appear on your main GitHub page because of the line `![Project Screenshot](screenshot.png)` in the code above.

  
