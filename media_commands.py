is_playing = False
has_video = False
## remember to comment this out later
valid = True

def isnumber(str):
    dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return all([c in dig for c in str])

async def execute(message, args, flags):
    global is_playing
    global has_video
    print("is_playing:")
    if is_playing:
        print("Yes")
    else:
        print("No")
    print("has_video:")
    if has_video:
        print("Yes")
    else:
        print("No")
    if args[0] == "play":
        if valid == False:
            await message.channel.send("Enter a valid video")
            return
        else:
            ## check flags
            if not flags:
                await message.channel.send("Enter at least 1 flag")
                return
            elif len(flags) == 1:
                flag = flags[0].split(":")
                ## since single flag, cannot be s
                if flag[0] != "-v":
                    await message.channel.send("Invalid flag")
                    return
                else:
                    print(type(flag[1]))
                    print(flag[1])
                    flag[1] = flag[1].lstrip("0")
                    print(flag[1])
                    ## in case flag[1] = 0
                    if not flag[1]:
                        flag[1] = "0"
                    if not isnumber(flag[1]):
                        await message.channel.send("Enter a positive integer for the volume")
                        return
                    await message.channel.send("Playing the video at volume " + flag[1])
                    has_video = True
                    is_playing = True
                    return
            elif len(flags) == 2:
                ## split so we can parse the validity
                flag1 = flags[0].split(":")
                flag2 = flags[1].split(":")
                ## add to a set
                allflags = set()
                allflags.add(flag1[0])
                allflags.add(flag2[0])
                ## check if "-s" and "-v" are present
                if "-s" in allflags and "-v" in allflags:
                    flag1[1] = flag1[1].lstrip("0")
                    if not flag1[1]:
                        flag1[1] = "0"
                    flag2[1] = flag2[1].lstrip("0")
                    if not flag2[1]:
                        flag2[1] = "0"
                    if not isnumber(flag1[1]) or not isnumber(flag2[1]):
                        await message.channel.send("Enter a positive integer for the volume and speed")
                        return
                    volume = ""
                    speed = ""
                    if (flag1[0] == "-s"):
                        speed = flag1[1]
                        volume = flag2[1]
                    else:
                        speed = flag2[1]
                        volume = flag1[1]
                    await message.channel.send("Playing the video at volume " + volume + " and at speed " + speed)
                    has_video = True
                    is_playing = True
                    return
            else:
                await message.channel.send("Too many flags")
                return has_video, is_playing
    elif args[0] == "pause":
        ## should have no flags
        if flags:
            await message.channel.send("Too many flags")
            return
        if not has_video:
            await message.channel.send("start playing a video before trying to pause")
        if not is_playing:
            await message.channel.send("Your video is already paused")
        else:
            is_playing = False
            await message.channel.send("Paused the video")
        return
    elif args[0] == "continue":
        ## shoulve have no flags
        if flags:
            await message.channel.send("Too many flags")
            return
        if not has_video:
            await message.channel.send("start playing a video before trying to continue")
        if is_playing:
            await message.channel.send("Your video is already playing")
        else:
            is_playing = True
            await message.channel.send("Resumed the video")
        return
