from firebase_functions import https_fn, options, params, pubsub_fn


@https_fn.on_request()
def onrequestexample(req: https_fn.Request) -> https_fn.Response:
    print("on request function data:", req.data)
    return https_fn.Response("Hello from https on request function example")