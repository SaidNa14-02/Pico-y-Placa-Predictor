# Pico y Placa Predictor

A Flask web application to check vehicle circulation restrictions in Quito, Ecuador.

## Installation

### 1. Create Virtual Environment

For Windows:
```powershell
# Navigate to project directory
cd c:\Users\usuario\Desktop\Stackb\Pico-y-Placa-Predictor

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate
```

For macOS/Linux:
```bash
# Navigate to project directory
cd path/to/Pico-y-Placa-Predictor

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

The command prompt should now show `(.venv)` indicating the virtual environment is active.

### 2. Install Requirements

With the virtual environment activated, install the required packages:

```powershell
# Install required packages
pip install -r requirements.txt
```

This will install:
- Flask
- Flask-WTF
- Python-dotenv
- WTForms

### 3. Run the Application

First, verify you're in the correct directory and the virtual environment is active:

```powershell
# Check directory
cd c:\Users\usuario\Desktop\Stackb\Pico-y-Placa-Predictor\Picoyplaca

# Verify virtual environment is active - should see in your terminal (.venv)
```

# Set Flask variables
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
$env:FLASK_DEBUG = "1"

# Run Flask application
python -m flask run

### 4. Project Structure and Functionality

This project implements the Pico y Placa traffic restriction system using 4 main classes:

#### Vehicle Class
- Handles license plate validation
- Validates format (ABC-1234)
- Manages plate data storage
- Performs data type checking

#### Schedule Class
- Manages date and time validation
- Handles date format (YYYY-MM-DD)
- Validates time format (HH:MM)
- Provides date/time utility methods

#### Day Restriction Class
- Implements day-based restrictions
- Maps days to restricted plate numbers
- Handles weekend exceptions
- Schedule integration for date validation

#### Time Restriction Class
- Manages time-based restrictions
- Implements restriction windows:
  - Morning: 07:00 - 09:30
  - Afternoon: 16:00 - 19:30
- Validates time inputs

### 5. Usage Example

```text
Input:
- Plate: ABC-1234
- Date: 2024-05-10
- Time: 08:30

Output:
- "You can not drive at this time" (if restricted)
- "You can drive with no problem" (if allowed)
```

### 6. Restriction Rules

- Monday: Plates ending in 1 and 2
- Tuesday: Plates ending in 3 and 4
- Wednesday: Plates ending in 5 and 6
- Thursday: Plates ending in 7 and 8
- Friday: Plates ending in 9 and 0
- Weekend: No restrictions

### 7. GUI
 
- HTML5 for structure
- CSS3 for styling
- Flask-WTF for form handling
- Jinja2 for template rendering

### 8. Screenshots
![Pico y Placa Interface](/image.png)