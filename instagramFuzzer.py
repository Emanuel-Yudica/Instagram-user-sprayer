import requests
class findUser:

    def find_instagram_id_by_username(self,username):
        url = f"https://www.instagram.com/{username}/"
        headers={
            'User-Agent':'Instagram 10.3.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+'
        }
        response = requests.get(url,headers=headers)
        user_id=response.text.find("profile_id")
        if user_id != -1:
            return url
        else:
            return None
