from flask import Flask, jsonify, request
from db import SessionLocal, Measurement

app = Flask(__name__)

@app.get("/api/latest")
def latest():
    session = SessionLocal()
    m = session.query(Measurement).order_by(Measurement.timestamp.desc()).first()
    session.close()
    if not m:
        return jsonify(None)
    return jsonify({
        "timestamp": m.timestamp.isoformat(),
        "temperature": m.temperature,
        "humidity": m.humidity,
        "pressure": m.pressure
    })

@app.get("/api/history")
def history():
    limit = int(request.args.get("limit", 100))
    session = SessionLocal()
    rows = (session.query(Measurement)
            .order_by(Measurement.timestamp.desc())
            .limit(limit)
            .all())
    session.close()
    rows = rows[::-1]
    return jsonify([
        {
            "timestamp": r.timestamp.isoformat(),
            "temperature": r.temperature,
            "humidity": r.humidity,
            "pressure": r.pressure
        } for r in rows
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
