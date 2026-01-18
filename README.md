# ACM-Teach-Database-and-SQL-Connectivity-for-a-dynamic-website

# Stranger Things Personality Quiz

A fun **Stranger Things–themed personality quiz** web application built with **Flask**, **SQLite**, and **Gemini AI**.   
Users answer 10 multiple-choice questions, and the app assigns them a **Stranger Things character** based on their responses.  

---

## Features

- 10 MCQ personality quiz questions  
- Stores quiz attempts and results in **SQLite database**  
- Uses **Gemini AI** to determine the character from answers  
- Dynamic web pages built with **Flask and Jinja2**  
- Simple, clean UI with responsive design  

---

## Demo

![Entry Page](static/image1.png) 
![Result Page](static/image2.png)

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/shreyaa1811/ACMTeachStrangerThingsPersonalityQuiz.git
cd ACMTeachStrangerThingsPersonalityQuiz
```
2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the venv**

```bash
venv\Scripts\Activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. Set up environmental variables
- Create a .env file in the directory
- In the .env file add the following line :

```python
GEMINI_API_KEY=your_gemini_api_key_here
```

## Run the application
```bash
python app.py
```
- Open your browser at http://127.0.0.1:5000

- Fill out the quiz and submit

- See which Stranger Things character matches your answers

## File Structure
StrangerThingsQuiz/
├─ app.py           # Main Flask app
├─ db.py            # SQLite database functions
├─ gemini.py        # Gemini AI integration
├─ templates/       # HTML templates
│   ├─ index.html
│   └─ result.html
├─ static/          # CSS, images, JS
├─ requirements.txt
└─ .env             # Environment variables (not in GitHub)

--- 

Notes

Make sure your Gemini API key is valid

Database file quiz_results.db is automatically created on first run

Use .gitignore to keep venv and .env out of GitHub