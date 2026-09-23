from datetime import datetime


def analyze_heartbeat():
    with open("hblog.txt", "r") as f:
        data = f.readlines()

    filtered_log = []
    for line in data:
        if "Key TSTFEED0300|7E3E|0400" in line:
            filtered_log.append(line)

    with open("hb_test.log", "w") as report:
        for i in range(len(filtered_log) - 1):
            current_line = filtered_log[i]
            next_line = filtered_log[i + 1]

            start = current_line.find("Timestamp ") + len("Timestamp ")
            current_str = current_line[start:start + 8]

            start = next_line.find("Timestamp ") + len("Timestamp ")
            next_str = next_line[start:start + 8]

            current_time = datetime.strptime(current_str, "%H:%M:%S")
            next_time = datetime.strptime(next_str, "%H:%M:%S")
            heartbeat = (current_time - next_time).total_seconds()

            if heartbeat >= 33:
                report.write("ERROR: heartbeat " + str(int(heartbeat)) + "s at " + current_str + "\n")
            elif heartbeat > 31:
                report.write("WARNING: heartbeat " + str(int(heartbeat)) + "s at " + current_str + "\n")


analyze_heartbeat()