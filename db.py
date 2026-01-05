from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///measurements.db", echo=False)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Measurement(Base):
    __tablename__ = "measurements"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    temperature = Column(Float)
    humidity = Column(Float)
    pressure = Column(Float)

Base.metadata.create_all(bind=engine)

def save_measurement(temp, hum, press):
    session = SessionLocal()
    m = Measurement(temperature=temp, humidity=hum, pressure=press)
    session.add(m)
    session.commit()
    session.close()
