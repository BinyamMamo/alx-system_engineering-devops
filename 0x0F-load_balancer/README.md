# 0x0F. Load balancer

<p>
<img width="50%" src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*0_AxDGA6rGF8ESMifA6j8w.gif">
</p>

## Introduction
This project focuses on the implementation and configuration of a load balancer within a web server environment. A load balancer efficiently distributes incoming network traffic across multiple servers to ensure no single server bears too much demand. It enhances the web infrastructure's performance and reliability by effectively managing network traffic.

## Tasks

| Task | Files | Description |
|------|-------|-------------|
| 0. Double the number of webservers | [0-custom_http_response_header](./0-custom_http_response_header) | scales the web server infrastructure by doubling the number of servers to handle increased traffic. |
| 1. Install your load balancer | [1-install_load_balancer](./1-install_load_balancer) | covers the installation and setup of the load balancer to manage traffic distribution. |
| 2. Add a custom HTTP header with Puppet | [2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp) | uses puppet to automate the addition of a custom HTTP header across all web servers. |
