import os

def update_settings(settings_xml_string):
    if not os.path.exists('settings/'):
        os.makedirs('settings/')
    settings_file = open('settings/settings.xml', 'w')
    settings_file.write(settings_xml_string)
    settings_file.close()
    return settings_xml_string