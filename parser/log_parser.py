def parse_log(file_path):
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            logs.append(line.strip())
    return logs
if __name__ == "__main__":
    logs = parse_log("parser/sample_logs/auth.log")
    for log in logs:
        print(log)
       #hello 
        

