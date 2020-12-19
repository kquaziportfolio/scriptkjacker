from flask import Flask,request
app=Flask(__name__)
@app.route("/",methods=["POST"])
def main():
    print("Recieved message from IP address", request.remote_addr)
    for k in request.form:
        print(f"{k}: {request.form[k]}")
    return "hai"
app.run(port=22)
