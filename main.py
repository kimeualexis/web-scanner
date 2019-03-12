from base import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

ROOT_DIR = 'scans'
create_dir(ROOT_DIR)


def run_scan(name, url):
    domain_name = get_domain_name(url)
    ip = get_ip_address(url)
    nmap = get_nmap('-F', ip)
    robots = get_robots_txt(url)
    whois = get_whois(domain_name)
    save_data(name, url, domain_name, nmap, robots, whois)


def save_data(name, url, domain_name, nmap, robots, whois):
    site_dir = ROOT_DIR + '/' + name
    create_dir(site_dir)
    write_file(site_dir + '/url.txt', url)
    write_file(site_dir + '/domain.txt', domain_name)
    write_file(site_dir + '/nmap.txt', nmap)
    write_file(site_dir + '/robots.txt', robots)
    write_file(site_dir + '/whois.txt', whois)


