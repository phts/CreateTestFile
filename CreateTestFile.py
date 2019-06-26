import sublime
import sublime_plugin
import os

class CreateTestFileCommand(sublime_plugin.WindowCommand):
    def run(self):
        file_path = self.window.active_view().file_name()
        if not file_path:
            return

        pair = os.path.splitext(file_path)
        new_test_file_name = pair[0] + '.test' + pair[1]
        open(new_test_file_name, 'a').close()
        self.window.open_file(new_test_file_name)
