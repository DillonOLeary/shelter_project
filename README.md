# Shelter Project
This project is a basic donation inventory management application. I wrote it as a part of an interview for Open Seattle.

To solve this, I created two solutions:

## Google Suite Solution
This solution uses the Google Suite to handle data intake and report generation. I strongly prefer this solution given my understanding of the requirements and only worked on the FastAPI solution to highlight my coding.
- Donation Registration Form: `https://forms.gle/Cjf4HdFWKvvPTjcf8`
  - staff can record donations here
- Donation Distribution Form: `https://forms.gle/dqnYfcab7yVNYmkE9`
  - donations that have been distributed can be recorded here
- All Shelter Data, including a donation balances report: `https://docs.google.com/spreadsheets/d/1Ehh3CRvd2P31k7PUY93IfwpYoGridXFWKaw_pgLwTWw/edit?usp=sharing`

Pros of this solution:
- fast to make, required no coding knowledge other than some knowledge of Google Sheets functions
  - because of this, we can enable the client to extend this product without our support
- managed service, so we are not on the hook if something goes wrong with the software
- great interface
- can integrate well with other tools if the organization already uses Google Suite

Cons:
- we are making our client dependent on Google, so Google could make changes they don't like
- be not coding a solution, we give up some fine grained control. Google Suite is pretty extensive, so I don't think this would be much of an issue
----
## FastAPI Solution (AKA this code)

## How to run
Commands for linux/mac

### Setting up the enviroment

First, create a virtual enviroment and activate it:

```console
python3 -m venv venv
source venv/bin/activate
```

Then install the dependencies:

```console
pip install -r requirements.txt
```

### Running the server
To run the server:

```console
uvicorn app.main:app --reload
```

Once server is running, you can view generated API documentation at `http://127.0.0.1:8000/docs`

----
## Full interview prompt

Imagine you're tasked with creating a practical solution for a local shelter to manage their donation inventory. This shelter is in need of a user-friendly tool to accurately record and track the inflow and outflow of donations, and to generate insightful reports about their donation management.

Here are the core functionalities your solution should address:

1. Donation Registration: A feature that allows the shelter staff to record details of the donations, such as the donor's name, type of donation (money, food, clothing, etc.), quantity or amount donated, and the date of the donation.
1. Donation Distribution: A feature to log when and how much of the donations are distributed, capturing the type of donation, quantity or amount distributed, and the date of distribution.
1. Donation Reports: Your solution should have the capacity to generate two types of reports: (1) An inventory report displaying the current status of donations, grouped by type. (2) A donator report, summarizing the total contributions received from each donor.

Feel free to select any programming language that you're most comfortable with. We want you to showcase your coding abilities, problem-solving prowess, and ability to operate under ambiguity. 

To clarify, you don't need to spend your time on setting up a database or creating a complex frontend. Your primary focus should be on the core functionalities mentioned above. However, if there's a particular area in which you excel, such as data modeling, frontend design, testing, or anything else, feel free to include that in your solution to show off your strengths. This will allow us to better understand if you have the abilities we currently need. 

Along with your code + comments, we'd appreciate clear instructions on how to run the code.

Remember, this exercise is not about checking boxes, but about allowing you the freedom to demonstrate your unique strengths and approach to problem-solving. We're excited to see what you can create!

