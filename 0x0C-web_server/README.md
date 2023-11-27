# 0x0C. Web server

<P>
<img width="100%" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png">
</p>

This project is about setting up and configuring a web server using Nginx and Puppet.

## Tasks

| Task | Files | Description |
| ---- | ----- | ----------- |
| 0. Transfer a file to your server | [0-transfer_file](./0-transfer_file) | transfers a file from our client to a server. |
| 1. Install nginx web server | [1-install_nginx_web_server](./1-install_nginx_web_server) | configures a new Ubuntu machine with Nginx installed and listening on port 80. |
| 2. Setup a domain name | [2-setup_a_domain_name](./2-setup_a_domain_name) | contains the domain name set up for the server using Gandi. |
| 3. Redirection | [3-redirection](./3-redirection) | configures the Nginx server to redirect `/redirect_me` to another page. |
| 4. Not found page 404 | [4-not_found_page_404](./4-not_found_page_404) | configures the Nginx server to have a custom 404 page. |
| 5. Install Nginx web server (w/ Puppet) | [7-puppet_install_nginx_web_server.pp](./7-puppet_install_nginx_web_server.pp) | sets up a web server with Nginx, with a custom 404 page and a redirection. |

## Conclusion

This project demonstrates the basic skills of web server administration and automation using Bash and Puppet. It also introduces the concept of DNS and how to set up a domain name for a server.
