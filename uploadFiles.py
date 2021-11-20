import dropbox
import os
import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)

        relative_path = os.path.relpath(local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)

        with open(local_path, "rb") as f:
            dbx.files_upload(f.read(), dropbox_path, mode = WriteMode("overwrite"))


def main():
    access_token = "yKaTa1XPr3kAAAAAAAAAAfiRoxPXqKZbZK_qHhee75EbYCaQ-6ibcMcv55oIxiAl"
    transferData = TransferData(access_token)

    file_from = input("Enter the folder path to transfer :-")
    file_to = input("Enter the path for dropbox upload :-")

    transferData.upload_file(file_from, file_to)
    print("The file is succesfully moved!!!")

main()