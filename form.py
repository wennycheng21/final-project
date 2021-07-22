import random 

print("Welcome to Homeless Resources! Please fill the form below to find a nearby shelters and inns.")

state_id = ""
user_state = input("What state do you live in? ")
user_age = input("What is your current age? ")
user_gender = input("What is your gender? (Female, Male, or N/A) ")
user_assistance = input(
    "What is the assistance you will need? (Food, Shelter, Hygiene, Job Assistance, Transportation) ")
id_number = random.randrange(1000, 9999)

state = {
    "new york": "NY",
    "alabama": "AL",
    "alaska": "AK",
    "arizona": "AZ",
    "arkansas": "AR",
    "california": "CA",
    "colorado": "CO",
    "connecticut": "CT",
    "delaware": "DE",
    "florida": "FL",
    "georgia": "GA",
    "hawaii": "HI",
    "idaho": "ID",
    "illinois": "IL",
    "indiana": "IN",
    "iowa": "IA",
    "kansas": "KS",
    "kentucky": "KY",
    "louisiana": "LA",
    "maine": "ME",
    "maryland": "MD",
    "massachusetts": "MA",
    "michigan": "MI",
    "minnesota": "MN",
    "mississippi": "MS",
    "missouri": "MO",
    "montana": "MT",
    "nebraska": "NE",
    "nevada": "NV",
    "new hampshire": "NH",
    "new jersey": "NJ",
    "new mexico": "NM",
    "north carolina": "NC",
    "north dakota": "ND",
    "ohio": "OH",
    "oklahoma": "OK",
    "oregon": "OR",
    "pennsylvania": "PA",
    "rhode island": "RI",
    "south carolina": "SC",
    "south dakota": "SD",
    "tennessee": "TN",
    "texas": "TX",
    "utah": "UT",
    "vermont": "VT",
    "virginia": "VA",
    "washington": "WA",
    "west virginia": "WV",
    "wisconsin": "WI",
    "wyoming": "WY"
}


print("Thank you for filling the form! Here's the info we received: State: " + user_state + ", Age: " + str(user_age) +
      ", Gender: " + user_gender + ", Assistance: " + user_assistance + ". Your assigned ID will be " + state[user_state.lower()] + str(id_number)) 
