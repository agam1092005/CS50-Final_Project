function check_engine() {
    var engines = document.getElementsByClassName("engines");
    console.log(engines);
    for (engine in engines)
    {
        if (engines[engine].checked && engines[engine].value == "google") {
        document.getElementById("inputForm").action = "https://google.com/search";
        }
        else if (engines[engine].checked && engines[engine].value == "bing") {
            document.getElementById("inputForm").action = "https://bing.com/search";
        }
        else if (engines[engine].checked && engines[engine].value == "duckduckgo") {
            document.getElementById("inputForm").action = "https://duckduckgo.com/";
        }
    }
}

const weatherIcon = document.querySelector(".weather-icon");

function checkWeather() {
    navigator.geolocation.getCurrentPosition(async function(position) {
        let tempArray = new Array();
        let lat = position.coords.latitude.toString();
        let long = position.coords.longitude.toString();
        const url = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + long + "&appid=1bb4b3f623ac64c71bd480d754f8ef42&units=metric";
        const response = await fetch(url);
        var data = await response.json();

        document.querySelector(".city").innerHTML = data.name;
        document.querySelector(".temp").innerHTML = Math.round(data.main.temp) + "°C";
        document.querySelector(".humidity").innerHTML = data.main.humidity + " %";
        document.querySelector(".wind").innerHTML = data.wind.speed + " Km/h";

        if (data.weather[0].main == "Clouds") {
            weatherIcon.src = "images/clouds.png";
        } else if (data.weather[0].main == "Clear") {
            weatherIcon.src = "images/clear.png";
        } else if (data.weather[0].main == "Rain") {
            weatherIcon.src = "images/rain.png";
        } else if (data.weather[0].main == "Drizzle") {
            weatherIcon.src = "images/drizzle.png";
        } else if (data.weather[0].main == "Mist") {
            weatherIcon.src = "images/mist.png";
        } else if (data.weather[0].main == "Snow") {
            weatherIcon.src = "images/snow.png";
        }

        document.querySelector(".weather").style.display = "block";
    })
}

checkWeather();
