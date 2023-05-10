from locust import LoadTestShape, HttpUser, TaskSet, task, constant, between
from locust.clients import HttpSession

api_v1 = "/desktop/v1/recommendations?count=30&locale={0}&region={0}&consumer_key=94110-6d5ff7a89d72c869766af0e0"

class NewTabInternaionalTasks(TaskSet):
    @task
    def it(self):
        self.user.client.get(api_v1.format("it"))

    @task
    def fr(self):
        self.user.client.get(api_v1.format("fr"))

    @task
    def sp(self):
        self.user.client.get(api_v1.format("es"))

    @task
    def spoc(self):
        self.user.spoc_client.get("/pulse")


class MultipleHostsUser(HttpUser):
    abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spoc_client = HttpSession(
            base_url="https://spocs.getpocket.com", request_event=self.client.request_event, user=self
        )

class NewTabUser(MultipleHostsUser):
    wait_time = between(2,5)
    host = "https://firefox-api-proxy.readitlater.com"
    tasks = [NewTabInternaionalTasks]

class StagesShape(LoadTestShape):

    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10},
        {"duration": 100, "users": 50, "spawn_rate": 10},
        {"duration": 180, "users": 100, "spawn_rate": 10},
        {"duration": 220, "users": 30, "spawn_rate": 10},
        {"duration": 230, "users": 10, "spawn_rate": 10},
        {"duration": 240, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
