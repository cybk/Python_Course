import pickle

colors  = ["blue", "green", "red2", "yellow"]
with open("colors_file.pkcl", "wb") as colors_file:
    pickle.dump(colors, colors_file)
