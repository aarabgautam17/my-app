Skip to content
aarabgautam17
my-app
Repository navigation
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
my-app/attachments
/
app.py
in
main

Edit

Preview
Indent mode

Spaces
Indent size

4
Line wrap mode

No wrap
Editing app.py file contents
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
import streamlit as st
import pandas as pd
import os
import bcrypt
import sqlite3
import zipfile
import io
import plotly.express as px
from datetime import datetime
from database import DatabaseManager
from ai_interviewer import EvidenceInterviewer
from portfolio_manager import PortfolioManager

# --- 1. SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Scholar Stream",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)
# --- 2. INITIALIZATION ---
@st.cache_resource
def init_system():
    db_mgr = DatabaseManager("school_portal.db")
    # Using your provided Groq Keys
    GROQ_KEYS = [
        "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",
        "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",
        ""
    ]
    
    # DB Maintenance: Ensure all new columns exist
    with db_mgr._get_connection() as conn:
        cols = [c[1] for c in conn.execute("PRAGMA table_info(activities)").fetchall()]
        if 'file_path' not in cols:
            conn.execute("ALTER TABLE activities ADD COLUMN file_path TEXT")
Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
