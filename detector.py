from utils import analyze_url

def main():
    url = input("Enter URL: ")
    score, reasons = analyze_url(url)

    print("\n🔍 Analysis Result:")
    
    if score >= 3:
        print("Risk Score: HIGH 🚨")
    elif score == 2:
        print("Risk Score: MEDIUM ⚠️")
    else:
        print("Risk Score: LOW ✅")

    print("\nReasons:")
    for r in reasons:
        print(f"- {r}")

if __name__ == "__main__":
    main()
