import random

print("Welcome to Homeless Resources! Please fill the form below to find a nearby shelters and inns.")

# this code asks for user inputs of the questions the forms asks them
state_id = ""
user_state = input("What state do you live in? ")
user_age = int(input("What is your current age? "))
user_gender = input("What is your gender? (Female, Male, or N/A) ")
user_assistance = input(
    "What is the assistance you will need? (Food, Shelter, Hygiene, Job Assistance, Transportation) ")

user_agerange = ""
# this code generates a random 4 digit number in the range of 1000 and 9999
id_number = random.randrange(1000, 9999)


# this code is a dictionary that creates the first two letters of their assigned ID using their state when they fill the form
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

# creating age ranges based on the user's age
if(0 <= user_age <= 14):
    user_agerange = "children"
elif(15 <= user_age <= 24):
    user_agerange = "youth"
elif(25 <= user_age <= 64):
    user_agerange = "adult"
elif (user_age >= 65):
    user_agerange = "senior"


# output after recieving the user's info in the form
print("Thank you for filling the form! Here's the info we received: State: " + user_state + ", Age Range: " + user_agerange +
      ", Gender: " + user_gender + ", Assistance: " + user_assistance + ". Your assigned ID will be " + state[user_state.lower()] + str(id_number))
