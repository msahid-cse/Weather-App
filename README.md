# Weather App

A simple weather application built using Django that fetches and displays real-time weather data based on user input.

## Features
- Search for weather information by city name.
- Fetch real-time weather data from an API.
- Display temperature, humidity, and weather conditions.
- Simple and user-friendly interface.

## Installation

### Prerequisites
- Python 3.x
- Django
- pip (Python package manager)

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/msahid-cse/Weather-App.git
   cd Weather-App-main
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```sh
   python manage.py migrate
   ```

5. Run the Django development server:
   ```sh
   python manage.py runserver
   ```

6. Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

## Configuration
- The app requires an API key from a weather data provider (e.g., OpenWeatherMap). Set up the API key in the project settings.

## License
This project is open-source and available under the MIT License.

## Contributors
- Md. Sahid
- MejbahJamanUtsha (Sahid's Secondary device)

## Screenshots

![Weather App UI] (https://github.com/msahid-cse/Weather-App/blob/main/weather%20app.png)


## Future Improvements
- Improve UI/UX.
- Add more weather details like wind speed and forecast.
- Allow users to search by ZIP code or GPS location.

