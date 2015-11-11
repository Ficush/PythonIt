import sublime
import sublime_plugin

class PythonItCommand(sublime_plugin.WindowCommand):

	def run(self):
		
		sourceView   = self.window.active_view()
		sourceViewID = sourceView.id()
		sourceFile   = sourceView.file_name()
		sourceWindow = sourceView.window()

		for index, currentview in enumerate(sourceWindow.views()):
			if currentview.id() == sourceViewID:
				if index > 0:
					self.buildinAnotherWindow(sourceView,sourceWindow,sourceFile)
				else:
					self.buildinSameWindow(sourceView,sourceWindow)
				break
			else:
				continue

		sublime.status_message("Build in Window! ")

	def buildinAnotherWindow(self,sourceView,sourceWindow,sourceFile):
		sourceView.run_command('save')
		sourceWindow.run_command('close')
		sublime.run_command('new_window')
		newSourceWindow = sublime.active_window()
		newSourceWindow.open_file(sourceFile)
		newSourceWindow.run_command('build')

	def buildinSameWindow(self,sourceView,sourceWindow):
		sourceView.run_command('save')
		sourceWindow.run_command('build')
