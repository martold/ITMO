from routeros_ssh_connector import MikrotikDevice

router = MikrotikDevice()
router.connect("192.168.88.1", "root", "Qwerty123")
print(router.send_command("/export"))
router.send_command('/export file=config')
print(router.get_export_configuration())
print(router.download_file("config.rsc",'/Users/admin/Desktop/'))
router.disconnect()
del router