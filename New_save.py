def save_data(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        for name, pw in data.items():
            f.write(f"{name}={pw}\n")

def load_data(filename):
    data = {}
    if filename is None:
        return data
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "=" not in line:
                continue
            name, pw = line.split("=", 1)
            data[name.strip()] = pw.strip()
    return data