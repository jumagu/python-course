from datetime import datetime

message = "Deserunt reprehenderit sit fugiat commodo non consectetur elit."
date = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

with open("test_files/logs.txt", "a") as my_log_file:
    my_log_file.write(f"[{date}] {message}\n")
