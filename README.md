# 🛡️ Manipulense – Conversation Manipulation & Influence Detector  

> **“Exposing hidden persuasion tactics in your everyday chats.”**

## 🚀 Repo Stats  

![Stars](https://img.shields.io/github/stars/ErrVoid/Manipulense?style=social)  
![Forks](https://img.shields.io/github/forks/ErrVoid/Manipulense?style=social)  
![Issues](https://img.shields.io/github/issues/ErrVoid/Manipulense)  
![Pull Requests](https://img.shields.io/github/issues-pr/ErrVoid/Manipulense)  
![Last Commit](https://img.shields.io/github/last-commit/ErrVoid/Manipulense)  

<p align="center">
  <img src="https://img.shields.io/badge/Made%20With-%F0%9F%90%8D%20Python-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Frontend-Flutter-blue?style=for-the-badge&logo=flutter" />
  <img src="https://img.shields.io/badge/AI-HuggingFace-orange?style=for-the-badge&logo=huggingface" />
</p>

---


## 🪄 Easter Egg for Hackathon Judges  

👉 Did you know?  
Every time you refresh this repo, you’re resisting manipulation 😉  

<p align="center">
  <img src="https://media.giphy.com/media/26tPplGWjN0xLybiU/giphy.gif" width="300" alt="fun gif"/>
</p>
---

## 🌍 Problem We’re Solving  
In daily chats (WhatsApp, Messenger, Discord…), people often **get influenced or manipulated** without realizing it.  
- Saying “yes” under peer pressure.  
- Agreeing because of guilt-tripping or flattery.  
- Being persuaded through fear or authority pressure.  
- Falling victim to gaslighting in toxic conversations.  

There is **no tool** today that can read a conversation and explain:  
- *Why did this person agree?*  
- *What tactics were used to influence them?*  
- *Was the response genuine, or was it forced/manipulated?*  

---

## ✨ Our Solution: Manipulense  
Manipulense is an **AI-powered conversation analyzer** that detects manipulation tactics in chats and explains them in **human language**.  

💬 Upload a chat log → ConvGuard highlights manipulative lines and shows you **why** they were manipulative.  

📊 Visualize influence → See how pressure built up across the conversation.  

🔎 Learn tactics → Understand guilt-tripping, flattery, fear, and gaslighting as they happen in text.  

---

## 🎯 Key Features  

- 📑 **Upload Chats** – Import WhatsApp exports or paste raw text.  
- 🧠 **AI-Powered Detection** – Uses Hugging Face pipelines to detect emotions + manipulation tactics.  
- 🔎 **Explainable Insights** – Every manipulative line comes with an explanation.   
- 🎨 **Modern Flutter UI** – Dark theme, micro-animations, chat bubbles, and interactive highlights.  
- ⚡ **Fast Python Backend** – Built with FastAPI + Hugging Face for NLP.  

---

## 🛠 Tech Stack  

| Layer        | Tech Used |
|--------------|-----------|
| **Frontend** | Flutter (Dart) – beautiful modern UI with animations |
| **Backend**  | Python (FastAPI) – NLP processing |
| **AI Models**| Hugging Face Transformers (emotion + intent + persuasion detection) |

---

## 🚀 Impact  

- 🛡 **Safety & Awareness** – Teens, women, and vulnerable groups can detect manipulation in relationships.  
- 🤝 **Negotiation Training** – Learn persuasion dynamics in business or sales chats.  
- 🧠 **Mental Health** – Identify toxic conversational patterns early.  
- 🎓 **Education** – A tool for teaching psychology, persuasion, and communication skills.  

Manipulense is not just a project — it’s a step toward **transparent, safer communication in the digital world**.  

---

## 📸 App Screenshots (UI Preview)  

<p align="center">
  <img src="https://via.placeholder.com/300x600.png?text=Home+Screen" width="200"/>
  <img src="https://via.placeholder.com/300x600.png?text=Chat+Analysis" width="200"/>
  <img src="https://via.placeholder.com/300x600.png?text=Influence+Graph" width="200"/>
</p>

---

## 🧩 How It Works  

1. **Input** → Upload a chat log (WhatsApp export or pasted text).  
2. **Preprocessing** → Split into speaker turns.  
3. **NLP Analysis** →  
   - Emotion detection  
   - Manipulation tactic classification (guilt, flattery, fear, gaslighting…)  
4. **Influence Mapping** → Detect when a person changes stance (No → Yes).  
5. **Output** →  
   - Highlighted chat bubbles (red = manipulative, green = neutral).  
   - Explanations for each manipulative line.  

---

## ⚙️ Installation & Setup  

### Frontend (Flutter)  
```bash
git clone https://github.com/ErrVoid/Manipulense/
cd Manipulense/flutter_app
flutter pub get
flutter run
