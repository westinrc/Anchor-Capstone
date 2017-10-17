
def update_settings(settings_xml_string):
    settings_file = open('settings.xml', 'w')
    settings_file.write(settings_xml_string)
    settings_file.close()
    return settings_xml_string