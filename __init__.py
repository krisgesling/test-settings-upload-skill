from mycroft import MycroftSkill, intent_file_handler


class TestSettingsUpload(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('upload.settings.test.intent')
    def handle_upload_settings_test(self, message):
        self.speak_dialog('upload.settings.test')


def create_skill():
    return TestSettingsUpload()

