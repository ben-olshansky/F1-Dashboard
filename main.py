import streamlit as st
import fastf1 as ff1
import fastf1.plotting
import fastf1.core
import pandas as pd
import os

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

os.makedirs("fastf1_cache", exist_ok=True)
ff1.Cache.enable_cache('fastf1_cache')

session = ff1.get_session(2026, "British Grand Prix", "R")
session.load()

print(session.results)