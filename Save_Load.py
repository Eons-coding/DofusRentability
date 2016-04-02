import pickle


def save(to_save, file_name):
    pickle.dump(to_save, open(file_name, "wb"))
    print("Saved")


def load(file_name):
    return pickle.load(open(file_name, "rb"))
