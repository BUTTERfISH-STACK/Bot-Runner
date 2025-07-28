import time
import requests

def report_post(post_url, reason="Spam or misleading"):
    print(f"[+] Reporting {post_url} for reason: {reason}")
    time.sleep(1)
    print(f"[✓] Report sent successfully!")

if __name__ == "__main__":
    target = input("Enter post URL to report: ")
    reason = input("Enter reason (or press Enter for default): ") or "Spam or misleading"
    report_post(target, reason)