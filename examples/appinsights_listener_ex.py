from locust_plugins.appinsights_listener import ApplicationInsightsListener
from locust import HttpUser, task, events, between

class MyHttpUser(HttpUser):
    @task
    def index(self):
        self.client.get("/Guilhermeslucas/locust-plugins")

    host = "https://github.com"
    wait_time = between(4, 10)


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    ApplicationInsightsListener(env=environment, instrumentation_key="<YOUR-APP-INSIGHTS-INSTRUMENTATION-KEY>")