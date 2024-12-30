import instaloader
class ProfilePic:
    def download_profile_pic(self,username,save_as):
        loader = instaloader.Instaloader()

        try:
            profile = instaloader.Profile.from_username(loader.context, username)

            loader.context.get_and_write_raw(profile.profile_pic_url, save_as)
        except Exception as e:
            print(f"Error downloading profile picture: {e}")

