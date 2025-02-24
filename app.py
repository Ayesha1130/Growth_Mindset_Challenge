import streamlit as st
import altair as alt
import pandas as pd
import requests



# Get API key from environment variables
api_key = st.secrets["OPENWEATHERMAP_API_KEY"]["value"]



# Function to display Home page
def display_home():
    st.balloons()
    st.title(" 🌱 Growth Mindset Challenge")
    st.image("assets/homepic.jpg")
    st.subheader(" ✨ This app is designed to help you explore the world around you.")
    st.write(" ✨ I'm here to provide you with insights and recommendations based on your interests. ✨ ")
    st.text(" ⬅️ Select an option from the sidebar to get started.")
    st.subheader("Created by ❤️ Ayesha Iqbal")

# Function to display Learn programming page
def display_learn_programming():
    st.balloons()
    st.title(" ✅ Explore Modern Web Technologies")
    st.image("assets/today.png")
    button1 = st.button("HTML 🧑🏻‍💻")
    button2 = st.button("CSS 🧑🏻‍💻")
    button3 = st.button("JavaScript 🧑🏻‍💻")
    button4 = st.button("Typescript 🧑🏻‍💻")
    button5 = st.button("Next.js 🧑🏻‍💻")
    button6 = st.button("React.js 🧑🏻‍💻")
    button7 = st.button("Python 🧑🏻‍💻")

    if button1:
        st.markdown("**Click here to Learn**: [HTML Resources](https://www.w3schools.com/html/default.asp)")
    if button2:
        st.markdown("**Click here to Learn**: [CSS Resources](https://www.w3schools.com/css/default.asp)")
    if button3:
        st.markdown("**Click here to Learn**: [JavaScript Resources](https://www.w3schools.com/js/default.asp)")
    if button4:
        st.markdown("**Click here to Learn**: [TypeScript Resources](https://www.w3schools.com/typescript/index.php)")
    if button5:
        st.markdown("**Click here to Learn**: [Next.js Resources](https://nextjs.org/docs)")
    if button6:
        st.markdown("**Click here to Learn**: [React.js Resources](https://www.w3schools.com/react/default.asp)")
    if button7:
        st.markdown("**Click here to Learn**: [Python Resources](https://www.w3schools.com/html/default.asp)")

# Function to display Dawn Newspaper page
def display_dawn_newspaper():
    st.balloons()
    st.title(" 🌟 Discover the latest trends in Dawn newspaper 📰")
    st.image("assets/paper.jpg")
    newspaper = st.button("Discover Dawn's latest news")
    if newspaper:
        st.markdown("**Click here to Learn**: [Dawn's latest news](https://www.dawn.com/news)")

# Function to display Weather page
def display_weather():
    st.balloons()
    st.header(" ☁️  Weather Forecast   ")
    st.image("assets/weather.jpg")
    city = st.text_input("Enter your city")  # Define 'city' here for the weather section

    if city:
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(base_url)
        data = response.json()

        # Error handling for weather data
        if data["cod"] != 200:
            st.error(f"City not found. Please enter a valid city name. {data.get('message', '')}")
        else:
            main_data = data["main"]
            weather_data = data["weather"][0]

            st.write(f"Temperature: {main_data['temp']}°C")
            st.write(f"Humidity: {main_data['humidity']}%")
            st.write(f"Weather: {weather_data['description']}")

            # Conditional images based on weather description
            if "clear" in weather_data["description"]:
                st.image("assets/sunny.jpg", width=300)
                st.balloons()
                st.write("It's a Sunny day! 🌞")
            elif "rain" in weather_data["description"]:
                st.image("assets/rainy.jpg", width=300)
                st.balloons()
                st.write("It's raining! 🌧️")
            elif "snow" in weather_data["description"]:
                st.image("assets/snowy.jpg", width=300)
                st.balloons()
                st.write("It's snowing! ❄️")
            elif "cloud" in weather_data["description"]:
                st.image("assets/cloudy.webp", width=300)
                st.balloons()
                st.write("It's cloudy! ☁️")

            # Displaying the chart only on the Weather page
            data = pd.DataFrame({
                'Month': ['January', 'February', 'March', 'April', 'May'],
                'Temperature': [5, 8, 15, 20, 25]
            })

            chart = alt.Chart(data).mark_bar().encode(
                x='Month',
                y='Temperature',
                color='Month'
            )

            # Streamlit Chart
            st.altair_chart(chart, use_container_width=True)

# Custom CSS to style buttons and body background color
st.markdown("""
    <style>
    body {
        background-color: #121212;  /* Dark background for the body */
        color: #e0e0e0;  /* Light text color for readability */
    }

    .stButton > button {
        background-color: #4CAF50;  /* Green background */
        color: white;               /* White text */
        border: 2px solid black;  /* Green border */
        border-radius: 10px;        /* Rounded corners */
        padding: 32px 32px;         /* Button padding */
        width: 90%;               /* Full width */
        height: auto;              /* Full height, auto if no content */
        margin: 16px;              /* Some top and bottom margin */
        display: flex;              /* Flexible container */
        justify-content: center;     /* Center-align items */
        align-items: center;         /* Center-align items */
        font-weight: bold;          /* Bold text */
        text-decoration: none;       /* No underline */
        text-transform: uppercase;   /* Uppercase text */
        overflow: hidden;            /* Hide overflow */
        transition: 0.3s;           /* Add transition effect on hover */
        text-align: center;         /* Text alignment */
        font-size: 18px;            /* Font size adjusted for mobile */
        cursor: pointer;           /* Pointer cursor on hover */
        transition: background-color 0.3s, transform 0.2s;
    }

    .stButton > button:hover {
        background-color: #45a049;  /* Darker green on hover */
        transform: scale(1.1);       /* Slightly increase size on hover */
    }

    /* Responsive design for mobile */
    @media (max-width: 768px) {
        .stButton > button {
            font-size: 18px;  /* Font size for mobile */
            padding: 10px 20px; /* Adjust padding for mobile */
            width: 100%; /* Button full width */
        }

        img {
            width: 80%; /* Reduce image size for mobile */
            height: auto;
        }

        body {
            font-size: 14px; /* Smaller font for better readability */
        }
    }
    </style>
""", unsafe_allow_html=True)


# Sidebar
st.sidebar.title("What do you want to explore today 🤔")
st.sidebar.image("assets/sidebar1.jpg", width=200)

option = st.sidebar.radio("What do you want to explore Today",["Home", "Learn programming", "Dawn newspaper", "Check Weather"])

if option == "Home":
    display_home()
elif option == "Learn programming":
    display_learn_programming()
elif option == "Dawn newspaper":
    display_dawn_newspaper()
elif option == "Check Weather":
    display_weather()
