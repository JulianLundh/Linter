class Report:
    def __init__(self, path):
        self.path = path
        self.results = {}

    def add_result(self, file_type, status, file_path, amount_found):
        self.results[file_type] = {
            "status": status,
            "file_path": file_path,
            "amount_found": amount_found,
        }

    def show_report(self):
        for file_type, data in self.results.items():
            print(
                f"{data['status']} {file_type.capitalize()} | Amount found: {data['amount_found']}"
            )
