# Airport-Data-Cleaner

A web application for cleaning and standardizing airport data with a Flask backend and HTML/CSS/JS frontend.
<br>
<br />
The web app is hosted on Render. Link [Here](https://airport-data-cleaner.onrender.com)

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Local Installation

1. **Clone the repository**

```
git clone https://github.com/yourusername/airport-data-cleaner.git
cd airport-data-cleaner
```
2. **Create a virtual environment (recommended)**
```
python -m venv venv
```
3. **Activate the virtual environment**
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. **Install dependencies**
```
pip install flask pandas
```
5. **Run the application**
```
python app.py
```
6. **Access the application**
- Open your browser and navigate to: http://127.0.0.1:5000

## Web Deployment (Render)

1. **Create required files**

- Create `requirements.txt`:
  ```
  flask
  pandas
  gunicorn
  ```

- Create `render.yaml`:
  ```yaml
  services:
    - type: web
      name: airport-data-cleaner
      env: python
      buildCommand: pip install -r requirements.txt
      startCommand: gunicorn app:app
      envVars:
        - key: PYTHON_VERSION
          value: 3.9
  ```

2. **Push to GitHub**

3. **Deploy on Render**
- Create account at [render.com](https://render.com)
- Create New Web Service
- Connect your GitHub repository
- Render will automatically detect and deploy

## Usage

1. Input raw airport data in semicolon-delimited format
2. Click "Clean Data"
3. View cleaned results in a table
4. Use "Use Result as New Input" for iterative cleaning

## Data Format

Expected input format:
```
Airline Code;DelayTimes;FlightCodes;To_From
Air Canada (!);[21, 40];20015.0;WAterLoo_NEWYork
```
## Cleaning Operations

- Normalizes airline codes
- Splits origin/destination cities
- Interpolates missing flight codes
- Standardizes case formatting

## Project Structure

- `app.py` - Flask backend with cleaning logic
- `templates/index.html` - Frontend interface


