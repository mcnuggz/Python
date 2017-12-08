with open("files/write.txt", 'w') as write_file:
    write_file.write('Python is pretty awesome!')

with open("files/write.txt", 'a') as write_file:
    write_file.write('\nI love it so much!')

quotes = [
    "\nI'm recording this because it could be the last thing I'll ever say ",
    "\nThe city I once knew as home is teetering on the edge of radioactive oblivion",
    "\nA three-hundred thousand degree baptism by nuclear fire", 
    "\nI'm not sorry, we had it coming",
    "\nA surge of white-hot atonement will be our wake-up call",
    "\nHope for our future is now a stillborn dream",
    "\nThe bombs begin to fall and I'm rushing to meet my love",
    "\nPlease, remember me",
    "\nThere is no more"
]

with open("files/write.txt", 'a') as write_file:
    write_file.writelines(quotes)