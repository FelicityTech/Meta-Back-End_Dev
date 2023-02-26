class FileExtensionError(ValueError):
    def process_file(filename):
        if not filename.endswith(".txt"):
            raise FileExistsError("filename must have .txt extension")