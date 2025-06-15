DJ_Playlist=[]
print("DJ Playlist")
while(True):
    print("*Menu")
    print("1.enter 1 to add a song to playlist ")
    print("2.enter 2 to Show the Playlist ")
    print("3.enter 3 to Exit ")
    Choice=int(input("Enter your Choice :"))
    if(Choice>=1 and Choice<=3):
        if(Choice==1):
            Name=input("Enter the name of the song :")
            DJ_Playlist.append(Name)
            print(f"{Name} is added to playlist")
        elif(Choice==2):
            print("Normal Order :",DJ_Playlist)
            print(DJ_Playlist[::-1])
        else:
            print("DJ")
            break
    else:
        print("In-valid Input....!")