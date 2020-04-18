# def test_reboot(ssh_client, random_product_name):
#     ssh_client.exec_command('echo {} > test'.format(random_product_name))
#     stdin, stdout, stderr = ssh_client.exec_command('cat test')
#     data = (stdout.read() + stderr.read()).decode().strip()
#     assert data == random_product_name
