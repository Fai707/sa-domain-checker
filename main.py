import requests
import csv

with open("available_domains.csv", "a", newline="") as f:
    write = csv.writer(f)

    if f.tell() == 0:
        write.writerow(["domain", "isAvailable"])


    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    domains = ["ax.sa"]

    for a in chars:
        domains.append(a + ".sa")

    for a in chars:
        for b in chars:
            domains.append(a + b + ".sa")

    for a in chars:
        for b in chars:
            for c in chars:
                domains.append(a + b + c + ".sa")


    for domain in domains:
        response = requests.post("https://api-domains.solutions.com.sa/v1/open/domains/search?checkVariant=true",json={"domainName": domain})
        data = response.json()
        write.writerow([domain, data.get("isAvailable")])
        print(domain, data.get("isAvailable"))
