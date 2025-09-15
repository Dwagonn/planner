# Meal Planner & Grocery List Web App

## Description
A Flask web application to:
- Add meals (with ingredients)
- Plan meals for each day of the week
- Randomize meal selection
- Generate a grocery list from planned meals

## Setup Instructions

1. Create a virtual environment:  
   `python -m venv venv`

2. Activate the virtual environment:  
   - On macOS/Linux: `source venv/bin/activate`  
   - On Windows: `venv\Scripts\activate`

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Initialize the database:  
   ```bash
   python
   >>> from app import db, create_app
   >>> app = create_app()
   >>> with app.app_context(): db.create_all()
   >>> exit()

5. Run the app:
   `python run.py`