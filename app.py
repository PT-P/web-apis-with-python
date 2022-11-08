from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/data")
def index():

    name = request.args.get("nama")

    thoriq = {
        "nama": "Thoriq",
        "umur": 20,
        "ttl": "8 mei 2002",
        "sekolah": {
            "sma": {
                "nama": "SMAN 1 BOGOR",
                "lokasi": "jl selot"
            },
            "kuliah": {
                "nama": "ITB",
                "lokasi": "jl ganesha"
            }
        }
    }

    vixell = {
        "nama": "Vixell",
        "umur": 20,
        "ttl": "18 juni 2002",
        "sekolah": {
            "sma": {
                "nama": "SMA KOLESE LOYOLA",
                "lokasi": "jl karanganyar"
            },
            "kuliah": {
                "nama": "ITB",
                "lokasi": "jl ganesha"
            }
        }
    }
    response = {
        "status": "failed to obtain data"
    }

    if (not name) or (name == "thoriq-vixell" or name == "vixell-thoriq"):
        response = {
            "data": [thoriq, vixell]
        }

    elif name == "thoriq":
        response = {
            "data": thoriq
        }

    elif name == "vixell":
        response = {
            "data": vixell
        }

    return jsonify(response)