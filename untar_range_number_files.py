import tarfile

for i in range(1, 1001):
    filename = f"file_{i}.tar.gz"
    with tarfile.open(filename, "r:gz") as tar:
        tar.extractall()
