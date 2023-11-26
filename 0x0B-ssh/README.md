# 0x0B. SSH

<p>
<img width="100%" src="https://media.licdn.com/dms/image/D4D12AQFXt7gIL21dig/article-inline_image-shrink_1000_1488/0/1676585456892?e=1706140800&v=beta&t=yerlnf-aiH2THAu9T8Da7bREtZ8IsaQcB5U9CmmJxFQ">
</p>

This project is about learning how to use SSH to connect to remote servers and perform various tasks. SSH is a secure protocol that allows encrypted communication between two machines over a network.

## Tasks

| Task | Files | Description |
| ---- | ----- | ----------- |
| 0. Use a private key | [0-use_a_private_key](./0-use_a_private_key) | uses ssh to connect to a server using a private key. |
| 1. Create an SSH key pair | [1-create_sshkey_pair](./1-create_sshkey_pair) | creates an RSA key pair. |
| 2. Client configuration file | [2-ssh_config](./2-ssh_config) | sets the default identity file, the preferred authentication method, and the port for the local SSH server. |
| 3. Let me in! | None | requires adding the public key to the server so that we can connect using ssh. |
| 4. Client configuration file (w/ Puppet) | [100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp) | configures the ssh client with the same settings as task 2. |

This project is a great way to learn how to use SSH for secure and convenient remote access. SSH is an essential tool for any system administrator or DevOps engineer.
