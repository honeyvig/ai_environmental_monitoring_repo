from sensors.environment import read_environment
from vision.human_detection import detect_humans
from llm.reporter import generate_report
import time

while True:
    env = read_environment()
    humans = detect_humans()
    print(generate_report(env, humans))
    time.sleep(2)
