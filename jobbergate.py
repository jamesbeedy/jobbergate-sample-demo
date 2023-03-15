from jobbergate_cli.subapps.applications.application_base import JobbergateApplicationBase
from jobbergate_cli.subapps.applications.questions import Text


class JobbergateApplication(JobbergateApplicationBase):

    def mainflow(self, data=None):
        if data is None:
            data=dict()
        data["nextworkflow"] = "subflow"
        return [
            Text("foo", message="gimme the foo!"),
            Text("bar", message="gimme the bar!"),
        ]

    def subflow(self, data=None):
        if data is None:
            data=dict()
        return [
            Text("baz", message="gimme the baz!", default="zab"),
            Text("workdir", message="gimme the workdir!", default="/myuserhomedir"),
            Text("job_name", message="Input the desired job-name!", default="my-job"),
        ]
