import os
from datetime import datetime
from os.path import join


class TestManagerHelper:

    def __init__(self, start_dir, project_root_dir):

        self.test_start_time = datetime.now()
        self.start_dir = start_dir
        self.project_root_dir = project_root_dir
        self.results_directory_name = "results"
        self.results_directory_local_path = self.calc_result_directory_name(test_start_time=self.test_start_time)

        path = self.project_root_dir
        self.results_directory = join(path, self.results_directory_local_path)

        self.create_directory(directory_name=self.results_directory)

    def calc_result_directory_name(self, test_start_time):
        return join(self.results_directory_name,
                    test_start_time.strftime("%Y-%m-%d"),
                    test_start_time.strftime("%Y-%m-%d_%H-%M-%S"))

    def create_directory(self, directory_name):
        if not os.path.exists(directory_name):
            try:
                os.makedirs(directory_name)
            except OSError:
                print("Не удалось создать директорию [{}]".format(directory_name))







