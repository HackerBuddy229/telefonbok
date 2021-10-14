from io import open


class FileStorageService:

    @staticmethod
    def save_raw(path, raw):
        # open rw stream to path
        stream = open(path, "w", encoding="utf-8")

        # truncate to 0 bytes
        stream.truncate(0)

        # write raw to stream
        stream.write(raw)

        # close stream
        stream.close()

    @staticmethod
    def fetch_raw(path):
        # open rw stream to path
        stream = open(path, "r", encoding="utf-8")

        raw = stream.read()

        # close stream
        stream.close()

        return raw
