import io


class FileStorageService:

    def __init__(self, path):

        # open rw stream to path
        self.stream = io.open(path, "rw", encoding="utf-8")

    def save_raw(self, raw):
        if self.stream.closed:
            return

        # truncate to 0 bytes
        self.stream.truncate(0)

        # write raw to stream
        self.stream.write(raw)

    def fetch_raw(self):
        if self.stream.closed:
            return

        raw = self.stream.read()
        return raw

    def dispose(self):
        self.stream.close()
