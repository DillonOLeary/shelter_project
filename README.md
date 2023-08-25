# Shelter Project
This project is a basic donation inventory management application. I wrote it as a part of an interview for a volunteer position at Open Seattle.

## Project Requirements
1. Donation Registration: A feature that allows the shelter staff to record details of the donations, such as the donor's name, type of donation (money, food, clothing, etc.), quantity or amount donated, and the date of the donation.
1. Donation Distribution: A feature to log when and how much of the donations are distributed, capturing the type of donation, quantity or amount distributed, and the date of distribution.
1. Donation Reports: Your solution should have the capacity to generate two types of reports: (1) An inventory report displaying the current status of donations, grouped by type. (2) A donator report, summarizing the total contributions received from each donor.

----

To solve this, I created two solutions:

## Google Suite Solution
This solution uses the Google Suite to handle data intake and report generation. I strongly prefer this solution given my understanding of the requirements and I only worked on the FastAPI solution to highlight my coding.
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
This full stack solution uses [FastAPI](https://fastapi.tiangolo.com) for the backend and [React](https://react.dev) for the frontend.

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

### Running the backend server
To run the server:

```console
uvicorn app.main:app --reload
```

Once server is running, you can view generated API documentation at `http://127.0.0.1:8000/docs`

### Running the frontend server
In a different session, run:

```console
cd frontend
npm install
npm start
```

The frontend can be viewed at `http://localhost:3000`
