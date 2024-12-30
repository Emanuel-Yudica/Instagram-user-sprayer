import os
from urllib.parse import urlparse
from instagramFuzzer import findUser
from usernameGenerator import UsernameGenerator
from downloadProfilePic import ProfilePic
def main():
    if not os.path.exists("images"):
        os.mkdir("images")
    
    #initialize classes
    find_user=findUser()
    username_generator=UsernameGenerator()
    profile_pic=ProfilePic()
    user_list=username_generator.main()

    existing_urls=[]
    for user in user_list:
        existing_urls.append(find_user.find_instagram_id_by_username(user))
    formated_urls=[x for x in existing_urls if x]
    if formated_urls:
        print("Users found: \n")

        for url in formated_urls:
            parsed_url=urlparse(url)
            username=parsed_url.path.split("/")[1]
            profile_pic.download_profile_pic(username,f"images/{username}.jpg")
            print(url)            
        print("\nAll user images were saved at ./images")
    else:
        print("No user found")



if __name__ == "__main__":
    main()