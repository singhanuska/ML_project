import logging 
import os
from datetime import datetime

log_file_name = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", log_file_name)    
os.makedirs(os.path.dirname(logs_path), exist_ok=True)


logging.basicConfig(
    filename=logs_path,         
    format='[%(asctime)s] %(levelname)s - %(message)s',
    level=logging.INFO,
)