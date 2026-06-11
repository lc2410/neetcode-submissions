class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folders = []
        for operation in logs:
            if operation == "../":
                if len(folders) != 0:
                    folders.pop()
            elif operation != "./":
                folders.append(operation)
        return len(folders)
                