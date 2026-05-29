import requests

API = "API-KEY"

features = int(input("OPTIONS:\n1. Scan URL \n2. Scan IP reputation \nEnter: "))

match features:
    case 1:
        url = input("Enter URL: ")
        api_url = "https://www.virustotal.com/api/v3/urls"

        headers={
            "x-apikey": API
        }

        data = {
            "url":url
        }

        response = requests.post(api_url, headers=headers, data=data)

        result = response.json()

        scan_id = result["data"]["id"]

        result_url = f"https://www.virustotal.com/api/v3/analyses/{scan_id}"

        scan_result = requests.get(result_url, headers=headers)

        scan_data = scan_result.json()


        stats = scan_data["data"]["attributes"]["stats"]

        print("\n===== RESULTS =====")
        print("Malicious :", stats["malicious"])
        print("Suspicious:", stats["suspicious"])
        print("Harmless  :", stats["harmless"])
        print("Undetected:", stats["undetected"])

