import time
import random

def shadow_report(username):
    print(f"[SHDW] Launching deep report sequence on @{username}")
    time.sleep(random.uniform(0.5, 1.5))
    reasons = ["Hate speech", "Impersonation", "Fake account", "Scam"]
    for reason in reasons:
        print(f"[SHDW] Reporting for: {reason}")
        time.sleep(random.uniform(0.5, 1.2))
    print(f"[SHDW] Stealth report wave completed.")

if __name__ == "__main__":
    target = input("Enter username to shadow report: ")
    shadow_report(target)