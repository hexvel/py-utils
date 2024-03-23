import os
import shutil
from typing import List, Union


class ShellCommands:
    def get_files_in_directory(self, directory: str) -> List[str]:
        """
        Return a list of files in the given directory and its subdirectories.
        """
        files = []
        for root, _, filenames in os.walk(directory):
            for file in filenames:
                files.append(os.path.join(root, file))
        return files

    def copy_file(self, source: str, destination: str) -> Union[str, None]:
        """
        Copy the source file to the destination. Return a success message or an error message.
        """
        try:
            shutil.copy(source, destination)
            return f"File '{source}' copied to '{destination}' successfully."
        except Exception as e:
            return f"Error while copying file {source}: {str(e)}"

    def move_file(self, source: str, destination: str) -> Union[str, None]:
        """
        Move the source file to the destination. Return a success message or an error message.
        """
        try:
            shutil.move(source, destination)
            return f"File '{source}' moved to '{destination}' successfully."
        except Exception as e:
            return f"Error while moving file {source}: {str(e)}"

    def delete_file(self, file: str) -> Union[str, None]:
        """
        Delete the given file. Return a success message or an error message.
        """
        try:
            os.remove(file)
            return f"File '{file}' deleted successfully."
        except Exception as e:
            return f"Error when deleting file {file}: {str(e)}"
