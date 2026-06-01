import requests # type: ignore

def main():
    url = "https://api.github.com"
    
    response = requests.get(url)
    print(response.json())
    
    print("Status Code:", response.status_code)
    print("Headers:", response.headers.get("content-type"))
    print("API Message:", response.json().get("current_user_url"))
    
if __name__ == "__main__":
    main()
    
    