class Solution:
    def minOperations(self, logs: List[str]) -> int:
        current_path = []
        for log in logs:
            if log == './':continue
            if log == '../':
                if current_path: 
                    current_path.pop()
                continue
            current_path.append(log)

        return len(current_path)