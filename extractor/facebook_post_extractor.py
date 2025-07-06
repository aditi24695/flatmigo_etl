import pandas as pd
import numpy as np
import re
import json
import sqlite3
from datetime import datetime, timedelta
import requests
from typing import Dict, List, Optional, Tuple
import logging
from dataclasses import dataclass
from abc import ABC, abstractmethod
import time
import hashlib

# Configure logging
logging.basicConfig(level=logging.INFO)



class FlatmateDataExtractor:
    def __init__(self):
        pass