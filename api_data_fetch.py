import requests
import json

API_URL = "https://randomuser.me/api/"

def fetch_user_data():
    try:
        response = requests.get(API_URL, timeout=10)

        # Check HTTP status code
        if response.status_code == 200:
            data = response.json()

            # Extract required fields from nested JSON
            user = data["results"][0]
            name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
            email = user["email"]
            country = user["location"]["country"]

            print("✅ User Data Fetched Successfully\n")
            print(f"Name    : {name}")
            print(f"Email   : {email}")
            print(f"Country : {country}")

            # Save full JSON response to file
            with open("user_data.json", "w") as file:
                json.dump(data, file, indent=4)

            print("\n📁 Data saved to user_data.json")

        else:
            print(f"❌ Failed to fetch data. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("⚠️ API Request Failed")
        print("Error:", e)

if __name__ == "__main__":
    fetch_user_data()
