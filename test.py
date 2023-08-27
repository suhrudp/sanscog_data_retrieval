
import os
import hashlib

def hash_string(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

from flask import Flask, session, render_template, request, redirect, url_for, jsonify, make_response
from flask_session import Session   
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



if __name__ == "__main__":
    print(hash_string("jonaslab123"))
