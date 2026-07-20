import fastf1 as ff1
import matplotlib.pyplot as plt
import pandas as pd

session = ff1.get_session(2026, "Miami", "R")
session.load()

driver_amount = len(session.drivers)

laps = session.laps

drivers = []
for index, lap in laps.iterlaps():
  drivers.append(lap.Driver)
  print(lap.Driver)
  print(int(lap.Position) if pd.notna(lap.Position) else "N/A")
  print(int(lap.LapNumber) if pd.notna(lap.LapNumber) else "N/A")