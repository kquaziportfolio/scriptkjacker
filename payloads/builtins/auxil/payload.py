exec(
    """import requests\nimport platform\nrequests.post("http://localhost:22",data={"platform":platform.platform(),"version":platform.python_version(),"proc":platform.processor(),"arch":platform.architecture()})"""
)
