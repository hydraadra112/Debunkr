<p align="center">
  <table>
    <tr>
      <td align="right">
        <img src="frontend/static/debunkrlogo.png" alt="Debunkr Logo" width="100"/>
      </td>
      <td align="left">
        <h1><strong>DEBUNKR</strong></h1>
      </td>
    </tr>
  </table>
</p>

<p align="center">
  <em>A Filipino fake news classifier built with Python, and SvelteKit — powered by LIME for interpretability.</em>
</p>

## 🎯 Purpose

**DEBUNKR** addresses the urgent problem of fake news in the Philippines, especially in the lead-up to the May 2025 midterm elections. A Pulse Asia survey reports that 86% of Filipinos view fake news as a major issue, with 90% encountering political misinformation—primarily via social media and TV. Compounding the problem, 65% find it difficult to distinguish truth from falsehood, and 55% report frequent exposure to disinformation. The rise of AI-generated content (e.g., deepfakes) further complicates the landscape.

To combat this, we developed a Tagalog fake news classifier to empower users with a tool that helps verify information and improve digital literacy. The backend leverages Python and multiple NLP libraries for model training, while the frontend is built using SvelteKit and TailwindCSS for optimized, scalable, and modular UI development.

---


## 🧠 Overview

**DEBUNKR** is a fake news detection web application focused on Filipino news content. It utilizes:
- Filipino/Tagalog [dataset](https://huggingface.co/datasets/jcblaise/fake_news_filipino) to train the models
- A modern SvelteKit frontend
- [LIME (Local Interpretable Model-Agnostic Explanations)](https://github.com/marcotcr/lime) for transparency and model interpretability
- [Trafilatura](https://github.com/adbar/trafilatura) for web-scraping of suspicious news content

This is a final project for our **CCS 249 - Natural Language Processing** course.

---

## ⚙️ Setup Instructions

To set up the project locally, follow the instructions below for both the frontend and backend components:

### 🔧 Setup

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Run the dev server
npm run dev -- --open

# Open a new terminal

# Navigate to the backend directory
cd backend

# Install required Python packages (Setup venv first)
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload --port 8000
```

<div align="center">

## 👥 Creators
[John Manuel Carado](https://github.com/hydraadra112)  
[Cherilyn Marie Deocampo](https://github.com/chiichann)  
[Mark Andrei Encanto](https://github.com/Markndrei)  
[Chariz Dianne Falco](https://github.com/chariz1101)  
[Jephone Israel Jireh S. Torre](https://github.com/JephoneTorre)  
</div>

