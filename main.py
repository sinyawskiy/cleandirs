# -*- coding: utf-8 -*-
# author: anonimous
import os
import re

home_dir = os.path.expanduser('~')

def find_products():
    products = ['PhpStorm', 'PyCharm', 'WebStorm']
    version_re = re.compile('(\d+\.\d+)')
    find_products = []
    for sub_dir in os.listdir(home_dir):
        for product in products:
            if sub_dir.startswith('.{}'.format(product)):
                version_arr = version_re.findall(sub_dir)[0].split('.')
                find_products.append({
                    'path': os.path.join(home_dir, sub_dir),
                    'product': product,
                    'version_full': sub_dir,
                    'version': version_arr[1],
                    'year': version_arr[0]
                })
    return find_products

def print_menu(products):
    print 21 * "-" , "Clean dirs after trial" , 21 * "-"
    for number, product in enumerate(products, start=1):
        print '{}. {} {}.{}'.format(number, product['product'], product['year'], product['version'])
    print '{}. All'.format(number+1)
    print '{}. Exit'.format(number+2)
    print 66 * "-"

def clean_dirs(item):
    print 'Reset {} {} {}'.format(item['product'], item['year'], item['version'])
    try:
        rm_path = os.path.join(item['path'], 'config', 'eval', '{}{}{}.evaluation.key'.format(
            item['product'],
            item['year'][-2:],
            item['version']
        ))
        print 'Remove file {}'.format(rm_path)
        os.remove(rm_path)
    except OSError:
        pass

    try:
        rm_path = os.path.join(item['path'], 'config', 'options', 'options.xml')
        print 'Remove file  {}'.format(rm_path)
        os.remove(rm_path)
    except OSError:
        pass

    try:
        rm_dir = os.path.join(home_dir, '.java', '.userPrefs', 'jetbrains', '{}'.format(item['product'].lower()))
        print 'Remove dir {}'.format(rm_dir)
        os.system('rm -rf {}'.format(rm_dir))
    except OSError:
        pass


if __name__ == '__main__':
    products = find_products()
    loop = True
    while loop:
        print_menu(products)
        choice = input('Enter your choice [1-{}]:'.format(len(products)+2))
        if choice <= len(products):
            clean_dirs(products[choice-1])
        elif choice == len(products)+1:
            for item in products:
                clean_dirs(item)
        elif choice == len(products)+2:
            loop = False
        else:
            print "Wrong option selection. Enter any key to try again..."
