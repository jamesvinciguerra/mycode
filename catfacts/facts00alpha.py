#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""


import requests

def main():
    """Run time code"""
    
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    
    print( dir(r) )
main()

