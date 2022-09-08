'''
Created on 04-Sep-2019
rb_clone: 2022_09_07

@author: bkadambi, rb
'''

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return 'Hello, world from rb! (from port 8080) v1'

if __name__ == '__main__':  # Script executed directly?
    print("Hello, World, from rb (on stdout). Uses S2I to build the application.")
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
