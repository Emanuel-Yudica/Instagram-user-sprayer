class usernameAdder:
    def __init__(self):
        pass
    def checkSimilarity(self,username):
        names=[]
        with open('names.txt', 'r') as f:
            usernames = [line.strip().lower() for line in f] 
        min_coincidence = 4

        for wordlist in usernames:
            common_letters = len(set(username[0]).intersection(set(wordlist)))
            if common_letters >= min_coincidence or wordlist in username:
                if len(username) > len(wordlist):
                    if username[0:2]==wordlist[0:2] : #Remove this in case the nickname don't start with the first letter of the username
                        names.append(wordlist)
        return names

    def setNames(self,username,answer):
        nicknames=[username]
        nicknames.extend(answer.split())
        return nicknames




    def main(self):
        name=input("Enter user name: ").split(" ")
        username=name[0].lower()
        last_name=name[-1].lower()
        if len(name)==3:
            middle_name=name[1].lower()
        suggested_names=self.checkSimilarity(username)

        if suggested_names:
            print("Sugested names: ")
            print(",".join([name.title() for name in suggested_names]))
        else:
            print("No suggested names were found.")
        answer=input("Write the names that you want to search (nicknames): ").lower()
        nicknames=self.setNames(username,answer)
        if len(name)==3:
            middle_name=name[1].lower()
            return nicknames,middle_name,last_name
        return nicknames,None,last_name
