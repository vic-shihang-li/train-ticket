from locust import HttpUser, task


class TrainTicketUser(HttpUser):
    # Auth token used for certain API routes that require authentication.
    #
    # This is hard-coded for now... To retrieve a new auth token, look at
    # the HTTP headers of an authenticated route in the browser network tab.
    AUTH_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY1MzQyNzYyMSwiZXhwIjoxNjUzNDMxMjIxfQ.QF382moiLnnFvzYFH2N7pXw0J47Ct7Txvl0HzabJ5O0"

    @task
    def hello_world(self):
        payload = {
            "startingPlace": "Shang Hai",
            "endPlace": "Su Zhou",
            "departureTime": "2022-05-31",
        }
        self.client.get("/api/v1/travelservice/trips/left", params=payload)

    @task
    def assurance(self):
        self.client.get(
            "/api/v1/assuranceservice/assurances/types", headers=self.auth_header()
        )

    @task
    def foodservice(self):
        self.client.get(
            "/api/v1/foodservice/foods/2022-05-31/Shang%20Hai/Su%20Zhou/D1345"
        )

    @task
    def contacts(self):
        account_id = "4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f"
        self.client.get(
            f"/api/v1/contactservice/contacts/account/{account_id}",
            headers=self.auth_header(),
        )

    def auth_header(self):
        return {"Authorization": f"Bearer {TrainTicketUser.AUTH_TOKEN}"}
