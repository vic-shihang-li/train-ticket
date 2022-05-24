from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        payload =  {\
                "startingPlace":"Shang Hai",\
                "endPlace":"Su Zhou",\
                "departureTime":"2022-05-31"}
        self.client.get("/api/v1/travelservice/trips/left",params = payload)
    
    # @task
    # def assurance(self):
    #     self.client.get("/api/v1/assuranceservice/assurances/types")

    @task
    def foodservice(self):
        self.client.get("/api/v1/foodservice/foods/2022-05-31/Shang%20Hai/Su%20Zhou/D1345")

    # @task
    # def contacts(self):
    #     self.client.get("/api/v1/contactservice/contacts/account/4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f")


