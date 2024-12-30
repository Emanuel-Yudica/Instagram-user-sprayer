from usernameMatcher import usernameAdder
class UsernameGenerator:
    def __init__(self):
        self.namesList=[]
    def makeCombinatories(self,username,middlename,lastname):
        try:
            self.namesList.extend([
            f"{username}{lastname}_",
            f"{username}{lastname}__",
            f"{username}{lastname}___",
            f"{username}.{lastname}",
            f"{username}{lastname}",
            f"{username[0]}.{lastname}",
            f"{username[0]}{lastname}",
            f"{username[0]}{username[1]}.{lastname}",
            f"{username}.{lastname[0]}",
            f"{username}_{lastname}",
            f"{lastname}{username}"
            ])
            if middlename:
                self.namesList.extend([
                f"{username}{middlename}{lastname}_",
                f"{username}{middlename}{lastname}__",
                f"{username}{middlename}{lastname}___",
                f"{username}{middlename[0]}.{lastname}",
                f"{username}{middlename[0]}{lastname}",
                f"{username[0]}{middlename[0]}{lastname}",
                f"{username[0]}{middlename[0]}.{lastname}",
                f"{username[0]}.{middlename[0]}.{lastname}",
                f"{username[0]}{middlename[0]}{lastname}",
                f"{username}.{middlename[0]}.{lastname[0]}",
                f"{username}_{middlename[0]}_{lastname}"
                ])
        except Exception as e:
            print(e)

        #print(self.namesList)
    
    def main(self):
        usernameMatcher=usernameAdder()
        usernames,middlename,lastname=usernameMatcher.main()
        for nickname in usernames:
            self.makeCombinatories(nickname,middlename,lastname)
        return self.namesList

if __name__ == "__main__":
    user=UsernameGenerator()
    user.main()