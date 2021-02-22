#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import make_response, redirect

app = Flask(__name__)


@app.route('/')
def redirect_pager():
    return redirect("https://www.facebook.com")


@app.route('/<page_name>')
def other_page(page_name):
    response = make_response('The page named %s does not exist.' % page_name, 404)
    return response


if __name__ == '__main__':
    app.run(debug=True)
